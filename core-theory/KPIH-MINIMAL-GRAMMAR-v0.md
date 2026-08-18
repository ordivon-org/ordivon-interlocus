# K×Π×H Minimal Grammar v0

Status: ROUND-2 PROVISIONAL / DERIVED THEORY ONLY

This grammar is a higher-order reconstruction over frozen NDF0-NDF5. It is not NDF6 and does not change Foundation authority.

## 1. External indices and imports

A Network judgement is indexed by context/query/cut `Γ` and may refer to underlying support reality `σ` owned by World/Physics/Runtime/other semantic owners. Network does not redefine `σ`.

`Γ` minimally selects:

- Network query / operational cut;
- participating locus roles / role boundary;
- time/history scope;
- principal/consumer role where relevant;
- claim/evidence scope where relevant.

## 2. K — Capability–Requirement Contract Boundary

`K` is a typed contract schema, not a store of current Network truth.

Minimal clause roles:

- `Assume(a)` — imported or upstream premise required by a composition/use;
- `Offer(c)` — capability role that an interface/realization purports to expose if its premises are discharged;
- `Require(d)` — demand/requirement role against which outcomes/continuations may be evaluated;
- `Guarantee(g)` — promised contract property conditional on discharged assumptions;
- `Quantifier(q)` — existential / selectable / probabilistic / almost-sure / guaranteed / bounded variants as typed by the contract;
- `Usage(u)` — reusable / consumable / reserved / exclusive / split / merge / other typed usage semantics;
- `Continuity(kappa)` — any-provider / equivalent-provider / exact-instance / association/session / lineage-sensitive continuation;
- `Temporal(tau)` — validity, lifetime, deadline, freshness or other time-scope requirement;
- `Version(v)` — contract identity/version and explicit migration/refinement relation where applicable;
- `Residual(r)` — undischarged continuation obligation after a partial realization/outcome.

`K` may import opaque predicates from SCD, Security, Physics, Time, etc. Their internal semantics remain externally owned.

### K non-circularity law

`K` may select which distinctions a projection must preserve, but it cannot make a projected/source fact true merely by requiring it.

`SelectionDependence != TruthDependence`.

## 3. Π — Qualified Network Projection Family

`Π` is a typed family of query/cut-relative Network projections over source reality, histories and evidence.

Projection roles include:

- `StructuralΠ`: SSP-style loci/membership, incidence, configuration, history projection;
- `DependencyΠ`: shared support / correlated failure / realization dependency projection;
- `ReferenceΠ`: reference, candidate, binding, locator/attachment and continuity-relevant projection;
- `CapabilitySupportΠ`: projected support conditions relevant to an Offer/Assume clause without equating projection with current capability truth;
- `ObservationΠ`: observed evidence-bearing view;
- `InferenceΠ`: inferred/believed view with explicit model/provenance;
- `CohortΠ`: transition/lineage/cohort view when merge, repair or continuity depends on history.

Truth roles remain distinct:

`SourceΠ != ObservationΠ != InferenceΠ != BeliefΠ`.

Projection adequacy is a judgement, not identity:

`Adequate_Γ(Π, K)` means Π preserves the distinctions required to soundly judge the relevant K clauses under Γ.

K may guide projection selection; Π values remain grounded in source/evidence/history, not in K.

## 4. H — Admissible Realization History

`H` is a typed history/transition object, not necessarily a static path, discrete total order, packet trace or forwarding lineage.

Admissible event/transition families include:

- establish / expose / revoke capability;
- transform / refine / split / merge / consume / reserve capability/resource;
- wait / store / carry;
- discover / derive / resolve / bind / rebind;
- forward / branch / revisit / repair;
- contract-version migrate / supersede;
- lineage/cohort merge or reconciliation;
- evidence acquisition/update;
- other typed histories admitted by a Foundation specialization.

`H_fwd ⊂ H` is the forwarding-specialized family governed by NDF5. Not every H is forwarding.

## 5. Higher-order transition form

A generic derived-theory transition schema is:

`H_Γ : (σ, K, Π) -> (σ', K', Π', o, E)`

where:

- `σ,σ'` are imported support reality states/history cuts;
- `K,K'` are contract/residual boundaries;
- `Π,Π'` are qualified Network projections;
- `o` is an outcome/result role, not intrinsically positive service;
- `E` is evidence/provenance emitted or acquired by the history.

This is a schema, not a claim that every regime is discrete, deterministic or functional.

## 6. Core judgements

### Semantic capability standing

`Cap_Γ(σ, K, Π, H) ⊨ c`

means the current source/support/history plus an adequate projection semantically witness capability role `c` under K and Γ.

It does NOT mean we currently possess adequate evidence to assert the claim operationally.

### Evidence-supported capability claim

`E ⊢_Γ ClaimLive(c | K, Π, H)`

means evidence E is adequate/current enough to support asserting the capability claim at the declared scope.

`SemanticCapabilityTruth != EvidenceSupportedCurrentClaim`.

### Satisfaction / residual update

`Eval_Γ(Require(d), K, Π_pre, H, o, Π_post) => (status, Residual(d'))`

where status may be satisfied / partially-satisfied / unchanged / worsened / violated / indeterminate under the declared demand semantics.

Positive service is derived by this judgement; it is not an intrinsic label on `H` or `o`.

### Composition / assumption discharge

`Discharge_Γ(K1, K2, Π, H) => K_residual`

requires typed refinement/compatibility, quantifier preservation, usage/dependency preservation and explicit residual obligations. Syntactic endpoint/field matching is insufficient.

### Projection adequacy

`Adequate_Γ(Π,K)`

requires every K-relevant distinction needed by the target judgement to be preserved or explicitly abstracted with a witness. A projection may be adequate for one K/query and inadequate for another.

### Resolution

`Resolve_Γ(r, K, Π, H) ⇓ (candidate/binding, Π', E)`

is a derived Pi/H judgement subject to K eligibility/continuity clauses and lineage preservation.

`ClaimMatch != VerifiedCapability != Reachability != Serviceability` remains a chain of distinct judgements.

## 7. Non-circularity discipline

Potential cycle:

`K -> selects Π -> Π supports capability standing -> capability standing appears in K`.

Repair:

1. K contains contract syntax/roles, not current capability truth.
2. Projection construction may be query/K-guided, but source/evidence determines Π values.
3. Capability standing is derived from `(σ,K,Π,H)`, not assumed by K.
4. Evidence-supported currentness is a second judgement over E, not semantic truth by observation.
5. A derived live capability may update K' as an exposed role only through an explicit establishment/refinement history witness; this is No Unwitnessed Capability Creation.

Therefore query dependence is permitted without truth circularity.

## 8. Owner membrane

- `σ` reality: World/Physics/Runtime/etc. as appropriate.
- semantic description predicates imported in K: SCD.
- authority/trust/authentication predicates: Security/Authority.
- Agent decision/planning/task semantics: Harness/Host.
- execution/job semantics: Runtime/Computing.
- generic probability/control/information/statistics: external mathematics.

Network owns the typed K/Π/H projections and Network-specific laws connecting them.
