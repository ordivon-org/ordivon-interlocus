# Capability Explanation Validator v0 — reference prototype

Status: **research/reference prototype only**. This directory is not a production API, registry, owner-discovery service, repair planner, or semantic truth source.

The prototype materializes two previously dogfooded Interlocus engineering contracts as a deliberately small pure validator/projector:

1. `capability_path_explanation_v0` — explains why one exact `TargetUse` reaches a cited owner-native consumer outcome through source-fenced warrant edges;
2. `counterfactual_repair_explanation_v0` — validates model-relative repair claims over an exact baseline explanation without promoting hypothetical effects to actual facts.

## Non-authority boundary

All semantic facts, standings, intervention effects, currentness and relation semantics are **caller supplied** and remain owned by their cited owners/contracts. The validator only checks structural warrant discipline. It performs no network calls, owner lookups, persistence, execution, credentials, recommendation, or standing normalization.

The core rule is:

> **No witness → no cross-role conclusion.**

The validator therefore fails closed when a document attempts, among other things, to:

- use a cross-role edge without an exact `relation_contract_ref` and currentness fence;
- treat a stale source/plan/effect as current;
- represent a counterfactual effect as an actual `SourceFact`;
- change the target and call the result a repair without target-continuity evidence;
- promote a branch-local failure to target blocking without a necessity witness;
- claim post-state sufficiency without intervention-effect (`E`) and dependency/currentness (`D`) closure;
- claim continuation robustness without `C` closure;
- claim minimality/necessity without an explicit intervention universe/order (`I` closure);
- compose multiple interventions without a joint effect/composition contract;
- attach future execution admission without revalidation and a precondition fence.

## Usage

```bash
python3 validator.py fixtures/finance.json
python3 -m unittest -v test_validator.py
```

The CLI output is intentionally concise. It is a display projection over a validated document, not a replacement for source evidence.

## Positive fixtures

- `fixtures/finance.json` — configured Workstation identity + degraded/UNKNOWN current capability + Finance `EGRESS_NOT_CURRENT`;
- `fixtures/research.json` — Host `READY` continuity remains true while the historical action route is not current;
- `fixtures/harness.json` — a rejected provider branch coexists with a target satisfied through another admitted route, preserving `BranchFailure != TargetFailure`.

## Scope limit

A successful validation means only that the supplied explanation is structurally admissible relative to its cited source/currentness/effect contracts. It does **not** prove that those external models are correct in reality, that an action is permitted/safe/preferred, or that an executed repair actually restored the target. Actual restoration still requires fresh post-action observation and standing revalidation.
