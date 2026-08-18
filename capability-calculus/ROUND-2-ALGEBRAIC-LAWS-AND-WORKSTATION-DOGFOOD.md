# Network Capability Calculus — Round 2
## Algebraic Laws and Workstation Dogfood

Status: COMPLETE / CAPABILITY ALGEBRA v0 SURVIVES

## 1. Associativity tournament

### Candidate

`(K1 ⊗ K2) ⊗ K3 = K1 ⊗ (K2 ⊗ K3)`.

### Destructive cases

1. **Consumable resource:** K1 supplies one consumable relational resource; K2 and K3 can each consume it. Early grouping may allocate the resource differently.
2. **Early hiding:** K1⊗K2 hides a shared dependency before K3 evaluates an independence guarantee.
3. **Branch selection:** grouping can cause an active/controller branch choice before the alternative is exposed to K3.
4. **Contract migration:** a version migration inserted between the first and second composition changes which clauses/witnesses exist.

### Verdict

Unconditional associativity FAILS.

A conditional theorem survives: if both parenthesizations are merely factorizations of the same global witnessed wiring graph with identical usage/dependency/provenance accounting and no moved H event, they are contextually equivalent.

`WiringAssociativityIsConditional`.

## 2. Identity tournament

A universal empty contract cannot be both the unit of open parallel composition and a serial capability-preserving identity without extra structure.

The survivor is operator-relative identity:

- empty/open boundary for disjoint composition;
- transparent `Id_B` wiring for serial boundary transport.

`Id_B` preserves clause semantics/lineage and does not assert a capability itself.

`IdentityIsOperatorRelative`.

`IdentityWiring != CapabilityProducer`.

## 3. Hiding tournament

### Counterexample

Two externally exposed providers appear independent. After composition an internal shared anchor is hidden. If hiding deletes the dependency edge, a false independence guarantee can be derived.

### Verdict

Hiding is exposure control only. It must retain dependency/provenance/usage/version/currentness information needed by later judgements.

`Hide != Forget`.

`Encapsulation != DependencyErasure`.

## 4. Refinement precongruence tournament

### Candidate

`K' ⊑prov K => C[K'] ⊑prov C[K]` for all C.

### Counterexamples

- C requires exact identity of the original provider;
- K' is functionally stronger but introduces a shared dependency that breaks C's independence claim;
- K' changes usage from reusable to exclusive/consumable;
- K' has stronger guarantees only under a changed version/imported predicate not accepted by C.

### Verdict

Universal precongruence FAILS.

Provider refinement is a precongruence only in provider-monotone contexts with explicit side conditions.

`RefinementPrecongruenceIsContextQualified`.

## 5. Choice tournament

### Counterexample

Two branches exist. Does that mean:

- the controller can select either?
- one will eventually become available?
- they fail independently?
- a race will succeed if either is healthy?

No.

### Result

Choice must include branch family, selection authority/mechanism, quantifier semantics, dependency/correlation information and resolution timing/history.

New anti-laws:

- `Branching != Selectability`;
- `SelectableChoice != IndependentChoice`;
- `ChoiceCardinality != AvailabilityGuarantee`;
- `RaceWinner != StablePreferredProvider`.

## 6. Temporal/continuity transformations

Pure K-to-K rewriting is insufficient because the same contract syntax can evolve differently under different events.

Examples:

- Harness selection narrows `any-provider(P)` to exact-instance/session continuity;
- allowed rebinding preserves broad equivalence-class continuity but may violate exact continuity;
- wait reduces deadline residual or freshness standing;
- expiration terminates a requirement without satisfying it;
- exact-path recovery can preserve identity while admission/health remains red;
- generation/path change invalidates exact identity even if stable authority naming remains unchanged.

### Result

Contract transformations are H-indexed and J-validated:

`K --[h,w]--> K'`.

Laws:

- `ContinuityTransformationRequiresHistory`;
- `TemporalResidualDependsOnHistory`;
- `Expiration != Satisfaction`;
- `FuturePossibility != CurrentServiceability`.

## 7. Finite normal-form tournament

A global unique normal form fails because valid wiring, entailment witnesses and unresolved branch semantics may differ.

A useful relative normal form survives for finite acyclic contracts under fixed wiring/witnesses:

`BRNF=<external negatives, external positives, usage residual, dependency/provenance closure, version lineage, witness ledger>`.

`NormalFormIsWiringAndWitnessRelative`.

## 8. Recursive fragment tournament

Round 1 correctly rejected universal recursive decidability. Round 2 identifies a candidate bounded fragment: finite named guarded recursion, bounded/no-higher-order contract generation, explicit H-progress guards, finite/decidable modality domains and imported implication oracles, plus no implicit unbounded duplication of consumable capabilities.

Structural checks can be decidable relative to those oracles; semantic capability standing remains J-level.

`DecidableFragment != UniversalDecidability`.

This is a research candidate for later implementation/theorem work, not a frozen completeness claim.

## 9. Workstation fault-tolerant pool dogfood

Historical implementation evidence at commit `66b2889` exposes an unusually clean real contract:

Stable authority contains:

- stable profile identity;
- `proxy=http://127.0.0.1:19083`;
- members `finance-okx-a`, `finance-okx-b`;
- explicit allowed TCP ports;
- `selectionPolicy=sticky-active-with-hedged-racing-on-admission`;
- fail-closed when no eligible member exists.

The authority digest intentionally does not bind current member generation. A separate lease projection binds active member and member generation/lease information. Tests explicitly verify that changing active member changes lease digest while stable profile authority digest does not change.

### Algebra mapping

- public/stable profile is a K boundary identity;
- configured members form structural alternatives, not guaranteed live choices;
- member eligibility/current health is Π/J standing;
- sticky active, hedged race and failover are H selection histories;
- active-member change is an H event that changes lease/currentness without changing stable K identity;
- member generation/lease is hidden from stable consumer identity but retained in provenance/currentness, satisfying `Hide != Forget`.

### Current read-only observation

At the Round-2 observation time on 2026-08-18, `finance-okx` reports:

- `status=UNKNOWN`;
- `memberCount=2`;
- `eligibleMembers=[]`;
- `activeMember=null`;
- `listenerReachable=false`;
- `serviceActive=false`;
- watchdog disposition `no-eligible-member`.

No Workstation mutation was performed.

This is a direct real-system falsifier for any algebra equating branch count with availability or selectability.

### New durable separation

`StableBoundaryIdentity != CurrentLeaseStanding`.

The same stable K can support different H/Π/J lease realizations over time.

## 10. Round-2 verdict

Capability Algebra v0 survives, but as a **typed partial algebra with explicit side conditions**, not a universal monoid/lattice/semiring.

Surviving laws:

1. `WiringAssociativityIsConditional`;
2. `IdentityIsOperatorRelative`;
3. `IdentityWiring != CapabilityProducer`;
4. `Hide != Forget`;
5. `Encapsulation != DependencyErasure`;
6. `RefinementPrecongruenceIsContextQualified`;
7. `Branching != Selectability`;
8. `SelectableChoice != IndependentChoice`;
9. `ChoiceCardinality != AvailabilityGuarantee`;
10. `RaceWinner != StablePreferredProvider`;
11. `ContinuityTransformationRequiresHistory`;
12. `TemporalResidualDependsOnHistory`;
13. `Expiration != Satisfaction`;
14. `FuturePossibility != CurrentServiceability`;
15. `NormalFormIsWiringAndWitnessRelative`;
16. `DecidableFragment != UniversalDecidability`;
17. `StableBoundaryIdentity != CurrentLeaseStanding`.

No NCT v1 reopen condition fires. No NDF Foundation reopen condition fires. NDF6 remains NOT ADMITTED.

## 11. Round-3 frontier

The next information-dense step is a closure/theorem round rather than more syntax:

- formalize contextual equivalence `≃_Γ` and observation boundary;
- prove/falsify the conditional associativity theorem on the finite acyclic fragment;
- formalize provider-monotone contexts and a refinement precongruence theorem;
- formalize BRNF construction and prove semantic preservation relative to fixed W/witness ledger;
- instantiate the choice algebra for sticky/race/failover and DTN/Agent selection cases;
- test GFRCF bounded unfolding and guarded-cycle rejection;
- decide FREEZE / REPAIR / REJECT for Network Capability Calculus v1.
