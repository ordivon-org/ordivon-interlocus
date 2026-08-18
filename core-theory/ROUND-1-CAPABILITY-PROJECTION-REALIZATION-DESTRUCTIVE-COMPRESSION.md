# Network Core Theory — Round 1
## Capability × Projection × Realization Destructive Compression

Status: COMPLETE / PROVISIONAL CORE REPAIR SUPPORTED

This round tests whether the frozen/repaired NDF0-NDF5 architecture admits a smaller higher-order theory. It is explicitly not an NDF6 search.

## 1. Candidate under test

Initial candidate:

`NetworkCore ?= Capability × Projection × Realization`

The candidate is admitted only if it can compress NDF0-NDF5 without deleting a responsibility, hiding a distinction by renaming it, making forwarding universal, or absorbing external-owner truth.

## 2. Foundation-to-axis factorization

| Foundation | Capability | Projection | Realization | Residual pressure |
|---|---|---|---|---|
| NDF0 InterLocusCapability | PRIMARY | qualification only | witness/history only | none |
| NDF1 Capability Composition / Realization Algebra | PRIMARY | dependency/evidence views | PRIMARY | capability boundary already contains claims + obligations |
| NDF2 Structural Projection / Interaction Geometry | indirect | PRIMARY | structural-history update | none |
| NDF3 Demand / Service / Satisfaction | insufficient under pure Capability | observation/feasibility views | outcome/action/residual transition | STRONG: demand/satisfaction is not identical to outcome history |
| NDF4 Reference / Binding / Resolution / Discovery | continuity/eligibility constraints | PRIMARY for reference/binding/scoped views | PRIMARY for discovery/resolution/rebinding | factorizes; no independent axis required |
| NDF5 Forwarding / Reachability Realization | residual forwarding contracts | routing/forwarding/control projections | PRIMARY traffic/transition lineage | specialization only |

### Immediate result

The pure initial triad FAILS IN SCOPE because NDF3 preserves a deletion-essential distinction:

`same outcome/history + different demand -> different service/satisfaction standing`.

Realization tells us what occurred. It does not by itself determine whether the occurrence satisfied the current demand, freshness requirement, exact-version requirement, deadline, constituent obligation, or continuity requirement.

## 3. Repair of the first axis

The failure does not yet justify a fourth independent axis because repaired NDF1 already distinguishes a `CapabilityBoundary K` containing typed exposed/assumed capability claims **and obligations**. NDF3 deepens the obligation side through demand identity, lifecycle, continuation residuals and satisfaction semantics.

Therefore the minimally repaired candidate is:

`NetworkCore ~= Capability-Obligation Contract × Qualified Projection × Realization History`

Abbreviated:

`K × Pi × H`

where:

- `K` — typed capability/obligation contract boundary: offered/assumed capabilities, demanded/guaranteed obligations, quantifiers, usage conditions, continuity constraints, contract versions and residual obligations;
- `Pi` — typed query/cut-relative Network projections: structural SSP, dependency views, reference/binding views, source/observed/inferred distinctions, and evidence/provenance-qualified operational views;
- `H` — admissible realization histories/transitions: establishment, transformation, consumption, discovery, resolution, rebinding, waiting/storage, forwarding, repair, merge and other capability-changing or capability-using histories.

Underlying support state `sigma` remains imported reality, not a fourth Network axis. Outcome `o` and evidence `E` are realization outputs / claim-support objects whose truth roles must remain distinct.

A generic higher-order form is therefore:

`H_Gamma : (sigma, K, Pi) -> (sigma', K', Pi', o, E)`

with service/satisfaction derived by evaluating the realized outcome/history against the obligation side of `K`, producing residual/updated obligations rather than treating 'positive service' as intrinsic to the action.

## 4. Deletion tests

### Delete K — FAIL

Matched worlds can have the same underlying relation, projection and event history while differing on whether an inter-locus relation is exposed/consumable under the relevant contract. Likewise, the same realized delivery can satisfy one obligation and violate another. Without K the theory cannot distinguish operational capability from arbitrary cross-locus causation, nor service from mere occurrence.

Verdict: K is deletion-essential.

### Delete Pi — FAIL

The same high-level capability contract and nominal realization can have different validity under different dependency, binding, topology, cohort or evidence projections. Two alternative realizations may share one hidden dependency; two matching candidates may have different locator lineage; source structure may differ from observed/inferred structure. Without typed projections the theory loses the distinctions needed for Dependency Preservation, Structural Projection, Witness/Lineage Preservation and ClaimMatch != VerifiedCapability != Reachability != Serviceability.

Verdict: Pi is deletion-essential.

### Delete H — FAIL

Capability and projection alone do not distinguish proposal from executed action, waiting from identity, old/new/repair transition histories, resource establishment from mere possibility, or discovery claims from completed resolution. Quantum entanglement generation/swapping, DTN store-carry-forward, forwarding transitions and Agent discovery all require typed histories.

Verdict: H is deletion-essential.

## 5. Fourth-axis tournament

### Demand / Evaluation

Strongest fourth-axis pressure. Pure `Capability × Projection × Realization` fails here. However demand/obligation is already structurally paired with capability inside NDF1's K and is needed to interpret NDF3 residual/satisfaction semantics. The minimal repair is therefore `Capability-Obligation Contract`, not a separate fourth substance at this round.

Standing: ABSORBED BY REPAIRED K, subject to future falsification.

### Resolution / Addressability

NDF4 factorizes into:

- K: eligibility/continuity/reference constraints;
- Pi: typed reference/binding/distributed scoped views/provenance;
- H: discovery, derivation, resolution and rebinding histories.

No matched-world counterexample yet requires Resolution as an independent fourth axis once these roles remain typed and lineage-preserving.

Standing: FACTORIZED; no fourth axis.

### Evidence / Currentness

Evidence cannot be collapsed into semantic support state or outcome. However the higher-order model can retain evidence as typed epistemic/provenance projections and realization outputs while preserving source/observed/inferred distinctions. This is not permission to equate evidence with truth.

Standing: CROSS-CUTTING TYPED QUALIFIER / PROJECTION FAMILY; no independent axis yet.

### Forwarding

NDF5 remains a specialization of Pi + H under forwarding-specific K. Quantum relational-resource realization proves forwarding cannot be universal.

Standing: SPECIALIZED REALIZATION FAMILY; no fourth axis.

## 6. Hostile-regime attacks

### Classical communication

K expresses the communication contract and quantifier strength; Pi exposes relevant loci/dependencies/bindings; H carries the actual communication/forwarding history. No extra axis required.

PASS.

### Quantum relational-resource capability

RFC 9340 distinguishes a quantum data plane that can provide Bell-pair resources to applications from classical user-data carriage, and describes entanglement generation/swapping as a key realization pattern. This pressure falsified the historical Communicability-only NDF0 but fits repaired K × Pi × H: K exposes a relational-resource capability with fidelity/usage obligations; Pi distinguishes physical, resource-backed and binding views; H represents generation/swapping/delivery. NDF5 forwarding is optional rather than universal.

PASS; revalidates the NDF0 repair and non-universal NDF5 rule.

### Delay-/disruption-tolerant networking

RFC 9171 explicitly supports intermittent connectivity, non-concurrent sender/receiver presence, store-carry-forward, scheduled/predicted/opportunistic connectivity and late binding. K carries lifetime/delivery obligations; Pi carries temporal/contact/binding projections; H carries store/wait/carry/forward histories. `Non-Identity Wait` remains necessary.

PASS.

### Dynamic Agent discovery

Current A2A specifications expose Agent Cards containing identity, capabilities/skills, endpoints and interaction/authentication information, with discovery through well-known locations, registries/catalogs or direct configuration. This regime pressures NDF4 but does not require an independent Addressability axis: claims/bindings are Pi, eligibility/continuity requirements are K, and discovery/resolution/rebinding is H. Agent planning, selection and task execution remain Harness/Runtime-owned.

PASS with owner membrane preserved.

### Biological / collective / higher-order interaction projection

Primary higher-order-network research demonstrates that group/higher-order interaction representations can alter collective dynamics relative to pairwise representations. This pressures Pi against graph-only reduction, but it does not by itself transfer biological/social process ownership into Network. A Network projection is admitted only relative to an explicit query/cut where a cross-locus operational capability/interaction role is the subject.

PASS AS PROJECTION PRESSURE; owner transfer rejected.

## 7. Derived-law placement

- Typed Assumption Discharge -> K
- Assume/Guarantee Refinement -> K
- Contextual Contract-Relative Equivalence -> K + Pi
- Dependency Preservation -> K + Pi
- No Unwitnessed Capability Creation -> H => K'
- Quantifier Preservation -> K
- Non-Identity Wait -> H
- Contract Evolution -> K + H
- Query-Relative Structural Projection -> Pi
- Witness Mapping/Lifting -> Pi + H
- Structural No-Resurrection -> Pi + H
- source/observed/inferred separation -> Pi
- Proposal != ExecutedAction -> Pi/H boundary; executed standing requires H
- Witness/Lineage Preservation -> Pi + H
- Cross-Candidate Splicing anti-law -> Pi
- Dormant-Lineage Obligation Preservation -> K + H
- Cohort/Lineage Merge Compatibility -> K + Pi + H

No durable derived law is left unmapped after the K repair.

## 8. Round 1 verdict

`Capability × Projection × Realization` = REJECTED AS TOO NARROW IN ITS FIRST AXIS.

`Capability-Obligation Contract × Qualified Projection × Realization History` = ROUND-1 SURVIVOR.

This is a derived-theory compression, not a new Foundation architecture. NDF0-NDF5 remain frozen; NDF6 remains NOT ADMITTED; no FoundationReopenCondition fired.

The strongest new proposition is:

> Network cases may be reconstructed as typed transformations over a capability/obligation contract boundary, a family of query-relative Network projections, and an admissible realization history, while underlying reality remains externally owned.

## 9. Reopen / falsification conditions for the triad

The repaired triad must be rejected or expanded if a concrete case demonstrates any of the following:

1. a Network-owned semantic responsibility that cannot be represented as K, Pi, H, or a typed relation/output over them;
2. a deletion-essential demand/evaluation structure that cannot be represented on the obligation side of K without circularity;
3. a resolution/addressability law that cannot factor into K constraints + Pi binding/reference state + H resolution history;
4. evidence/currentness semantics whose truth role cannot remain distinct when represented as typed Pi/E outputs;
5. a realization family that requires NDF5 forwarding as universal, contradicting the quantum repair;
6. owner-boundary failure where the compression requires importing World/Runtime/Harness/Host/SCD/Security/generic-math truth as Network-owned.

## 10. Next round

Round 2 should attempt a positive formal reconstruction of K, Pi and H rather than another Foundation search:

- define minimal typed objects and judgments;
- prove/falsify non-circularity between K and Pi;
- separate semantic current capability from evidence-supported capability claim;
- reconstruct NDF3 satisfaction/residual update as a derived judgment;
- reconstruct NDF4 resolution as Pi/H factorization;
- reconstruct NDF5 as one specialization of H;
- then dogfood the theory against real Ordivon egress/serviceability/dependency cases.

## External pressure sources consulted

- RFC 9340 — Architectural Principles for a Quantum Internet.
- RFC 9171 — Bundle Protocol Version 7.
- Agent2Agent Protocol — official specification and Agent Discovery documentation.
- Zhang, Lucas & Battiston (2023), Higher-order interactions shape collective dynamics differently in hypergraphs and simplicial complexes, Nature Communications.
