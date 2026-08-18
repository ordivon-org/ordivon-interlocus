# Network Capability Calculus — Round 1
## Minimal Calculus and Destructive Tests

Status: COMPLETE / v0 CANDIDATE SURVIVES

## 1. Starting pressure

Frozen NCT v1 exposes K roles but intentionally does not define a contract algebra. A useful calculus must be expressive enough for NDF1/NDF3/NDF4-derived cases while avoiding four failure modes:

1. turning K into current-truth storage;
2. using one syntactic refinement direction for provider substitution and demand strengthening;
3. treating composition as field matching and thereby erasing dependency/usage/quantifier semantics;
4. importing a generic logic/type system as if it were Network ontology.

## 2. Minimal-object tournament

Candidates considered:

- untyped clause set;
- fixed A/G pair;
- relational interface only;
- state machine/protocol only;
- linear resource sequent only;
- polarized typed clause graph.

### Rejections

A plain clause set loses variance and dependency. A fixed A/G pair is too narrow for Network Require/Offer/continuity/usage roles. A pure relational interface risks collapsing K into Π. A state machine belongs primarily to H/protocol realizations. Universal linear sequents incorrectly force reusable/shareable/affine regimes into one resource logic.

### Survivor

`K=<kid,C,D,V>` with polarized typed clauses `κ=<id,role,subject,predicate,μ,scope,version>` and typed dependency declarations.

This is structural enough for calculus while keeping live truth in J and realization in H.

## 3. Refinement-direction attack

### Counterexample

Demand D0: `any provider satisfying P`.

After Harness selects provider A, the Network continuation demand becomes D1: `exact instance A / same session lineage`.

D1 is stricter than D0; its satisfaction set is smaller.

By contrast, a provider implementation P1 that requires fewer assumptions and guarantees more is a substitutive refinement of P0.

Trying to express both changes with one unqualified `<=` reverses variance somewhere.

### Result

Two relations are explicitly separated:

- provider substitution refinement `⊑prov`;
- demand strengthening `⊒req`.

General law: `RefinementDirectionIsRoleRelative`.

## 4. Composition/discharge attack

### Counterexample A — syntactic match without quantifier strength

Requirement: guaranteed reachability during scope τ.
Offer: merely possible reachability during τ.

Same subject/predicate does not discharge the requirement.

### Counterexample B — same endpoint, incompatible continuity

Requirement: exact-instance/session continuation.
Offer: any equivalent provider.

Field/type compatibility is insufficient.

### Counterexample C — version mismatch

Old provider contract and new consumer contract use nominally identical capability names but changed semantics. Contract Evolution requires an explicit migration/refinement witness.

### Result

Discharge requires a witness across predicate, quantifier, usage, continuity, temporal, version and dependency dimensions.

`SyntacticMatch != Discharge`.

Composition is represented by a typed wiring W over clauses, yielding a residual contract. Sequential/parallel/choice/feedback are derived wiring patterns rather than mandatory primitive operators.

## 5. Quantifier attack

A universal chain such as:

`possible < probabilistic < selectable < almost-sure < guaranteed`

is unsound because these modes depend on control authority, conditioning and imported probability semantics and can be incomparable.

Example: controller-selectable among two actions is not equivalent to a random event of probability p; almost-sure does not imply per-history guarantee.

### Result

K carries a typed q and accepts only witnessed implication `q1 =>_Γ q2`.

No universal scalar quantifier strength is admitted.

## 6. Usage/resource attack

### Quantum relational-resource case

Two Bell-pair resources used in entanglement swapping cannot be duplicated by contract composition. The input resources are consumed/changed while a different relational resource may be established.

### Classical reusable service case

A classical service capability may be reusable across requests, but reuse may still share capacity/failure dependencies.

A universal linear resource rule would reject legitimate reuse; universal contraction would duplicate consumable/exclusive resources.

### Result

Usage is a typed capability-family algebra/reference. Split/merge/reuse/consume/reserve/discard require explicit admitted operations/witnesses.

`TypedUsage != UniversalLinearResource` and `NoImplicitDuplication`.

## 7. Dependency attack

Two route/provider alternatives can share one physical anchor, resolver, authority, power source or control plane.

Contract-level branch count therefore cannot establish independence.

### Result

K may declare dependency/support structure, but actual independence is a J judgement grounded by Π dependency projection and provenance/H.

`AlternativeRealization != IndependentRealization`.

Hiding an internal support clause after composition cannot erase the underlying dependency:

`HiddenDependency != DischargedDependency`.

## 8. Temporal / DTN attack

A DTN contract can remain meaningful when no contemporaneous path exists. Requirement may persist through store/wait/carry and a future contact may establish a service opportunity.

Therefore:

- current unavailability does not cancel the requirement;
- wait is not identity;
- eventual/future possibility is not current serviceability;
- residual demand survives until discharged, expired or explicitly superseded.

The calculus leaves temporal predicate semantics imported and uses H/J for actual standing.

PASS.

## 9. Agent discovery/selection attack

Initial discovery demand:

`Require exists provider satisfying capability predicate P`.

After Harness selection:

`Require exact instance A / session lineage κ`.

This is a cross-owner H event inducing a new K continuity mode. It is demand strengthening, not proof that A remains live or serviceable.

PASS.

## 10. Runtime/Harness bridge attack

A Network K may export `Offer(remote-serviceability)` and discharge one Runtime input premise. But Runtime admission/Attempt/effect semantics remain Runtime-owned; Harness selection/invocation remains Harness-owned.

The K calculus can compose boundary contracts without identifying their semantic owners.

`ComposedBoundary != OwnerMerge`.

PASS.

## 11. Recursive/meta-contract attack

### Unsupported cycle

A offers X if B offers Y; B offers Y if A offers X.

No external support exists.

Naive fixed-point acceptance could bootstrap both capabilities.

### Result

`ContractCycle != CapabilityWitness` remains mandatory. A recursive description needs base support, establishment history, or imported justified fixed-point admissibility.

The calculus intentionally makes no universal algorithmic decidability claim for recursive refinement/composition.

## 12. External primary-literature confrontation

### Assume-guarantee contracts / relational interfaces

Nuzzo, Iannopollo, Tripakis and Sangiovanni-Vincentelli show that a natural transformation from relational interfaces to A/G contracts can preserve refinement while failing to preserve serial composition without an additional assumption-projection operator. This is strong pressure against treating refinement, interface projection and composition as interchangeable operations. It supports the Network decision to keep K distinct from Π and make discharge/composition explicitly witnessed.

### Resource-aware session types

Das, Balzer, Hoffmann, Pfenning and Santurkar use shared session types plus linear typing/resource analysis to prevent invalid duplication/deletion of contract assets in their digital-contract setting. This supports resource-sensitive usage as a serious compositional concern, but also illustrates why Network should import/use linearity only for capability families whose usage law warrants it rather than universalizing linear logic.

### Recursive session types / subtyping

Recursive session-type work shows that recursion materially complicates duality/subtyping; richer nested recursive session subtyping can become undecidable. This is pressure against claiming one complete decision procedure for all recursive Network contract refinement. The calculus therefore defines semantic admissibility/judgements first and leaves algorithms to bounded specializations.

These literatures are comparison/falsification pressure only, not authority for Network ownership.

## 13. Round-1 verdict

Capability Calculus v0 survives with the following core shape:

- polarized typed clause graph K;
- orthogonal typed modality bundle q/u/χ/θ;
- role-relative refinement relations;
- witnessed clause discharge;
- composition as wiring + residualization;
- explicit dependency/provenance preservation;
- no implicit resource duplication;
- recursive contracts allowed as syntax but cycles cannot bootstrap standing;
- live capability remains a J judgement over σ/K/Π/H.

No NCT v1 reopen condition fires. No NDF Foundation reopen condition fires. NDF6 remains NOT ADMITTED.

## 14. Round-2 frontier

Next attack should determine whether v0 can support a compact algebra rather than only semantic rules:

1. derive algebraic laws for wiring composition: associativity conditions, identity/open boundary, hiding and residualization;
2. test when refinement is a precongruence under composition and when dependency/usage/quantifier context breaks it;
3. define choice/branch algebra without turning alternatives into independence;
4. define temporal and continuity transformation laws under H events;
5. test whether a normal form exists for finite non-recursive K;
6. classify recursive fragment(s) with sound decidable approximations without universal decidability claims;
7. dogfood against real Workstation scoped-egress pool/failover contracts.
