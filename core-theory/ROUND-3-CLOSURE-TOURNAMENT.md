# Network Core Theory — Round 3 Closure Tournament

Status: COMPLETE

Final decision: **FREEZE Derived Network Core Theory v1**, with one architectural clarification: the core is `<K, Π, H ; J>`, where J is a first-class judgement calculus but not a fourth semantic carrier/state axis.

## A. Π overbreadth attack

### Falsifier sought

If Π means arbitrary representation, any K or H can be serialized into Π and the proposed compression becomes vacuous.

### Repair/admission discipline

An admissible Π must name its source role, query/cut scope, projection relation, view, provenance and adequacy target. Π cannot create contract roles or occurrences by representing them. An information-complete representation of K/H remains a representation and does not acquire their semantic role.

Derived laws:

- ProjectionGrounding;
- ProjectionNonGeneration;
- RepresentationNonSubstitution;
- AdequacyIsQueryRelative;
- ProjectionNonAnnexation.

### Verdict

PASS after discipline tightening. No new axis and no Foundation reopen.

## B. K vs Ordivon Normative boundary attack

Ordivon Normative owns context-relative constitutive/normative admission, consequence and transformation semantics, including normative power and validity/jurisdiction after admission. Network K needs operational Require/Guarantee/Continuity/Residual roles.

The boundary is stable if Network Require means only an operational satisfaction/admissibility criterion selected by a Network capability/service contract. If a case depends on permission, legitimacy, entitlement, jurisdiction or deontic validity, K imports that external predicate; it does not derive it.

Examples:

- `Require TLS endpoint authentication` may import Security semantics;
- `Require provider authorized under policy P` imports Authority/Normative truth;
- `Require delivery before deadline` is an operational Network criterion and needs no normative owner.

### Verdict

PASS. No owner collision. Project-root wording `Capability–Requirement Contract Boundary` is retained.

## C. Recursive composition / hypercontract attack

Hostile pattern:

- capability A is offered only if B is live;
- capability B is offered only if A is live;
- a negotiated meta-contract can rewrite both interfaces.

Naive assumption discharge could self-justify the cycle.

Repair law:

`ContractCycle != CapabilityWitness`.

A recursive contract graph may describe dependencies, but current capability standing requires an external/base support witness, an establishment history, or imported justified fixed-point semantics. Meta-contract negotiation is represented as H changing K->K'; it does not retroactively make the old K true.

### Verdict

PASS. No Hypercontract fourth axis required. Recursive semantics is a typed K/H specialization plus J, not a new Network substance.

## D. Evidence / currentness layer attack

Round 2 already separated semantic capability truth from evidence-supported current claim. Round 3 asks whether currentness can remain implicit.

It cannot.

Engineering evidence distinguishes:

- parent identity current while transient health is red;
- identity current during exact-path recovery backoff while admission fails closed;
- stale admission evidence superseded by newer healthy watchdog evidence;
- profile health changing UNAVAILABLE->AVAILABLE without stable-profile identity change;
- generation/path changes invalidating identity even if public profile naming remains stable.

Therefore currentness must be an explicit typed judgement family.

Minimal repair:

`NCT_v1 = <K,Π,H ; J>`.

J is not a fourth state axis because it does not introduce an independent Network substance. It classifies relations among K/Π/H/E/σ under scope/time.

### Verdict

PASS WITH ARCHITECTURAL CLARIFICATION. J becomes first-class in v1.

## E. Healthy -> degraded -> recovered lineage dogfood

Current read-only Workstation observation from Round 2 found `finance-okx` UNKNOWN/no eligible member and `surf-clash` UNAVAILABLE. Historical engineering lineage contains explicit recovery implementations/tests:

- commit `91d6200`: recover scoped egress across transient parent health;
- commit `8dde4a4`: rebind scoped egress after anchor recovery;
- commit `bfaf4af`: keep scoped egress resident across exact-path recovery.

The executed test corpus includes concrete state transitions where destination health is absent/red -> profile UNAVAILABLE -> current healthy destination evidence -> profile AVAILABLE; where transient parent health is red but parent identity remains current; and where exact-path recovery retains identity while admission fails closed.

This supports a lineage model where K/profile identity may persist, Π/E health/currentness views change, H records recovery/rebinding, and J changes admission/serviceability standing without erasing historical identity.

### Verdict

PASS. Live mutation was neither required nor performed.

## F. Network × Runtime theorem transport

Runtime consolidation states Runtime owns bounded admitted operational commitment, Attempt/realization, execution/effect evidence and reconciliation, while Network owns inter-locus capability/transport phenomena.

Transport theorem candidate:

A Network judgement may discharge a Runtime premise such as `remote service/capability currently admissible`, but cannot discharge Runtime execution/effect/result semantics.

Canonical chain:

`NetworkClaim/Serviceability -> RuntimePremise`

but

`NetworkServiceable != RuntimeOperationAdmitted != RuntimeAttemptSucceeded != ExternalEffectTrue`.

Conversely, a successful Runtime Attempt at t0 does not prove the Network capability remains current at t1.

Runtime Scope Conservation and Evidence/Truth Non-Lifting are consistent with Network's scoped ClaimLive/J currentness.

### Verdict

PASS. The theorem transports across the owner boundary without duplicate ownership.

## G. Network × Harness theorem transport

Harness consolidation states Harness owns Agent/Task/Context, selection, invocation, bounded Run/control mediation and result attribution; Network owns the inter-locus capability/discovery/transport substrate.

Transport chain:

`Network discovery/ClaimMatch`
`-> Harness candidate input`
`-> Harness selection disposition`
`-> Harness invocation`
`-> Runtime admitted operation/attempt`.

None of these arrows is identity.

Canonical anti-law:

`NetworkDiscoveryMatch != HarnessSelected != HarnessInvoked != RuntimeAttempt`.

Harness may change K by selecting a candidate and thereby strengthening continuity from `any provider` to `exact instance/session`, but the selection event is Harness-owned and merely induces a new Network contract boundary through an explicit cross-owner history/bridge.

### Verdict

PASS. Agentic networking does not force planning/control into Network.

## H. Final closure decision

### FREEZE

Derived Network Core Theory v1 is frozen as:

`NCT_v1 = <K, Π, H ; J>_Γ`

where:

- K = Capability–Requirement Contract Boundary;
- Π = grounded, typed, query/cut-relative Network projection family;
- H = admissible realization history family;
- J = typed judgement layer for capability standing, evidence-supported current claim, adequacy, satisfaction/residual, resolution, composition/discharge and currentness.

### What freeze means

- the higher-order compression is stable enough to become the current Derived Network Core Theory;
- NDF0-NDF5 remain the Foundation/provenance substrate and are not renumbered away;
- NDF6 remains NOT ADMITTED;
- future Network research should prefer derived-theory programmes and external/engineering falsification over Foundation-number expansion;
- v1 remains reopenable under explicit Core-Theory Reopen Conditions.

### What freeze does not mean

- exhaustive mathematical completeness;
- whole-domain closure forever;
- external novelty/priority claim;
- permission to annex other owners;
- production refactor mandate.

## I. New durable laws/anti-laws surfaced by the closure tournament

1. `SelectionDependence != TruthDependence`.
2. `ProjectionNonGeneration`.
3. `RepresentationNonSubstitution`.
4. `ProjectionNonAnnexation`.
5. `ContractCycle != CapabilityWitness`.
6. `SemanticCapabilityTruth != EvidenceSupportedCurrentClaim`.
7. `IdentityCurrent != HealthCurrent != AdmissionStanding != Reachable != Serviceable`.
8. `Configured != Live`.
9. `Multiplicity != Independence != Availability`.
10. `NetworkServiceable != RuntimeAdmitted != RuntimeAttemptSucceeded != ExternalEffectTrue`.
11. `NetworkDiscoveryMatch != HarnessSelected != HarnessInvoked != RuntimeAttempt`.

These are derived Network Core laws unless later falsified; they are not new numbered Foundations.
