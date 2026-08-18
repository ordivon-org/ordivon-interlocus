# Ordivon Network Capability Algebra v0

Status: PROVISIONAL DERIVED THEORY / ROUND-2 SURVIVOR

Upstream authorities:

- frozen `NCT_v1=<K,Π,H;J>_Γ`;
- Capability Calculus v0 from Round 1.

This artifact identifies algebraic laws that survive destructive testing. The laws are deliberately conditional: the calculus does **not** form one unconditional monoid/lattice/semiring over all Network contracts.

## 1. Wiring composition

Let a finite family of contracts be `{K_i}` and let `W` be a typed wiring relation mapping selected negative clauses to positive clauses with discharge witnesses.

`Compose_Γ({K_i},W,Π,H) => K_res`

The semantic object being composed is the **witnessed global wiring graph**, not a textual nesting of binary operators.

## 2. Conditional associativity

Binary parenthesizations are contextually equivalent only when they are factorizations of the same admissible global wiring.

Define `AssocAdmissible_Γ(G)` for a global wiring graph G when at least:

1. clause identities are disjoint up to alpha-renaming;
2. both parenthesizations induce the same positive-to-negative discharge edges;
3. discharge witnesses remain valid in the larger context;
4. usage accounting is identical or provably commuting/confluent;
5. dependency/provenance edges are preserved before any hiding;
6. no branch-selection authority/event is moved across the reassociation;
7. no contract migration/version transition is inserted between the two bracketings;
8. residualization is confluent for the same H/outcome/evidence history.

Then:

`AssocAdmissible_Γ(G) => ((K1 ⊗ K2) ⊗ K3) ≃_Γ (K1 ⊗ (K2 ⊗ K3))`

where both sides are merely presentations of G.

Canonical law:

`WiringAssociativityIsConditional`.

Unconditional associativity is rejected. A consumable capability, an order-sensitive branch choice, an early hide, or a version migration can make the two parenthesizations observably different.

## 3. Identity is operator-relative

There is no single universal identity object for every composition family.

### Open/disjoint composition unit

For disjoint union/open parallel composition, an empty boundary contract can act as a unit when it contributes no clauses, dependency, version or usage effects.

### Transparent wiring identity

For serial wiring over a boundary B, define `Id_B` as a transparent wiring context that bijectively transports compatible clauses while preserving:

- role/polarity;
- predicate semantics;
- q/u/χ/θ modalities;
- clause/version lineage;
- dependency/provenance;
- scope.

`Id_B` is not a provider that manufactures capability. It is a structural wiring witness.

Canonical laws:

`IdentityIsOperatorRelative`.

`IdentityWiring != CapabilityProducer`.

## 4. Hiding / encapsulation

`Hide_S(K)` may remove a set S of internal clause interfaces from the exposed boundary only if an abstraction witness proves that externally relevant semantics are preserved.

At minimum:

1. hidden negative clauses are discharged or intentionally encapsulated;
2. hidden positive clauses are not externally required by identity/continuity semantics unless replaced by an explicit abstract interface;
3. dependency/support lineage is retained in D/Π/provenance summaries;
4. usage/residual accounting is retained;
5. version/migration lineage remains traceable;
6. evidence/currentness obligations needed by J are not erased.

Canonical laws:

`Hide != Forget`.

`Encapsulation != DependencyErasure`.

`HiddenDependency != DischargedDependency`.

## 5. Provider-refinement precongruence

Provider substitution refinement is not automatically a precongruence in every contract context.

A context `C[-]` is provider-monotone for `K' ⊑prov K` only when the hole is used in a way that preserves substitutability. Typical side conditions include:

- no exact identity/session requirement that singles out K's original provider unless a substitution witness permits K';
- usage demand placed by C is within K' usage semantics;
- quantifier/temporal/continuity clauses required by C are preserved by the refinement witnesses;
- new dependency/provenance facts of K' do not falsify context-visible independence/failure-domain claims;
- version/imported-owner predicates remain compatible;
- C does not inspect intentionally hidden implementation identity except through an admitted abstraction.

Then:

`ProviderMonotone_Γ(C,K',K) ∧ K' ⊑prov K => C[K'] ⊑prov C[K]`.

Canonical law:

`RefinementPrecongruenceIsContextQualified`.

Counterexamples arise from exact-instance continuity, exclusivity/consumption conflicts, dependency-sensitive resilience claims, and version/provenance constraints.

## 6. Choice algebra

A branch set is not enough to define choice semantics.

Represent a choice boundary as:

`Choice = <B, s, q, δ, ρ>`

where:

- `B` = typed branch family;
- `s` = selection/decision authority or mechanism;
- `q` = quantifier/standing semantics of the choice;
- `δ` = dependency/correlation declaration/projection reference;
- `ρ` = resolution timing/history rule.

Selection modes may include, without universalizing them:

- environment/adversarial choice;
- controller-selectable choice;
- stochastic outcome;
- hedged race / first-success;
- sticky-active failover;
- latent alternative with no current selector;
- externally selected branch.

Canonical anti-laws:

`Branching != Selectability`.

`SelectableChoice != IndependentChoice`.

`ChoiceCardinality != AvailabilityGuarantee`.

`RaceWinner != StablePreferredProvider`.

`AlternativeRealization != IndependentRealization`.

Choice composition therefore carries selector/quantifier/dependency semantics explicitly rather than deriving them from branch count.

## 7. H-indexed continuity transformations

Continuity changes are not pure K algebra; they are K transformations induced by typed H events and validated by J.

Generic form:

`K --[h,w]--> K'`.

Examples:

### Selection

`any-provider(P) --HarnessSelect(A)--> exact-instance(A)`

when the consumer/session semantics requires instance continuity.

### Rebinding

A rebind A->B may preserve an any-provider/equivalence-class requirement but fails exact-instance/session continuity unless an explicit substitution/migration witness permits it.

### Recovery

Recovery may preserve stable capability identity while changing health/admission standing. Identity preservation is a J/H result, not inferred from names.

### Generation/path change

A generation/path identity change may invalidate exact continuity even when the public contract name/port remains unchanged.

Canonical law:

`ContinuityTransformationRequiresHistory`.

## 8. H-indexed temporal transformations

Temporal clauses evolve under time/history; wait is never algebraic identity by default.

Examples:

- deadline residual decreases with elapsed time;
- freshness requirement may become unsatisfied while content identity stays fixed;
- DTN eventual-delivery requirement can persist while current serviceability is false;
- expiration may terminate a requirement without implying it was satisfied;
- a future contact event may move a capability from merely possible to currently serviceable only when J witnesses the new standing.

Canonical laws:

`TemporalResidualDependsOnHistory`.

`Expiration != Satisfaction`.

`FuturePossibility != CurrentServiceability`.

## 9. Finite acyclic boundary-residual normal form

For a finite non-recursive contract family with fixed wiring W and fixed discharge witnesses, define a **Boundary Residual Normal Form (BRNF)**:

`BRNF(K,W) = <N_ext, P_ext, U_res, D*, V*, L_w>`

where:

- `N_ext` = externally undischarged negative clauses;
- `P_ext` = externally exposed positive clauses;
- `U_res` = residual usage/resource state;
- `D*` = dependency/provenance closure required for external judgements;
- `V*` = version/migration lineage summary;
- `L_w` = witness ledger for internal discharge/hiding.

BRNF is useful for comparison and composition planning, but it is not globally unique:

- different admissible wirings can yield different residuals;
- different predicate/refinement witnesses may be incomparable;
- branch selection semantics may intentionally remain unresolved;
- imported predicates may not possess canonical normal forms.

Therefore:

`NormalFormIsWiringAndWitnessRelative`.

No universal canonical normal form is claimed.

## 10. Safe recursive fragment candidate

A **Guarded Finite Recursive Contract Fragment (GFRCF)** is proposed for algorithmic experimentation, not frozen as universal semantics.

Candidate restrictions:

1. finite named recursion graph;
2. no runtime generation of unbounded new contract schemas;
3. recursive discharge cycles require explicit progress/establishment guards checked against H/J;
4. finite or externally decidable modality implication domains;
5. imported predicate implication is provided by a bounded decision oracle or treated as unknown;
6. no unbounded implicit duplication of consumable/exclusive usage-bearing clauses;
7. finite clause/version identifiers modulo guarded recursion.

Under these restrictions, structural well-formedness, bounded unfolding and some refinement/discharge checks can be decidable **relative to the imported oracles**.

Semantic live capability standing remains outside this syntactic decidability result.

Canonical discipline:

`DecidableFragment != UniversalDecidability`.

## 11. Workstation scoped-egress mapping

The Workstation fault-tolerant egress pool is a concrete downstream consumer of the calculus.

### Stable K-like authority

Historical pool implementation defines a stable authority containing:

- profile identity;
- loopback CONNECT endpoint;
- member set;
- allowed TCP ports;
- selection policy `sticky-active-with-hedged-racing-on-admission`;
- fail-closed behavior when no eligible member exists.

The stable authority intentionally excludes active member generation.

### Dynamic realization/currentness

Lease/current observation carries active member, per-member eligibility, member lease/generation, listener/health standing, failover/race history.

Tests establish that profile authority identity stays stable while lease digest changes when active member changes.

This maps cleanly to:

- stable K identity/requirements;
- Π/J eligibility/currentness/dependency views;
- H member selection, race and failover transitions.

### Choice falsifier

Configured `memberCount=2` does not imply two eligible members, independence, selectability, or availability. Current read-only observation on 2026-08-18 reports:

- status `UNKNOWN`;
- `memberCount=2`;
- `eligibleMembers=[]`;
- `activeMember=null`;
- `listenerReachable=false`;
- `serviceActive=false`.

Therefore the pool strongly supports the choice anti-laws above.

### Hiding/currentness lesson

Stable authority hides dynamic member generation from consumer identity, but generation/lease provenance is retained in the dynamic lease/currentness surface. This is valid encapsulation, not forgotten dependency/currentness.

Canonical dogfood law:

`StableBoundaryIdentity != CurrentLeaseStanding`.

## 12. v0 algebra standing

The algebra that survives Round 2 is intentionally **partial and side-condition-rich**:

- composition is global-wiring based;
- associativity is conditional;
- identities are operator-relative;
- hiding preserves dependency/provenance;
- refinement precongruence is context-qualified;
- choice carries selector/quantifier/dependency semantics;
- temporal/continuity change is H-indexed;
- finite normal form is witness-relative;
- recursive decidability is fragment-relative.

This is stronger than an unstructured contract calculus and more conservative than claiming a universal algebraic structure that the hostile cases falsify.
