import copy
import json
import unittest
from pathlib import Path

from validator import ValidationError, render_concise, validate_document


HERE = Path(__file__).resolve().parent


def fixture(name):
    return json.loads((HERE / "fixtures" / f"{name}.json").read_text(encoding="utf-8"))


def fence(token="rev:1", currentness="CURRENT"):
    return {"token": token, "currentness": currentness}


def minimal_repair():
    return {
        "kind": "counterfactual_repair_explanation_v0",
        "baseline_explanation_ref": {
            "source_ref": "explanation:finance:baseline",
            "target_use_ref": "finance:egress-current",
            "fence": fence("baseline:1"),
        },
        "target_use": {
            "id": "finance:egress-current",
            "contract_ref": "finance:egress-current:v1",
            "scope": "restore exact current-egress target",
            "snapshot": "post-intervention",
            "spans_intervention_horizon": True,
        },
        "intervention_plan": {
            "id": "plan:recover-egress",
            "owner_ref": "ordivon-workstation",
            "plan_ref": "workstation:repair-plan:1",
            "fence": fence("plan:1"),
            "action_refs": ["workstation:action:recover-member"],
        },
        "counterfactual_effects": [
            {
                "id": "effect:restored",
                "effect_kind": "hypothetical",
                "effect_contract_ref": "workstation:effect-contract:1",
                "fence": fence("effect:1"),
                "outcome_scope": "poststate",
                "postcondition_witness_refs": ["workstation:postcondition:egress-current"],
            }
        ],
        "closure_witnesses": {
            "E": {"ref": "closure:E", "fence": fence("closure:E:1")},
            "D": {"ref": "closure:D", "fence": fence("closure:D:1")},
        },
        "repair_claims": [
            {
                "kind": "SUFFICIENT_AT_POSTSTATE_UNDER_EFFECT_CONTRACT",
                "effect_refs": ["effect:restored"],
                "witness_refs": ["workstation:postcondition:egress-current"],
                "scope": "poststate",
                "model_relative": True,
            }
        ],
        "assessment": {"status": "EXPLAINED"},
    }


class CapabilityPathTests(unittest.TestCase):
    def test_positive_finance_research_harness(self):
        for name in ("finance", "research", "harness"):
            with self.subTest(name=name):
                result = validate_document(fixture(name))
                self.assertEqual(result["assessment"], "EXPLAINED")
                self.assertIn("Target:", render_concise(fixture(name)))

    def test_missing_relation_contract_fails(self):
        doc = fixture("finance")
        del doc["justification_edges"][0]["relation_contract_ref"]
        with self.assertRaises(ValidationError):
            validate_document(doc)

    def test_stale_fence_requires_invalidated(self):
        doc = fixture("finance")
        doc["source_facts"][0]["fence"]["currentness"] = "STALE"
        with self.assertRaises(ValidationError):
            validate_document(doc)
        doc["assessment"]["status"] = "INVALIDATED"
        self.assertEqual(validate_document(doc)["assessment"], "INVALIDATED")

    def test_hypothetical_cannot_be_source_fact(self):
        doc = fixture("finance")
        doc["source_facts"][0]["fact_kind"] = "hypothetical"
        with self.assertRaises(ValidationError):
            validate_document(doc)

    def test_current_fence_cannot_hide_expected_token_mismatch(self):
        doc = fixture("finance")
        doc["source_facts"][0]["fence"]["expected_token"] = "sha256:not-the-current-profile"
        with self.assertRaises(ValidationError):
            validate_document(doc)

    def test_edge_cannot_self_support_its_conclusion(self):
        doc = fixture("finance")
        doc["justification_edges"][0]["premises"].append("finance-outcome")
        with self.assertRaises(ValidationError):
            validate_document(doc)

    def test_branch_blocker_cannot_be_promoted_without_necessity(self):
        doc = fixture("harness")
        doc["assessment"]["target_blocking_node_ids"] = ["deepseek-branch"]
        with self.assertRaises(ValidationError):
            validate_document(doc)

    def test_conflict_is_preserved(self):
        doc = fixture("finance")
        doc["source_facts"][1]["fence"]["currentness"] = "CONFLICTED"
        with self.assertRaises(ValidationError):
            validate_document(doc)
        doc["assessment"]["status"] = "CONFLICTED"
        self.assertEqual(validate_document(doc)["assessment"], "CONFLICTED")


class CounterfactualRepairTests(unittest.TestCase):
    def test_minimal_positive_repair(self):
        result = validate_document(minimal_repair())
        self.assertEqual(result["assessment"], "EXPLAINED")
        self.assertIn("SUFFICIENT_AT_POSTSTATE", render_concise(minimal_repair()))

    def test_target_revision_requires_continuity(self):
        doc = minimal_repair()
        doc["target_use"]["id"] = "finance:weaker-target"
        with self.assertRaises(ValidationError):
            validate_document(doc)
        doc["target_continuity"] = {"ref": "target-equivalence:1", "fence": fence("target:1")}
        self.assertEqual(validate_document(doc)["assessment"], "EXPLAINED")

    def test_counterfactual_effect_must_stay_hypothetical(self):
        doc = minimal_repair()
        doc["counterfactual_effects"][0]["effect_kind"] = "actual"
        with self.assertRaises(ValidationError):
            validate_document(doc)

    def test_restoration_claim_requires_target_postcondition_witness(self):
        doc = minimal_repair()
        doc["repair_claims"][0]["witness_refs"] = []
        with self.assertRaises(ValidationError):
            validate_document(doc)

    def test_sufficiency_requires_E_and_D_closure(self):
        for missing in ("E", "D"):
            doc = minimal_repair()
            del doc["closure_witnesses"][missing]
            with self.subTest(missing=missing):
                with self.assertRaises(ValidationError):
                    validate_document(doc)

    def test_robust_requires_C_closure(self):
        doc = minimal_repair()
        doc["repair_claims"][0]["kind"] = "ROBUST_OVER_CONTINUATION_UNDER_EFFECT_CONTRACT"
        with self.assertRaises(ValidationError):
            validate_document(doc)
        doc["closure_witnesses"]["C"] = {"ref": "closure:C", "fence": fence("closure:C:1")}
        self.assertEqual(validate_document(doc)["assessment"], "EXPLAINED")

    def test_minimality_requires_I_and_order(self):
        doc = minimal_repair()
        doc["repair_claims"][0] = {
            "kind": "MINIMAL_RELATIVE_TO_ORDER",
            "effect_refs": ["effect:restored"],
            "witness_refs": [],
            "scope": "poststate",
        }
        with self.assertRaises(ValidationError):
            validate_document(doc)
        doc["closure_witnesses"]["I"] = {"ref": "closure:I", "fence": fence("closure:I:1")}
        doc["repair_claims"][0]["order_ref"] = "repair-order:subset"
        self.assertEqual(validate_document(doc)["assessment"], "EXPLAINED")

    def test_multi_action_requires_joint_effect_contract(self):
        doc = minimal_repair()
        doc["intervention_plan"]["action_refs"].append("workstation:action:start-listener")
        with self.assertRaises(ValidationError):
            validate_document(doc)
        doc["intervention_plan"]["joint_effect_contract_ref"] = "workstation:joint-effect:recover+start"
        self.assertEqual(validate_document(doc)["assessment"], "EXPLAINED")

    def test_stale_plan_invalidates_current_repair(self):
        doc = minimal_repair()
        doc["intervention_plan"]["fence"]["currentness"] = "STALE"
        with self.assertRaises(ValidationError):
            validate_document(doc)
        doc["assessment"]["status"] = "INVALIDATED"
        self.assertEqual(validate_document(doc)["assessment"], "INVALIDATED")

    def test_future_execution_gate_requires_revalidation_and_precondition_fence(self):
        doc = minimal_repair()
        doc["execution_gate"] = {"authority_ref": "harness:action-admission"}
        with self.assertRaises(ValidationError):
            validate_document(doc)
        doc["execution_gate"] = {
            "authority_ref": "harness:action-admission",
            "revalidation_ref": "revalidate:before-exec",
            "precondition_fence_ref": "runtime:revision-guard",
        }
        self.assertEqual(validate_document(doc)["assessment"], "EXPLAINED")

    def test_unknown_currentness_cannot_be_explained(self):
        doc = minimal_repair()
        doc["counterfactual_effects"][0]["fence"]["currentness"] = "UNKNOWN"
        with self.assertRaises(ValidationError):
            validate_document(doc)
        doc["assessment"]["status"] = "INCOMPLETE"
        self.assertEqual(validate_document(doc)["assessment"], "INCOMPLETE")


if __name__ == "__main__":
    unittest.main()
