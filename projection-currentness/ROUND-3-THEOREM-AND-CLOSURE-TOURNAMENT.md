# Network Projection & Currentness Theory — Round 3
## Theorem and Closure Tournament

Status: COMPLETE

Final decision: **FREEZE Network Projection & Currentness Theory v1**.

## A. Authority compatibility tournament

### Failed candidate

A universal authority lattice ranking Source > Observation > Inference > Belief or Owner A > Owner B for all claims.

This fails because authority is claim-role specific. A Workstation watchdog may own a health observation but not normative permission; a Research owner may own semantic current-recovery authority but not Host Task continuity; an operator-primary discovery source may identify a provider but still not own current admission/serviceability truth.

### Survivor

Define claim-local authority policy:

`AP_Γ(ck)=<claimOwner,admissibleAuthorityRoles,comparisonRules,supersessionRules,correctionRules,migrationRules>`.

This policy may import external-owner predicates but does not globalize them.

New laws:

- `AuthorityCompatibilityIsClaimLocal`;
- `AuthorityRankDoesNotGlobalize`;
- `ProjectionCannotAdjudicateBeyondClaimOwnerPolicy`.

PASS.

## B. Supersession transitivity/acyclicity tournament

### Same-epoch theorem

Within one fixed claim epoch ε, if owner policy precedence/correction rules are irreflexive/transitive and effective-scope precedence composes consistently, claim-relative supersession is a strict partial order and therefore acyclic.

### Migration counterexample

Generation G1 health evidence and generation G2 health evidence should not be forced into one transitive supersession chain. G2 begins a different exact-generation claim epoch. Similar pressure comes from path change, rebind and K-version migration.

### Repair

Supersession is epoch-local. Cross-epoch relation is explicit claim migration/lineage, not supersession.

New laws:

- `SupersessionIsEpochLocal`;
- `SupersessionTransitivityStopsAtMigration`;
- `MigrationDoesNotCarryStandingByDefault`;
- `CrossEpochSplicingForbidden`.

PASS AFTER BOUNDARY REPAIR.

## C. Evidence Frontier determinacy tournament

### Finite/bounded theorem

For a finite admissible evidence set A under a strict partial supersession order, the set of maximal elements `Max_▷(A)` is mathematically unique and independent of insertion/input order.

If deterministic conflict rules are evaluated over this frontier, conflict preservation is also input-order independent.

### Infinite-chain counterexample

An infinite strict ascending evidence chain may have no maximal element. Treating `Max=empty` as UNKNOWN would be semantically wrong because evidence exists but no terminal/maximal observation has been materialized.

### Repair

The determinacy theorem applies to finite query snapshots or more general evidence structures satisfying the required maximality condition. Live streams must be queried at an explicit cutoff/materialized snapshot or with another admitted completion condition.

New laws:

- `FrontierDeterminacyRequiresMaximalityCondition`;
- `InputOrderDoesNotDetermineFrontier`;
- `ConflictPreservationIsFrontierInvariant`.

PASS AFTER DOMAIN CONDITION.

## D. Conservative-refinement adequacy theorem

### Theorem

For fixed Γ/Ω/targetJ/time/claim epoch:

`Adequate(π1) ∧ π2 ⪰^c π1 => Adequate(π2)`.

This follows because conservative refinement is admitted only when every distinction/provenance/currentness/identity/dependency predicate required by targetJ is preserved.

### Apparent counterexamples

- a fresh negative observation invalidates old serviceability;
- time advances beyond freshness threshold;
- new generation appears;
- K demand strengthens.

These are not conservative projection refinements under fixed premises. They are evidence updates, time changes, epoch migrations or target changes.

### New distinction

`ProjectionRefinement != EvidenceUpdate`.

`AdequacyPreservationRequiresFixedTarget`.

PASS.

## E. Standing-bridge stability tournament

A ClaimMatch/VerifiedCapability/Reachability/Serviceability derivation D may transport from π1 to π2 only when π2 conservatively refines π1 and preserves all bridge witnesses used by D, while K/time/identity epoch remain unchanged.

A new evidence frontier can legitimately invalidate D. A stronger/different K demand can also invalidate Serviceability even when the network projection itself is unchanged.

New laws:

- `StandingDerivationIsSnapshotRelative`;
- `ServiceabilityTransportRequiresStablePremises`;
- `EvidenceUpdateMayInvalidateStanding`.

PASS as a conditional theorem; unconditional standing monotonicity is rejected.

## F. Multi-generation historical-retention tournament

Consider:

`G1 -> G2 -> G3`.

Correct semantics preserves evidence under separate epochs. Current G3 serviceability may transport selected predicates from prior generations only through explicit migration witnesses. The following is forbidden:

- G1 verified capability evidence;
- G2 reachability/binding evidence;
- G3 current identity;
- spliced together into one unwitnessed G3 Serviceability proof.

Historical evidence remains available under G1/G2 effective scope, and recovery never rewrites those intervals.

Canonical laws:

- `HistoricalRetention != CurrentAdmissibility`;
- `CrossEpochSplicingForbidden`;
- `RecoveredStanding != RetroactiveStanding`;
- `Recovery != HistoryReset`.

PASS.

## G. Current Workstation closure dogfood

Round-3 read-only observations remain:

### surf-clash

- current observation with a stable generation/capability identity;
- domain status UNAVAILABLE;
- namespace/resolver/transport/required-target/service health negative.

This remains direct evidence for `Currentness != PositiveStanding`.

### finance-okx

- stable profile/authority digest;
- memberCount=2;
- domain status UNKNOWN;
- no eligible members;
- no active member;
- listener/service inactive.

This remains direct evidence for stable identity vs current standing separation and branch-count non-availability.

No network mutation occurred.

## H. Cross-owner stale-ready closure pressure

Old Network exploration can remain Host READY while later Network owner/Research-System authority treats it as historical for semantic recovery. Under v1 these map to different claim keys/authority policies. They coexist; neither projection annexes the other's owner semantics.

PASS.

## I. Final closure decision

### FREEZE

Network Projection & Currentness Theory v1 is frozen with:

- typed projection families/instances;
- truth-role separation;
- typed claim keys and claim epochs;
- immutable evidence;
- claim-local authority policies;
- epoch-local supersession strict partial orders;
- explicit migration graph;
- deterministic evidence frontiers on finite/maximality-satisfying snapshots;
- conflict-preserving evidence composition;
- typed currentness distinct from domain standing;
- completeness-witnessed absence-to-negation;
- conservative projection refinement/equivalence;
- role-relative identity/binding transitions;
- bridge-witnessed standing promotions;
- snapshot-relative standing transport;
- multi-generation historical retention without cross-epoch splicing.

### Freeze does not mean

- universal authority ordering;
- last-write-wins semantics;
- generic epistemology or probability theory;
- monotonic standing under all new evidence;
- currentness as one Boolean;
- machine-checked universal proof;
- production implementation mandate;
- external academic novelty claim.

No NCT v1, Capability Calculus v1 or NDF reopen condition fires. NDF6 remains NOT ADMITTED.
