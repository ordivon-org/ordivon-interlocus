# Ordivon Network Capability Calculus v1

Status: FROZEN DERIVED THEORY at the current evidence frontier

Upstream authority: frozen `NCT_v1=<K,Π,H;J>_Γ`.

This calculus is the K-side derived theory for Network capability/requirement contracts. It is a **typed partial algebra with explicit side conditions**, not an unconditional monoid, lattice, semiring, universal type system, or current-capability database.

## 1. Contract carrier

A contract is:

`K = <kid, C, D, V>`

where:

- `kid` is immutable contract identity;
- `C` is a finite or recursively described family of typed polarized clauses;
- `D` is declared dependency/support structure;
- `V` is version/migration lineage.

A clause is:

`κ = <id, role, subject, predicate, μ, scope, version>`

with:

- `role ∈ {Assume, Require, Offer, Guarantee}`;
- negative polarity: Assume / Require;
- positive polarity: Offer / Guarantee;
- `μ=<q,u,χ,θ>` for quantifier, usage, continuity and temporal modalities.

K declares contract structure. It does not store current capability truth.

## 2. Polarized refinement

There is no universal unqualified refinement order.

### Provider substitution refinement

`K' ⊑prov K`

means K' may safely replace K in a provider-monotone context under witnessed compatibility:

- negative side requires no more than allowed by K;
- positive side provides at least the contract-relevant behavior of K;
- q/u/χ/θ, dependency, provenance, version and imported predicates remain compatible.

### Demand strengthening

`D' ⊒req D`

means D' accepts a subset of the providers/realizations accepted by D.

Canonical laws:

`ProviderRefinement != DemandStrengthening`.

`RefinementDirectionIsRoleRelative`.

## 3. Witnessed discharge

A positive clause p discharges a negative clause n only through:

`p ⊣_w n`

where witness w justifies, as applicable:

- predicate entailment/substitution;
- quantifier implication;
- usage accounting;
- continuity compatibility;
- temporal compatibility;
- version/migration compatibility;
- dependency/provenance preservation;
- required imported-owner predicates.

`SyntacticMatch != Discharge`.

## 4. Global witnessed wiring

Composition is defined primarily over a global wiring graph G/W, not over arbitrary binary syntax:

`Compose_Γ({K_i}, W, Π, H) => K_res`.

W maps selected negative clauses to positive clauses with discharge witnesses and retains usage/dependency/provenance lineage.

Sequential, parallel/open, branch/choice, transformation and feedback are derived wiring patterns.

`ContractComposition != LiveCapabilityComposition`.

Live capability standing remains a J judgement over σ/K/Π/H/E.

## 5. Observation signature and contextual equivalence

Algebraic equivalence is relative to an explicit observation signature:

`Ω_Γ = <BoundaryRoles, JudgementRoles, ProvenanceVisibility, IdentityVisibility, TimeScope, ImportScope>`.

Ω determines which externally relevant facts/judgements a context may distinguish. At minimum it may include:

- exposed positive/negative clauses and their q/u/χ/θ semantics;
- residual requirements/usage visible at the boundary;
- identity/continuity roles declared externally meaningful;
- dependency/provenance facts needed by allowed J judgements;
- version/migration standing when externally relevant;
- currentness/serviceability/satisfaction judgement roles within the declared time scope.

Two contracts/compositions are contextually equivalent when no Ω-admissible external contract context and compatible Π/H/J continuation can distinguish them:

`K1 ≃_{Γ,Ω} K2`.

Internal syntax/history may differ only when Ω explicitly abstracts that difference and all downstream required summaries remain preserved.

Canonical laws:

`ContextualEquivalenceIsObservationRelative`.

`HiddenInternalDifference != IrrelevantDifference`.

## 6. Conditional wiring associativity theorem

For a finite acyclic global wiring G, let two parenthesizations P1 and P2 be factorizations of G.

If:

1. both induce the same clause-discharge edges modulo alpha-renaming;
2. the same discharge witnesses remain valid under both factorizations;
3. usage accounting is equal or confluent/commuting under the admitted usage theory;
4. dependency/provenance closure is preserved before hiding;
5. no selector/branch-decision event is moved across the factorization;
6. no contract migration/version event is moved or inserted;
7. residualization is confluent for the same H/outcome/evidence history;
8. both factorizations expose the same Ω-boundary summary;

then:

`P1(G) ≃_{Γ,Ω} P2(G)`.

This is the **Conditional Wiring Associativity Theorem** for the finite acyclic fixed-wiring fragment.

Unconditional associativity is rejected.

`WiringAssociativityIsConditional`.

## 7. Operator-relative identities

No one identity contract serves every operator.

- Open/disjoint composition may use an empty boundary when it contributes no semantic effects.
- Serial boundary transport uses `Id_B`, a transparent wiring preserving clause roles/modalities, dependency/provenance, scope and version lineage.

`IdentityIsOperatorRelative`.

`IdentityWiring != CapabilityProducer`.

## 8. Hiding and abstraction

`Hide_S(K)` removes internal clause exposure only under an abstraction witness.

Hiding must preserve every summary required by Ω and later J judgements, including dependency/provenance, usage residual, version lineage and currentness obligations where relevant.

`Hide != Forget`.

`Encapsulation != DependencyErasure`.

`HiddenDependency != DischargedDependency`.

## 9. Provider-monotone contexts and precongruence theorem

A context `C[-]` is **provider-monotone relative to Γ,Ω** when substitution in the hole cannot observe or demand distinctions that the provider refinement is not required to preserve.

Side conditions include:

1. no unpreserved exact-instance/session identity dependence;
2. context usage is admissible under the refined provider usage modality;
3. required quantifier/temporal/continuity implications are witnessed;
4. dependency/provenance changes do not invalidate Ω-visible resilience/independence claims;
5. version/imported-predicate compatibility holds;
6. the context observes implementation details only through admitted Ω abstractions.

Then:

`ProviderMonotone_{Γ,Ω}(C,K',K) ∧ K' ⊑prov K`

implies

`C[K'] ⊑prov C[K]`

for the finite acyclic witnessed-wiring fragment.

This is the **Qualified Provider Refinement Precongruence Theorem**.

`RefinementPrecongruenceIsContextQualified`.

## 10. Choice object

Choice is explicitly typed:

`Choice = <B,s,q,δ,ρ>`

where:

- B = branch family;
- s = selector/decision authority or mechanism;
- q = quantifier/standing semantics;
- δ = dependency/correlation role;
- ρ = resolution timing/history rule.

Possible selector regimes include controller choice, environment/adversarial choice, stochastic outcome, sticky-active failover, hedged race, latent future opportunity and externally owned Harness selection.

Canonical laws:

`Branching != Selectability`.

`SelectableChoice != IndependentChoice`.

`ChoiceCardinality != AvailabilityGuarantee`.

`ChoiceResolution != BranchExistence`.

`RaceWinner != StablePreferredProvider`.

`ChoiceSemanticsRequiresSelectorOwnership`.

## 11. Quantifier discipline

Quantifier modes form no universal total scalar order.

Use only witnessed implication:

`q1 =>_Γ q2`

under the same declared conditioning/control/scope semantics.

`QuantifierDifference != ScalarStrengthDifference`.

Possible, controller-selectable, probabilistic, almost-sure and guaranteed modes may be incomparable without imported theory.

## 12. Usage discipline

Usage semantics are capability-family-specific.

Permitted operations may include reuse, consume, reserve, exclusive use, sharing, split, merge, transfer and discard when an admitted usage theory/witness supports them.

`TypedUsage != UniversalLinearResource`.

`NoImplicitDuplication`.

## 13. H-indexed contract transformation

Continuity and temporal changes are not pure algebraic rewriting:

`K --[h,w]--> K'`.

Examples:

- Harness selection may narrow any-provider to exact-instance/session continuity;
- rebind may preserve equivalence-class continuity but violate exact-instance continuity;
- wait changes deadline/freshness/lifetime residuals;
- expiration ends validity without implying satisfaction;
- generation/path change may invalidate exact continuity while stable public boundary identity remains unchanged.

`ContinuityTransformationRequiresHistory`.

`TemporalResidualDependsOnHistory`.

`Expiration != Satisfaction`.

`FuturePossibility != CurrentServiceability`.

## 14. Boundary Residual Normal Form

For finite acyclic K under fixed W and fixed witness ledger, define:

`BRNF_{Γ,Ω}(K,W)=<N_ext,P_ext,U_res,D*,V*,L_w>`

where:

- N_ext = externally undischarged negative clauses;
- P_ext = externally exposed positive clauses;
- U_res = usage/resource residual;
- D* = dependency/provenance closure required by Ω/J;
- V* = version/migration lineage summary;
- L_w = witness ledger sufficient to justify hidden discharge/abstraction.

### BRNF preservation theorem

If W/witnesses are fixed, the contract graph is finite/acyclic, all hiding is Ω-closed, and residualization is confluent, then:

`K ≃_{Γ,Ω} BRNF_{Γ,Ω}(K,W)`.

The theorem is relative to Ω. If Ω expands to expose a distinction omitted by the prior BRNF, the old normalization proof no longer applies.

Canonical laws:

`NormalFormIsWiringAndWitnessRelative`.

`NormalizationRequiresObservationClosure`.

`ObservationExpansionMayInvalidateNormalization`.

No globally unique canonical normal form is claimed.

## 15. Guarded finite recursive analysis fragment

The calculus admits recursive contract descriptions but rejects unsupported cyclic truth creation.

A **Grounded Guarded Finite Recursive Contract Fragment (G-GFRCF)** is admitted for bounded algorithmic analysis when:

1. the recursion graph has finitely many named clause/contract schemas;
2. every recursive strongly connected component has a grounding certificate:
   - an external/base support edge, or
   - an establishment/progress rule with a justified well-founded/progress witness, or
   - explicitly imported fixed-point semantics with admissibility conditions;
3. recursive H guards are semantic/provenance-bearing, not mere syntax labels;
4. modality implication domains are finite/decidable or delegated to bounded imported oracles;
5. no unbounded implicit duplication of consumable/exclusive capabilities is admitted;
6. bounded unfolding preserves clause/version identity and provenance.

The fragment may support decidable structural well-formedness and bounded discharge/refinement checks relative to imported oracles.

It does **not** decide live capability standing.

Canonical laws:

`GuardedSyntax != GroundedRecursion`.

`BoundedUnfolding != CapabilityProof`.

`DecidableFragment != UniversalDecidability`.

`ContractCycle != CapabilityWitness`.

## 16. Choice instantiations

### Workstation sticky/race/failover

- B = configured egress members;
- s = sticky-active plus hedged-race policy;
- q = current admission/service opportunity under eligible-member evidence, not guaranteed availability;
- δ = dependency/correlation remains separately projected;
- ρ = admission-time race/failover history.

Current configured branch count can coexist with zero eligible members.

`StableBoundaryIdentity != CurrentLeaseStanding`.

### DTN future opportunity

Branches may be future contact opportunities. Selection may be environment/schedule/opportunity-driven rather than controller-selectable. Eventual possibility is not current serviceability.

### Harness-selected provider

B may be discovered candidate providers while s is externally owned by Harness. Harness selection induces an explicit H bridge and may strengthen K continuity; Network does not annex the decision semantics.

These three regimes are not collapsed into one generic OR operator.

## 17. Owner membrane

The calculus owns Network contract structure and Network-specific preservation laws only.

It imports rather than owns:

- normative legitimacy/permission/authority;
- security/authentication/trust semantics;
- generic probability/control/information mathematics;
- Harness planning/selection intent;
- Runtime execution/effect truth;
- World/Physics underlying support reality;
- SCD description meaning.

`ComposedBoundary != OwnerMerge`.

## 18. Closure status

Network Capability Calculus v1 is FROZEN at the current evidence frontier.

Freeze is justified because:

- the polarized K carrier survived destructive testing;
- role-relative refinement survived;
- witnessed discharge/composition survived;
- a sound conditional associativity theorem is available on the finite acyclic fixed-wiring fragment;
- qualified provider-refinement precongruence is available on provider-monotone contexts;
- BRNF is semantics-preserving relative to explicit Ω and fixed witnesses;
- choice semantics survive Workstation, DTN and Harness-selection instantiations without false selectability/independence claims;
- grounded guarded recursion rejects unsupported bootstrap cycles without claiming universal decidability;
- real Workstation pool evidence supports stable boundary vs dynamic lease/currentness separation;
- no NCT v1 reopen condition or NDF FoundationReopenCondition fired.

This is strong provisional derived-theory closure, not a machine-checked proof of all theorems, exhaustive algebraic completeness, or academic novelty/priority claim.

## 19. Capability Calculus Reopen Conditions

Reopen v1 if a concrete case establishes one of:

1. a K-relevant Network contract role not representable by polarized clauses, typed modalities, dependency/version structure and J/H interfaces;
2. a valid composition whose semantics cannot be represented by witnessed global wiring/residualization;
3. a counterexample to the stated finite-fragment conditional associativity side conditions;
4. a provider-monotone context satisfying the stated side conditions where refinement precongruence still fails;
5. a finite acyclic fixed-wiring case where Ω-closed BRNF changes an allowed external judgement;
6. a choice regime requiring branch count alone to imply selectability/independence/availability;
7. a sound recursive capability whose standing arises from an ungrounded contract cycle, falsifying `ContractCycle != CapabilityWitness`;
8. a usage regime requiring universal contraction/linearity rather than typed family-specific usage;
9. a concrete upstream NCT/NDF reopen condition.

No such condition is currently established.
