# Network Core Theory — Round 2
## Positive Reconstruction, Non-Circularity, Derived-Judgement Tests, and Ordivon Dogfood

Status: COMPLETE / K×Π×H SURVIVES ROUND 2 WITH ONE IMPORTANT WORDING REPAIR

## 1. Round 2 question

Round 1 repaired the initial pure triad into:

`NetworkCore ~= K × Π × H`

where K was called Capability-Obligation Contract Boundary, Π Qualified Projection, and H Realization History.

Round 2 asks whether this is a real theory rather than a renaming:

1. can K, Π and H be typed without circular definitions;
2. can NDF3 satisfaction/residual semantics be derived rather than hidden;
3. can NDF4 resolution/currentness/lineage factorization survive stale/churn/splicing attacks;
4. can NDF5 remain only a realization specialization;
5. does live Ordivon engineering expose a missing fourth axis?

## 2. Wording repair: Obligation -> Requirement at the owner boundary

The word `Obligation` is useful inside NDF1/NDF3 operational contract grammar but risks confusion with Ordivon Normative's constitutive/normative admission semantics.

No semantic owner transfer is intended. Therefore the higher-order project-root name is repaired to:

`K = Capability–Requirement Contract Boundary`

while typed operational `obligation` / `residual obligation` remains admissible inside K where it denotes a contract role, not moral/legal/normative ought.

This is wording/boundary repair only, not a Foundation reopen.

## 3. Minimal grammar result

A separate artifact, `KPIH-MINIMAL-GRAMMAR-v0.md`, defines:

- K: Assume, Offer, Require, Guarantee, Quantifier, Usage, Continuity, Temporal, Version, Residual roles;
- Π: Structural, Dependency, Reference/Binding, Capability-Support, Observation, Inference and Cohort projection families;
- H: establishment/transformation/consumption/wait/discovery/resolution/rebinding/forwarding/repair/merge/evidence histories;
- semantic capability standing, evidence-supported current claim, satisfaction/residual update, composition/discharge, projection adequacy and resolution judgements.

## 4. K <-> Π non-circularity attack

### Attack

Capability truth may depend on topology, binding, dependency or evidence projections. But those projections are often selected because the contract asks whether a capability exists. If K stores the answer and Π is selected from K, K×Π becomes self-certifying.

### Destructive matched case

Take two worlds with identical K syntax:

`Require HTTPS CONNECT to public IPv4:443 under profile P`.

World A has a live eligible anchor/listener and an adequate current projection witnessing it. World B has the same declared profile but no eligible member/listener. If K itself stores `live=true`, the theory cannot distinguish declaration from truth without circularly importing Π back into K.

### Repair

K stores contract roles/syntax, not current standing. Π values are grounded in source/evidence/history. K may select which distinctions Π must preserve; it cannot determine those values.

Canonical anti-law:

`SelectionDependence != TruthDependence`.

Capability standing is a derived judgement:

`Cap_Γ(σ,K,Π,H) ⊨ c`.

Evidence-supported assertability is separate:

`E ⊢_Γ ClaimLive(c | K,Π,H)`.

### Verdict

NON-CIRCULARITY PASS after the explicit declaration-vs-standing separation.

## 5. NDF3 reconstruction / fourth-axis attack

### Candidate derivation

Service/satisfaction is reconstructed as:

`Eval_Γ(Require(d),K,Π_pre,H,o,Π_post) => (status,Residual(d'))`.

This keeps the Round-1 counterexample intact: same outcome, different demand -> different status/residual.

### Hostile cases

- exact-version demand vs freshness demand over the same cached response;
- hard deadline vs best-effort demand over the same eventual delivery;
- one constituent cancellation during shared/coded service;
- application usable while lower realization still has residual completion obligations.

In every case the distinguishing information is a typed Require/Temporal/Continuity/Residual role in K, with H/o evaluated against it. No independent substance beyond K/Π/H is needed.

### Verdict

Demand/Evaluation FOURTH AXIS PRESSURE DOES NOT SURVIVE ROUND 2.

Satisfaction remains a deletion-essential judgement but not a fourth state axis.

## 6. NDF4 reconstruction / stale-churn-splicing attack

Resolution is reconstructed as:

`Resolve_Γ(r,K,Π,H) ⇓ (binding,Π',E)`.

K carries eligibility and continuity constraints. Π carries candidate/reference/binding/locator/provenance/current-view state. H carries discovery, derivation, verification, resolution and rebinding transitions.

### Attack A — stale capability claim

A candidate advertised capability at t0, but readiness/endpoint state changed before use. Historical ClaimMatch cannot be silently transported to current Serviceability.

Required discipline:

- claim/evidence timestamp/scope remains in Π/E;
- H records change/revalidation/rebinding where witnessed;
- current assertion requires a fresh enough `ClaimLive` judgement;
- absence of fresh evidence may yield UNKNOWN rather than semantic falsehood.

### Attack B — churn after broad discovery

Initial K may require `exists provider satisfying P`; after selection/session, K' may require exact-instance or association continuity. Re-discovering another P-provider is not automatically a valid continuation.

This is Quantifier-to-Continuity Transition represented as K -> K' through H.

### Attack C — cross-candidate splicing

Capability evidence for candidate A plus locator/binding evidence for candidate B cannot justify one serviceable candidate unless an explicit equivalence/substitution/aggregation history witnesses the transfer.

This is represented by Π lineage/provenance plus H derivation identity and K continuity/equivalence clauses.

### External pressure

The current A2A 1.0.0 specification requires Agent Cards describing identity, capabilities/skills and interaction requirements, and standardizes discovery mechanisms. This is naturally a claim/discovery surface, not proof that a currently advertised capability is reachable, authorized or serviceable. K×Π×H preserves that separation.

### Verdict

NDF4 FACTORIZATION PASS. No Addressability/Resolution fourth axis required.

## 7. NDF5 specialization reconstruction

Define `H_fwd ⊂ H` for forwarding-specific histories with NDF5 traffic-lineage, residual refinement, transition/cohort and Q-relative control semantics.

Quantum entanglement establishment/swapping may use other H families and therefore remains a counterexample to universal forwarding. DTN may mix H_fwd with wait/store/carry transitions without reducing all history to a contemporaneous path.

### Verdict

NDF5 SPECIALIZATION PASS; universal realization gate remains rejected.

## 8. Evidence/currentness theorem candidate

Round 2 strengthens a cross-cutting law:

`ConfiguredOrAdvertised != SemanticallyLive != EvidenceSupportedCurrent != Reachable != Serviceable`.

The exact middle ordering is role-dependent: semantic truth may exist without current evidence, while evidence may support only a bounded claim rather than complete serviceability.

Therefore currentness is not one Boolean property stored in K or Π. It is a judgement over scope/time/history/evidence.

## 9. Live Ordivon engineering dogfood — 2026-08-18

Read-only Workstation observations were taken during Round 2; no route, proxy, TUN, TLS or service mutation was performed.

### finance-okx scoped egress profile

Observed current projection:

- profile exists with proxy `http://127.0.0.1:19083`;
- status `UNKNOWN`;
- listenerReachable=false;
- serviceActive=false;
- parentHealthOk=false;
- watchdogDisposition=`no-eligible-member`;
- memberCount=2, eligibleMembers=[].

### surf-clash anchor

Observed current projection:

- status `UNAVAILABLE`;
- namespacePresent=false;
- resolverHealthy=false;
- transportHealthy=false;
- requiredTargetsHealthy=false;
- serviceActive=false.

### native-a / native-b anchors

Both currently project `UNKNOWN` with no current generation/capability digest and inactive/unhealthy transport evidence.

### Dogfood consequences

1. `ProfileConfigured != LiveCapability`.
2. `MemberCount=2 != AvailableAlternativeRealization`.
3. Historical existence/success cannot be transported to current standing without current witness — Contract/Capability Currentness is time/evidence qualified.
4. `UNKNOWN` is necessary: missing/failed current evidence is not equivalent to proving the semantic capability impossible.
5. A loopback proxy address existing in configuration does not imply listener reachability or serviceability.
6. The same K requirement can remain stable while Π/H/current evidence changes and the current capability judgement changes. This is direct empirical support for K/Π non-circularity.

No product mutation was performed; this is theory dogfood only.

## 10. External theory confrontation

Assume-guarantee contract literature independently supports separating environment assumptions from guarantees and treating refinement/composition as first-class operations. Relational-interface work also shows interface and contract formalisms are related but not trivially identical. K×Π×H therefore should not collapse K into Π merely because both can be represented relationally.

This is supporting analogy, not external authority for Ordivon Network truth.

## 11. Round 2 result

Round-2 survivor:

`NetworkCore v0 candidate = K × Π × H`

with the clarified names:

- `K` = Capability–Requirement Contract Boundary;
- `Π` = Qualified Network Projection Family;
- `H` = Admissible Realization History.

Core derived form:

`H_Γ : (σ,K,Π) -> (σ',K',Π',o,E)`

plus distinct judgements for:

- semantic capability standing;
- evidence-supported current claim;
- satisfaction/residual update;
- projection adequacy;
- composition/assumption discharge;
- resolution/binding;
- forwarding specialization.

No fourth axis survives Round 2. No FoundationReopenCondition fires. NDF6 remains NOT ADMITTED.

## 12. What is still unproved

Round 2 does NOT yet establish a frozen Network Core Theory v1.

Remaining destructive pressure:

1. whether K's Require/Guarantee grammar duplicates generic Normative semantics despite the operational boundary wording;
2. whether Π becomes overbroad enough to absorb K/H and destroy the compression;
3. whether evidence/currentness requires a first-class typed judgement layer beyond the three state/history axes;
4. whether recursive/higher-order capability composition requires a fixed-point or hypercontract structure not captured by the current schema;
5. whether multi-owner theorem transport can preserve the Network owner membrane under more complex Runtime/Harness cases;
6. whether real healthy/failover Ordivon cases, not only a currently degraded snapshot, preserve the same factorization.

## 13. Next research round

Round 3 should not search NDF6. It should run the **Core-Theory Closure Tournament**:

- projection-overbreadth attack;
- operational requirement vs Normative-owner boundary attack;
- recursive composition / hypercontract attack;
- semantic truth vs evidence/currentness typed-layer attack;
- healthy->degraded->recovered engineering lineage dogfood;
- cross-owner Network×Runtime and Network×Harness theorem-transport tests;
- then decide FREEZE / REPAIR / REJECT for Derived Network Core Theory v1.

## External primary/reference sources used for pressure only

- RFC 9171, Bundle Protocol Version 7.
- RFC 9340, Architectural Principles for a Quantum Internet.
- Agent2Agent Protocol Specification, latest released 1.0.0 at time of Round 2.
- Nuzzo et al., From Relational Interfaces to Assume-Guarantee Contracts, UC Berkeley EECS Technical Report 2014-21.
- de Alfaro and Henzinger interface-theory lineage, used only as external comparison for contract/interface separation.
