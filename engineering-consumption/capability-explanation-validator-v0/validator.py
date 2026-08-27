#!/usr/bin/env python3
"""Reference validator/projector for Interlocus explanation contracts v0.

This module is intentionally non-authoritative. It validates caller-supplied,
source-fenced explanation documents. It performs no owner discovery, I/O beyond
reading a supplied JSON file in CLI mode, persistence, execution, or repair
selection.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


class ValidationError(ValueError):
    pass


CURRENTNESS = {"CURRENT", "STALE", "UNKNOWN", "CONFLICTED"}
ASSESSMENT = {"EXPLAINED", "INCOMPLETE", "CONFLICTED", "INVALIDATED"}
REPAIR_CLAIMS = {
    "MAY_RESTORE_UNDER_EFFECT_CONTRACT",
    "SUFFICIENT_AT_POSTSTATE_UNDER_EFFECT_CONTRACT",
    "ROBUST_OVER_CONTINUATION_UNDER_EFFECT_CONTRACT",
    "REQUIRED_CONDITION_CHANGE",
    "NECESSARY_INTERVENTION_RELATIVE_TO_UNIVERSE",
    "MINIMAL_RELATIVE_TO_ORDER",
}


def _fail(message: str) -> None:
    raise ValidationError(message)


def _dict(value: Any, where: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        _fail(f"{where} must be an object")
    return value


def _list(value: Any, where: str) -> list[Any]:
    if not isinstance(value, list):
        _fail(f"{where} must be an array")
    return value


def _str(value: Any, where: str) -> str:
    if not isinstance(value, str) or not value:
        _fail(f"{where} must be a non-empty string")
    return value


def _strict_keys(obj: dict[str, Any], allowed: set[str], where: str) -> None:
    extra = set(obj) - allowed
    if extra:
        _fail(f"{where} contains unsupported fields: {sorted(extra)}")


def _fence(value: Any, where: str) -> str:
    obj = _dict(value, where)
    _strict_keys(obj, {"token", "expected_token", "currentness"}, where)
    token = _str(obj.get("token"), f"{where}.token")
    currentness = _str(obj.get("currentness"), f"{where}.currentness")
    if currentness not in CURRENTNESS:
        _fail(f"{where}.currentness must be one of {sorted(CURRENTNESS)}")
    if "expected_token" in obj:
        expected = _str(obj["expected_token"], f"{where}.expected_token")
        if currentness == "CURRENT" and token != expected:
            _fail(f"{where} claims CURRENT but token does not match expected_token")
    return currentness


def _target_use(value: Any, where: str) -> dict[str, Any]:
    obj = _dict(value, where)
    _strict_keys(
        obj,
        {"id", "contract_ref", "scope", "snapshot", "spans_intervention_horizon"},
        where,
    )
    for field in ("id", "contract_ref", "scope", "snapshot"):
        _str(obj.get(field), f"{where}.{field}")
    if "spans_intervention_horizon" in obj and not isinstance(
        obj["spans_intervention_horizon"], bool
    ):
        _fail(f"{where}.spans_intervention_horizon must be boolean")
    return obj


def validate_capability_path(doc: dict[str, Any]) -> dict[str, Any]:
    _strict_keys(
        doc,
        {"kind", "target_use", "source_facts", "justification_edges", "assessment"},
        "document",
    )
    if doc.get("kind") != "capability_path_explanation_v0":
        _fail("kind must be capability_path_explanation_v0")
    target = _target_use(doc.get("target_use"), "target_use")

    facts = _list(doc.get("source_facts"), "source_facts")
    fact_by_id: dict[str, dict[str, Any]] = {}
    source_currentness: list[str] = []
    for index, raw in enumerate(facts):
        where = f"source_facts[{index}]"
        fact = _dict(raw, where)
        _strict_keys(
            fact,
            {
                "id",
                "owner_ref",
                "source_ref",
                "fact_kind",
                "fence",
                "native",
                "display_summary",
            },
            where,
        )
        fid = _str(fact.get("id"), f"{where}.id")
        if fid in fact_by_id:
            _fail(f"duplicate source fact id: {fid}")
        _str(fact.get("owner_ref"), f"{where}.owner_ref")
        _str(fact.get("source_ref"), f"{where}.source_ref")
        if fact.get("fact_kind") != "actual":
            _fail(f"{where}.fact_kind must be actual; hypothetical effects are not facts")
        source_currentness.append(_fence(fact.get("fence"), f"{where}.fence"))
        native = _dict(fact.get("native"), f"{where}.native")
        if "label" not in native:
            _fail(f"{where}.native.label is required")
        _str(native["label"], f"{where}.native.label")
        if "display_summary" in fact and not isinstance(fact["display_summary"], str):
            _fail(f"{where}.display_summary must be a string")
        fact_by_id[fid] = fact

    edges = _list(doc.get("justification_edges"), "justification_edges")
    known_nodes = set(fact_by_id)
    edge_ids: set[str] = set()
    relation_currentness: list[str] = []
    target_blocker_witnessed: set[str] = set()
    for index, raw in enumerate(edges):
        where = f"justification_edges[{index}]"
        edge = _dict(raw, where)
        _strict_keys(
            edge,
            {
                "id",
                "premises",
                "conclusion",
                "relation_contract_ref",
                "relation_fence",
                "role",
                "supports_target_blocker_nodes",
                "necessity_witness_ref",
            },
            where,
        )
        eid = _str(edge.get("id"), f"{where}.id")
        if eid in known_nodes or eid in edge_ids:
            _fail(f"duplicate explanation node id: {eid}")
        premises = _list(edge.get("premises"), f"{where}.premises")
        if not premises:
            _fail(f"{where}.premises must not be empty")
        for premise in premises:
            pid = _str(premise, f"{where}.premises[]")
            if pid not in known_nodes and pid not in edge_ids:
                _fail(f"{where} premise {pid!r} is not a prior fact/edge; explanation must be well-founded")
        conclusion = _str(edge.get("conclusion"), f"{where}.conclusion")
        if conclusion not in fact_by_id:
            _fail(f"{where}.conclusion must name an actual source fact")
        if conclusion in premises:
            _fail(f"{where} may not use its own conclusion as a premise")
        _str(edge.get("relation_contract_ref"), f"{where}.relation_contract_ref")
        relation_currentness.append(
            _fence(edge.get("relation_fence"), f"{where}.relation_fence")
        )
        _str(edge.get("role"), f"{where}.role")
        promoted = edge.get("supports_target_blocker_nodes", [])
        promoted = _list(promoted, f"{where}.supports_target_blocker_nodes")
        if promoted:
            witness = _str(edge.get("necessity_witness_ref"), f"{where}.necessity_witness_ref")
            if not witness:
                _fail(f"{where} target-blocker promotion requires necessity witness")
            for node in promoted:
                node_id = _str(node, f"{where}.supports_target_blocker_nodes[]")
                if node_id not in fact_by_id:
                    _fail(f"{where} target blocker {node_id!r} is not a source fact")
                target_blocker_witnessed.add(node_id)
        elif "necessity_witness_ref" in edge:
            _str(edge["necessity_witness_ref"], f"{where}.necessity_witness_ref")
        edge_ids.add(eid)

    assessment = _dict(doc.get("assessment"), "assessment")
    _strict_keys(
        assessment,
        {
            "status",
            "target_outcome_node_id",
            "observed_blocking_node_ids",
            "target_blocking_node_ids",
            "revalidation_node_ids",
        },
        "assessment",
    )
    status = _str(assessment.get("status"), "assessment.status")
    if status not in ASSESSMENT:
        _fail(f"assessment.status must be one of {sorted(ASSESSMENT)}")
    outcome = _str(assessment.get("target_outcome_node_id"), "assessment.target_outcome_node_id")
    if outcome not in fact_by_id:
        _fail("assessment.target_outcome_node_id must reference a source fact")
    for field in ("observed_blocking_node_ids", "target_blocking_node_ids", "revalidation_node_ids"):
        values = _list(assessment.get(field, []), f"assessment.{field}")
        for value in values:
            node = _str(value, f"assessment.{field}[]")
            if node not in fact_by_id:
                _fail(f"assessment.{field} references unknown fact {node!r}")
    for node in assessment.get("target_blocking_node_ids", []):
        if node not in target_blocker_witnessed:
            _fail(f"target-level blocker {node!r} lacks a necessity witness")

    all_currentness = source_currentness + relation_currentness
    if "STALE" in all_currentness and status != "INVALIDATED":
        _fail("stale source/relation fence requires INVALIDATED assessment")
    if "CONFLICTED" in all_currentness and status not in {"CONFLICTED", "INVALIDATED"}:
        _fail("conflicted source/relation fence must be preserved")
    if "UNKNOWN" in all_currentness and status == "EXPLAINED":
        _fail("EXPLAINED cannot depend on UNKNOWN currentness")

    return {
        "kind": doc["kind"],
        "target": target["id"],
        "assessment": status,
        "outcome_node": outcome,
        "observed_blockers": list(assessment.get("observed_blocking_node_ids", [])),
        "target_blockers": list(assessment.get("target_blocking_node_ids", [])),
    }


def _closure_map(value: Any) -> dict[str, dict[str, Any]]:
    obj = _dict(value, "closure_witnesses")
    _strict_keys(obj, {"R", "E", "D", "C", "I"}, "closure_witnesses")
    result: dict[str, dict[str, Any]] = {}
    for key, raw in obj.items():
        witness = _dict(raw, f"closure_witnesses.{key}")
        _strict_keys(witness, {"ref", "fence"}, f"closure_witnesses.{key}")
        _str(witness.get("ref"), f"closure_witnesses.{key}.ref")
        _fence(witness.get("fence"), f"closure_witnesses.{key}.fence")
        result[key] = witness
    return result


def validate_counterfactual_repair(doc: dict[str, Any]) -> dict[str, Any]:
    _strict_keys(
        doc,
        {
            "kind",
            "baseline_explanation_ref",
            "target_use",
            "target_continuity",
            "intervention_plan",
            "counterfactual_effects",
            "closure_witnesses",
            "repair_claims",
            "assessment",
            "execution_gate",
        },
        "document",
    )
    if doc.get("kind") != "counterfactual_repair_explanation_v0":
        _fail("kind must be counterfactual_repair_explanation_v0")

    baseline = _dict(doc.get("baseline_explanation_ref"), "baseline_explanation_ref")
    _strict_keys(baseline, {"source_ref", "target_use_ref", "fence"}, "baseline_explanation_ref")
    _str(baseline.get("source_ref"), "baseline_explanation_ref.source_ref")
    baseline_target = _str(baseline.get("target_use_ref"), "baseline_explanation_ref.target_use_ref")
    currentness = [_fence(baseline.get("fence"), "baseline_explanation_ref.fence")]

    target = _target_use(doc.get("target_use"), "target_use")
    if target["id"] != baseline_target:
        continuity = _dict(doc.get("target_continuity"), "target_continuity")
        _strict_keys(continuity, {"ref", "fence"}, "target_continuity")
        _str(continuity.get("ref"), "target_continuity.ref")
        currentness.append(_fence(continuity.get("fence"), "target_continuity.fence"))
    elif "target_continuity" in doc:
        continuity = _dict(doc["target_continuity"], "target_continuity")
        _strict_keys(continuity, {"ref", "fence"}, "target_continuity")
        _str(continuity.get("ref"), "target_continuity.ref")
        currentness.append(_fence(continuity.get("fence"), "target_continuity.fence"))

    plan = _dict(doc.get("intervention_plan"), "intervention_plan")
    _strict_keys(
        plan,
        {"id", "owner_ref", "plan_ref", "fence", "action_refs", "joint_effect_contract_ref"},
        "intervention_plan",
    )
    for field in ("id", "owner_ref", "plan_ref"):
        _str(plan.get(field), f"intervention_plan.{field}")
    currentness.append(_fence(plan.get("fence"), "intervention_plan.fence"))
    actions = _list(plan.get("action_refs"), "intervention_plan.action_refs")
    if not actions:
        _fail("intervention_plan.action_refs must not be empty")
    for action in actions:
        _str(action, "intervention_plan.action_refs[]")
    if len(actions) > 1:
        _str(plan.get("joint_effect_contract_ref"), "intervention_plan.joint_effect_contract_ref")

    effects = _list(doc.get("counterfactual_effects"), "counterfactual_effects")
    effect_ids: set[str] = set()
    for index, raw in enumerate(effects):
        where = f"counterfactual_effects[{index}]"
        effect = _dict(raw, where)
        _strict_keys(
            effect,
            {"id", "effect_kind", "effect_contract_ref", "fence", "outcome_scope", "postcondition_witness_refs"},
            where,
        )
        eid = _str(effect.get("id"), f"{where}.id")
        if eid in effect_ids:
            _fail(f"duplicate counterfactual effect id: {eid}")
        if effect.get("effect_kind") != "hypothetical":
            _fail(f"{where}.effect_kind must be hypothetical; counterfactual effects are not actual facts")
        _str(effect.get("effect_contract_ref"), f"{where}.effect_contract_ref")
        currentness.append(_fence(effect.get("fence"), f"{where}.fence"))
        _str(effect.get("outcome_scope"), f"{where}.outcome_scope")
        witnesses = _list(effect.get("postcondition_witness_refs", []), f"{where}.postcondition_witness_refs")
        for witness in witnesses:
            _str(witness, f"{where}.postcondition_witness_refs[]")
        effect_ids.add(eid)

    closures = _closure_map(doc.get("closure_witnesses", {}))
    for key, witness in closures.items():
        currentness.append(_dict(witness["fence"], f"closure_witnesses.{key}.fence")["currentness"])

    claims = _list(doc.get("repair_claims"), "repair_claims")
    claim_kinds: list[str] = []
    for index, raw in enumerate(claims):
        where = f"repair_claims[{index}]"
        claim = _dict(raw, where)
        _strict_keys(
            claim,
            {"kind", "effect_refs", "witness_refs", "scope", "model_relative", "order_ref"},
            where,
        )
        kind = _str(claim.get("kind"), f"{where}.kind")
        if kind not in REPAIR_CLAIMS:
            _fail(f"{where}.kind is not an allowed repair claim")
        claim_kinds.append(kind)
        _str(claim.get("scope"), f"{where}.scope")
        effect_refs = _list(claim.get("effect_refs", []), f"{where}.effect_refs")
        for ref in effect_refs:
            rid = _str(ref, f"{where}.effect_refs[]")
            if rid not in effect_ids:
                _fail(f"{where} references unknown counterfactual effect {rid!r}")
        witness_refs = _list(claim.get("witness_refs", []), f"{where}.witness_refs")
        for ref in witness_refs:
            _str(ref, f"{where}.witness_refs[]")

        if kind in {
            "MAY_RESTORE_UNDER_EFFECT_CONTRACT",
            "SUFFICIENT_AT_POSTSTATE_UNDER_EFFECT_CONTRACT",
            "ROBUST_OVER_CONTINUATION_UNDER_EFFECT_CONTRACT",
        }:
            if claim.get("model_relative") is not True:
                _fail(f"{where} must state model_relative=true")
            if not effect_refs:
                _fail(f"{where} requires at least one counterfactual effect")
            if not witness_refs:
                _fail(f"{where} requires a target/postcondition witness")
        if kind == "SUFFICIENT_AT_POSTSTATE_UNDER_EFFECT_CONTRACT":
            if not {"E", "D"}.issubset(closures):
                _fail(f"{where} requires E and D closure")
        if kind == "ROBUST_OVER_CONTINUATION_UNDER_EFFECT_CONTRACT":
            if not {"E", "D", "C"}.issubset(closures):
                _fail(f"{where} requires E, D, and C closure")
        if kind == "REQUIRED_CONDITION_CHANGE" and "R" not in closures:
            _fail(f"{where} requires R closure")
        if kind == "NECESSARY_INTERVENTION_RELATIVE_TO_UNIVERSE":
            if not {"R", "I"}.issubset(closures):
                _fail(f"{where} requires R and I closure")
        if kind == "MINIMAL_RELATIVE_TO_ORDER":
            if not {"E", "D", "I"}.issubset(closures):
                _fail(f"{where} requires E, D, and I closure")
            _str(claim.get("order_ref"), f"{where}.order_ref")

    assessment = _dict(doc.get("assessment"), "assessment")
    _strict_keys(assessment, {"status"}, "assessment")
    status = _str(assessment.get("status"), "assessment.status")
    if status not in ASSESSMENT:
        _fail(f"assessment.status must be one of {sorted(ASSESSMENT)}")

    if "execution_gate" in doc:
        gate = _dict(doc["execution_gate"], "execution_gate")
        _strict_keys(
            gate,
            {"authority_ref", "revalidation_ref", "precondition_fence_ref"},
            "execution_gate",
        )
        for field in ("authority_ref", "revalidation_ref", "precondition_fence_ref"):
            _str(gate.get(field), f"execution_gate.{field}")

    if "STALE" in currentness and status != "INVALIDATED":
        _fail("stale counterfactual source/plan/effect/closure requires INVALIDATED assessment")
    if "CONFLICTED" in currentness and status not in {"CONFLICTED", "INVALIDATED"}:
        _fail("conflicted counterfactual inputs must be preserved")
    if "UNKNOWN" in currentness and status == "EXPLAINED":
        _fail("EXPLAINED repair cannot depend on UNKNOWN currentness")

    return {
        "kind": doc["kind"],
        "target": target["id"],
        "assessment": status,
        "plan": plan["id"],
        "claims": claim_kinds,
    }


def validate_document(doc: Any) -> dict[str, Any]:
    obj = _dict(doc, "document")
    kind = obj.get("kind")
    if kind == "capability_path_explanation_v0":
        return validate_capability_path(obj)
    if kind == "counterfactual_repair_explanation_v0":
        return validate_counterfactual_repair(obj)
    _fail("unsupported document kind")


def render_concise(doc: dict[str, Any]) -> str:
    result = validate_document(doc)
    lines = [
        f"Target: {result['target']}",
        f"Assessment: {result['assessment']}",
    ]
    if result["kind"] == "capability_path_explanation_v0":
        fact_by_id = {fact["id"]: fact for fact in doc["source_facts"]}
        outcome = fact_by_id[result["outcome_node"]]
        native = outcome["native"]
        lines.append(f"Native outcome: {native['label']}={native.get('value', '<opaque>')}")
        if result["observed_blockers"]:
            lines.append("Observed blockers: " + ", ".join(result["observed_blockers"]))
        if result["target_blockers"]:
            lines.append("Target blockers (proven necessary): " + ", ".join(result["target_blockers"]))
    else:
        lines.append(f"Intervention plan: {result['plan']}")
        if result["claims"]:
            lines.append("Repair claims: " + ", ".join(result["claims"]))
        else:
            lines.append("Repair claims: none")
    return "\n".join(lines)


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: validator.py DOCUMENT.json", file=sys.stderr)
        return 2
    path = Path(argv[1])
    try:
        doc = json.loads(path.read_text(encoding="utf-8"))
        print(render_concise(doc))
    except (OSError, json.JSONDecodeError, ValidationError) as exc:
        print(f"INVALID: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
