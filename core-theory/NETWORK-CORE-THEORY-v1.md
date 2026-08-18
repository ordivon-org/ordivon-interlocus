# Ordivon Network Core Theory v1

Status: FROZEN DERIVED THEORY at the current evidence frontier

This is a higher-order compression and judgement calculus over the frozen/repaired NDF0-NDF5 corpus. It is not NDF6, does not replace Foundation provenance, and does not change external owner truth.

## 1. Core form

Canonical v1 form:

`NCT_v1 = <K, Π, H ; J>_Γ`

with imported support reality `σ`.

The semicolon is intentional:

- `K`, `Π`, and `H` are the three deletion-essential semantic carriers/axes;
- `J` is a first-class typed judgement layer over those carriers, not a fourth state/substance axis.

Generic transition schema:

`H_Γ : (σ, K, Π) -> (σ', K', Π', o, E)`

The schema is formalism-neutral: histories may be nondeterministic, probabilistic, continuous, partially ordered, branching, resource-transforming, forwarding, or otherwise typed by a specialization.

## 2. K — Capability–Requirement Contract Boundary

K specifies the operational distinctions that matter to a Network capability/service claim. It is not a store of current truth.

Canonical clause roles:

- Assume;
- Offer;
- Require;
- Guarantee;
- Quantifier;
- Usage;
- Continuity;
- Temporal;
- Version;
- Residual.

`Require` and `Guarantee` are operational interface/service roles. They do not by themselves mean moral/legal/deontic obligation, legitimacy, permission, jurisdiction or normative authority. Such predicates may be imported opaquely from Ordivon Normative/Security/other owners when a Network contract depends on them.

### K laws

1. `SelectionDependence != TruthDependence` — K may select what Π must distinguish; it cannot make a source/projected fact true.
2. `ContractSyntax != CapabilityStanding` — declaration is not live capability truth.
3. `QuantifierPreservation` — possible/selectable/probabilistic/almost-sure/guaranteed claims are not silently interchangeable.
4. `ContractEvolutionRequiresWitness` — standing under K_t does not automatically transport to K_t+1.
5. `ResidualObligationsPersistUntilDischargedOrSuperseded`.

## 3. Π — Qualified Network Projection Family

Π is not arbitrary representation. An admissible Network projection must have:

`Π = <SourceRole, Scope/Cut, ProjectionRelation, View, Provenance, AdequacyTarget>`

where the primary subject remains a Network-owned cross-locus operational capability/interaction/service/binding/forwarding role.

Canonical projection families include:

- structural SSP projections;
- dependency/support projections;
- reference/binding/locator projections;
- capability-support projections;
- observation/evidence projections;
- inference/belief projections;
- cohort/lineage/transition projections.

### Π discipline

1. `ProjectionGrounding` — Π values must be grounded in source reality, evidence, or typed history; query selection does not generate their values.
2. `ProjectionNonGeneration` — encoding a K clause or H history inside a view does not create a requirement, capability truth, or occurrence.
3. `RepresentationNonSubstitution` — a representation of K/H cannot replace their independent semantic roles merely because it is information-complete.
4. `SourceΠ != ObservationΠ != InferenceΠ != BeliefΠ`.
5. `AdequacyIsQueryRelative` — Π may be adequate for one K/J target and lossy for another.
6. `ProjectionNonAnnexation` — projecting an external fact into Network does not transfer ownership of its internal semantics.

These constraints prevent Π from expanding into an unconstrained universal representation axis.

## 4. H — Admissible Realization History

H represents typed establishment/use/change history. It is not universally a path, packet trace, total order or forwarding lineage.

Admitted families include:

- establish/expose/revoke;
- transform/refine/split/merge/consume/reserve;
- wait/store/carry;
- discover/derive/resolve/bind/rebind;
- forward/branch/revisit/repair;
- contract migration/supersession;
- lineage/cohort merge/reconciliation;
- evidence acquisition/update.

NDF5 forwarding histories satisfy:

`H_fwd ⊂ H`.

### H laws

- `NonIdentityWait`;
- `NoUnwitnessedCapabilityCreation`;
- `Proposal != ExecutedAction`;
- `DormantLineageObligationPreservation`;
- `CohortMergeRequiresCompatibility`;
- historical occurrence is not erased by later recovery/rebinding.

## 5. J — Typed Network Judgement Layer

J is first-class because currentness, serviceability, satisfaction and adequacy are relations over K/Π/H/E, not fields that belong intrinsically to one axis.

Canonical judgement families:

### Capability standing

`Cap_Γ(σ,K,Π,H) ⊨ c`

Semantic standing of capability role c.

### Evidence-supported current claim

`E ⊢_Γ ClaimLive(c | K,Π,H)`

Adequate/current evidence supports asserting a live claim at the declared scope.

`SemanticCapabilityTruth != EvidenceSupportedCurrentClaim`.

### Projection adequacy

`Adequate_Γ(Π,K,J_target)`

Π preserves the distinctions required by the intended judgement.

### Satisfaction / residual

`Eval_Γ(Require(d),K,Π_pre,H,o,Π_post) => (status,Residual(d'))`

Positive service is derived here; it is not intrinsic to o or H.

### Resolution

`Resolve_Γ(r,K,Π,H) ⇓ (binding,Π',E)`

subject to eligibility, continuity and lineage constraints.

### Composition / discharge

`Discharge_Γ(K1,K2,Π,H) => K_residual`

with typed assumption/guarantee refinement, dependency, usage and quantifier preservation.

### Currentness

`Current_Γ(x | role, scope, τ, E, H)`

Currentness is role-specific. Identity currentness, health currentness, binding currentness, evidence currentness, admission standing and serviceability are not one Boolean property.

## 6. Recursive composition law

Recursive or mutually dependent contracts are permitted as descriptions, but cycles do not bootstrap truth.

Canonical anti-law:

`ContractCycle != CapabilityWitness`.

If A requires capability B and B requires capability A, the cycle alone cannot establish either capability. Live standing requires an external/source support witness, an establishment history, or an explicitly imported fixed-point semantics with a justified base/admissibility rule.

This is a direct consequence of No Unwitnessed Capability Creation plus Dependency Preservation.

## 7. NDF0-NDF5 reconstruction

- NDF0 InterLocusCapability -> K carrier roles + Cap judgement.
- NDF1 capability composition/realization -> K + H + Discharge/Cap judgements.
- NDF2 Structural Projection -> Π + Adequate judgement.
- NDF3 Demand/Service/Satisfaction -> Require/Residual in K + Eval judgement over H/o/Π.
- NDF4 Reference/Binding/Resolution/Discovery -> K continuity/eligibility + Π reference/binding/provenance + H resolution histories + Resolve/ClaimLive judgements.
- NDF5 Forwarding/Reachability -> forwarding-specialized Π/H plus forwarding-specific J predicates; never a universal realization gate.

No durable Foundation responsibility is orphaned by this reconstruction.

## 8. Owner membrane

### World / Physics / domain reality

Own underlying entities, resources, physical state, causal reality and generic occurrence truth represented by σ or imported predicates.

### Ordivon Normative / Security / Authority

Own legitimacy, normative validity, permission/jurisdiction and generic trust/authority semantics. Network K may condition on those predicates but cannot generate them.

### Runtime / Computing

Own Operation/Attempt/execution/computation/effect semantics. Network may supply a current inter-locus capability/serviceability premise consumed by Runtime.

Canonical separation:

`NetworkServiceable != RuntimeAdmitted != RuntimeAttemptSucceeded != ExternalEffectTrue`.

### Harness / Host

Harness owns Agent/Task/Context/selection/invocation/control mediation; Host owns durable Task continuity and semantic work continuation. Network supplies discovery/binding/capability/transport surfaces.

Canonical separation:

`NetworkDiscoveryMatch != HarnessSelected != HarnessInvoked != RuntimeAttempt`.

## 9. Currentness and recovery laws from engineering dogfood

The Workstation scoped-egress lineage supplies strong downstream falsification evidence:

1. configured profile identity can remain stable while live health/service standing changes;
2. parent/child identity may remain current through transient red health or exact-path recovery backoff while new admission correctly fails closed;
3. stale health evidence may be superseded by newer owner evidence rather than permanently poisoning the capability;
4. generation/path identity changes invalidate continuity even if names/ports remain equal;
5. `MemberCount > 1` does not imply independent or currently available alternatives;
6. a current `UNKNOWN` projection does not prove semantic impossibility.

Canonical derived separations:

`IdentityCurrent != HealthCurrent != AdmissionStanding != Reachable != Serviceable`.

`Configured != Live`.

`Multiplicity != Independence != Availability`.

`HistoricalStanding != CurrentStanding`.

## 10. Closure status

Derived Network Core Theory v1 is FROZEN at the current evidence frontier because:

- K, Π and H each survived deletion attacks;
- Π overbreadth is blocked by explicit grounding/non-generation/adequacy rules;
- operational requirements do not require Normative owner transfer;
- recursive contracts do not bootstrap capability and require witnesses;
- Evidence/Currentness requires J but not a fourth semantic carrier axis;
- NDF3/NDF4/NDF5 reconstruct without orphan responsibilities;
- Network×Runtime and Network×Harness theorem transport preserves owner membranes;
- classical, quantum, DTN, Agentic, higher-order/collective and Ordivon engineering regimes do not currently falsify the core.

This is strong provisional derived-theory closure, not exhaustive mathematical completeness.

## 11. Core-Theory Reopen Conditions

Reopen or reject NCT v1 only on a concrete case showing one of:

1. a Network-owned semantic responsibility not representable by K, Π, H, J or typed relations/outputs over them;
2. an admissible Π that requires generating truth/requirements/history rather than projecting grounded source/evidence/history;
3. a genuine Network operational requirement whose truth conditions are irreducibly normative and therefore invalidate the current owner membrane;
4. recursive capability standing that can soundly arise from unsupported contract cycles, falsifying ContractCycle != CapabilityWitness;
5. evidence/currentness semantics requiring an independent Network substance/state axis rather than J;
6. a realization family requiring NDF5 forwarding universally;
7. a cross-owner case where Network cannot expose/consume a typed interface without annexing Runtime/Harness/Host/World/Normative/SCD/Security truth;
8. a concrete new counterexample firing an underlying NDF FoundationReopenCondition.

No such condition is currently established.
