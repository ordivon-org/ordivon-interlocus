# Network Capability Calculus — Round 3
## Theorem and Closure Tournament

Status: COMPLETE

Final decision: **FREEZE Network Capability Calculus v1** as a typed partial algebra with explicit observation-, context-, wiring- and witness-relative side conditions.

## A. Contextual equivalence tournament

### Failure of boundary-only equality

Comparing only exposed clause names/types is unsound. Two compositions can expose the same nominal capability while differing in shared dependency, exact-instance continuity, version lineage, usage residual or currentness evidence that a later allowed J judgement can observe.

### Survivor

Define an explicit observation signature:

`Ω_Γ=<BoundaryRoles,JudgementRoles,ProvenanceVisibility,IdentityVisibility,TimeScope,ImportScope>`.

Then:

`K1 ≃_{Γ,Ω} K2`

iff no Ω-admissible external contract context plus compatible Π/H/J continuation can distinguish them on allowed boundary/judgement observations.

This makes abstraction explicit rather than silently declaring internal differences irrelevant.

New laws:

- `ContextualEquivalenceIsObservationRelative`;
- `HiddenInternalDifference != IrrelevantDifference`.

PASS.

## B. Conditional associativity theorem tournament

### Theorem target

For finite acyclic contracts and one fixed global witnessed wiring G, two bracketings should be equivalent when they merely factor G differently.

### Proof sketch

Under the Round-2 side conditions:

1. both bracketings preserve the same discharge edge set;
2. each edge keeps the same valid witness;
3. usage operations commute/converge to the same residual;
4. dependency/provenance closure is accumulated globally rather than hidden early;
5. branch-selection and migration H events are not moved;
6. residualization is confluent;
7. the Ω-exposed boundary summary is equal;

both bracketings reduce to the same Ω-closed BRNF. By BRNF preservation they are contextually equivalent.

### Counterexample defense

Every known Round-2 associativity counterexample violates at least one side condition:

- competing consumption -> nonconfluent usage;
- early dependency hiding -> Ω/dependency closure violation;
- moved branch selection -> H-event movement;
- inserted migration -> version/H mismatch.

### Verdict

THEOREM SURVIVES on the finite acyclic fixed-wiring fragment.

No unconditional theorem is admitted.

## C. Provider refinement precongruence tournament

### Theorem target

`K' ⊑prov K => C[K'] ⊑prov C[K]`.

### Necessary context classification

A provider-monotone context cannot demand/observe distinctions that the refinement relation did not promise to preserve.

Required side conditions include:

- no unpreserved exact-instance/session dependence;
- context usage within K' admitted usage semantics;
- witnessed q/χ/θ implications;
- no Ω-visible dependency/provenance claim broken by K';
- version/import compatibility;
- intensional implementation identity observed only through admitted abstraction.

### Proof sketch

Each negative clause presented by C to the hole that K could discharge remains dischargeable by K' through the provider-refinement witnesses. Every externally visible positive clause/guarantee of C[K] is preserved or strengthened under the same Ω. Dependency/provenance and usage side conditions prevent the known nonmonotone counterexamples.

### Verdict

QUALIFIED PRECONGRUENCE SURVIVES on provider-monotone finite witnessed-wiring contexts.

Universal context precongruence remains rejected.

## D. BRNF preservation tournament

### Failure mode

A normal form that retains only external positive/negative clauses can erase exactly the facts needed later for independence, currentness, continuity or version judgements.

### Repair

BRNF is parameterized by Ω and contains:

- external negative/positive clauses;
- usage residual;
- dependency/provenance closure;
- version lineage;
- hidden discharge/abstraction witness ledger.

### Preservation argument

For fixed W/witnesses on a finite acyclic graph, BRNF removes only internal presentation structure. All Ω-visible boundary facts and all summaries needed by Ω-authorized J judgements remain. Therefore replacing K with BRNF cannot change an Ω-observable judgement under compatible continuations.

### New laws

`NormalizationRequiresObservationClosure`.

`ObservationExpansionMayInvalidateNormalization`.

### Verdict

BRNF PRESERVATION SURVIVES relative to fixed W/witnesses and Ω.

Global unique normalization remains rejected.

## E. Choice instantiation tournament

### Workstation sticky-active / hedged race / failover

Historical Workstation pool semantics provide:

- stable configured branch set;
- a sticky active member;
- eligibility gating;
- hedged race on admission;
- failover history;
- separate stable authority vs dynamic lease.

Current read-only observation has two configured members and zero eligible members. Therefore branch count cannot imply availability/selectability.

The choice tuple cleanly separates B/s/q/δ/ρ.

### DTN

Future contacts are branches/opportunities but selection may be environment/schedule-driven, and eventual possibility is not current controller-selectability or current serviceability.

### Harness provider selection

Discovered candidates form B, but selector ownership is Harness. The selection event is imported through H and may strengthen Network continuity. Network cannot infer selection merely from candidate existence.

### New laws

`ChoiceResolution != BranchExistence`.

`ChoiceSemanticsRequiresSelectorOwnership`.

### Verdict

CHOICE ALGEBRA SURVIVES without a generic OR/choice collapse.

## F. Guarded recursion tournament

### Attack on Round-2 GFRCF

A syntactic guard label on every cycle is insufficient. A cycle can remain completely self-supporting while every edge is marked 'after progress' if no progress/source fact is independently grounded.

Therefore Round-2 GFRCF requires a repair.

### Repaired fragment: G-GFRCF

Every recursive strongly connected component must possess a grounding certificate:

- external/base support edge; or
- establishment/progress rule with a justified well-founded/progress witness; or
- imported fixed-point semantics with explicit admissibility conditions.

Bounded unfolding can check structure and reject obvious unsupported SCCs, but cannot itself prove live capability standing.

New laws:

`GuardedSyntax != GroundedRecursion`.

`BoundedUnfolding != CapabilityProof`.

### Verdict

ROUND-2 RECURSIVE FRAGMENT REPAIRED; v1 SURVIVES.

`ContractCycle != CapabilityWitness` remains intact.

## G. Workstation closure dogfood

The real scoped-egress pool remains a strong downstream witness for the final calculus:

- stable profile authority behaves like stable K identity;
- active member and lease generation belong to H/Π/J current realization;
- two configured branches can produce zero currently eligible choices;
- sticky/race/failover selector policy must remain explicit;
- hiding member generation from stable consumer identity is sound only because lease/currentness provenance remains separately available.

Canonical separation retained:

`StableBoundaryIdentity != CurrentLeaseStanding`.

No network mutation was required for this research.

## H. Final closure decision

### FREEZE

Network Capability Calculus v1 is frozen with:

- polarized typed K clauses;
- typed q/u/χ/θ modalities;
- role-relative provider refinement and demand strengthening;
- witnessed discharge;
- global witnessed wiring and residualization;
- Ω-relative contextual equivalence;
- conditional associativity on finite acyclic fixed-wiring fragments;
- operator-relative identities;
- hiding with observation/dependency/provenance closure;
- provider-monotone-context precongruence;
- typed choice object B/s/q/δ/ρ;
- H-indexed temporal/continuity transformations;
- Ω-relative BRNF preservation;
- grounded guarded finite recursive analysis fragment.

### Freeze does not mean

- machine-checked proof;
- universal associativity/precongruence;
- unique global normal form;
- universal recursive decidability;
- replacement for NCT v1/NDF0-NDF5;
- external academic novelty claim;
- implementation mandate.

No NCT v1 or NDF Foundation reopen condition fires. NDF6 remains NOT ADMITTED.
