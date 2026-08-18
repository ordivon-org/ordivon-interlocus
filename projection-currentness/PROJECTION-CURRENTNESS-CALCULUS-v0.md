# Ordivon Network Projection & Currentness Calculus v0

Status: PROVISIONAL DERIVED THEORY / ROUND-2 SURVIVOR

Upstream authorities:

- frozen `NCT_v1=<K,Π,H;J>_Γ`;
- frozen Network Capability Calculus v1;
- Projection & Currentness Theory v0.

This calculus owns Network-facing claim/evidence/projection/currentness relations. It does not define generic epistemology, probability, Host continuity, Runtime execution truth, or underlying external-owner truth.

## 1. Claim key

Evidence is comparable only after resolving a typed claim identity.

Define:

`ck = <subjectRole, subjectIdentity, claimRole, scopeCut, lineageRole, contractVersion, effectiveDomain>`

where:

- `subjectRole` identifies the Network-facing kind of subject;
- `subjectIdentity` is the identity appropriate to the claim role (stable profile, exact generation, binding, candidate, session, etc.);
- `claimRole` identifies what is being claimed (health, binding-current, reachability, capability, serviceability, etc.);
- `scopeCut` identifies query/principal/topology/cut scope;
- `lineageRole` states which continuity relation makes observations comparable;
- `contractVersion` binds K semantics when the claim depends on a versioned requirement/capability contract;
- `effectiveDomain` declares time/event/cohort applicability semantics.

Raw string/key equality is insufficient. Claim-key comparison may require a typed migration/identity witness.

`SameLabel != SameClaim`.

## 2. Evidence identity

`e = <eid, ck, truthRole, authorityRole, sourceRef, value, effectiveScope, producedAt, provenance>`

Evidence identity is immutable. New evidence never mutates old evidence in place.

`EvidenceRevision != EvidenceMutation`.

If a source corrects itself, the correction is a new evidence object plus a typed supersession/correction relation.

## 3. Comparability

`Comparable_Γ(e1,e2)` only when:

1. claim keys are equal or connected by an admitted claim migration/identity witness;
2. truth roles are admissible for the comparison being made;
3. effective scopes overlap in the target query;
4. lineage identities are compatible for the claim role;
5. authority roles can be compared under the owner/import rules of that claim.

Otherwise the evidence may coexist without contradiction.

`DifferentScope != Conflict`.

`DifferentRole != Conflict`.

## 4. Supersession partial relation

Define:

`e2 ▷_{Γ,ck} e1`

when e2 supersedes e1 **for the named claim key and target scope**.

Necessary conditions include:

- `Comparable(e1,e2)`;
- e2 has admitted authority for the claim role;
- e2's effective scope is later/more current or explicitly corrective for the target scope;
- identity/lineage continuity or migration is witnessed;
- no truth-role downgrade is silently treated as an authority upgrade;
- the owner's supersession rule admits the replacement.

Supersession is a strict partial relation for one target query: irreflexive and transitive where the same claim/migration semantics compose.

It is **not** a universal total order.

Canonical laws:

`NewerTimestamp != Supersession`.

`HigherDetail != Supersession`.

`SupersessionIsClaimRelative`.

`Supersession != Erasure`.

## 5. Migration, contradiction, coexistence

Keep distinct:

### Supersession

Same continuing claim role/lineage; newer/corrective evidence replaces old evidence for current judgement.

### Claim migration

`MigrateClaim_Γ(ck_old,h,w) => ck_new`

A version, generation, binding, or role transition maps an old claim identity to a new one. Evidence under `ck_old` remains historical evidence; it is not simply superseded as if the claim identity never changed.

### Contradiction/conflict

`Conflict_Γ(e1,e2 | ck)` when comparable, currently admissible evidence supports incompatible values and neither validly supersedes the other.

### Coexistence

Evidence about different scopes/roles/lineages may both be valid without conflict.

Canonical laws:

`Migration != Supersession`.

`Contradiction != Staleness`.

`Coexistence != Agreement`.

## 6. Evidence frontier

For a target `(ck, Γ, τ)`, let `A` be the set of admissible evidence after scope/truth-role/authority filtering.

Define the **current evidence frontier**:

`Frontier_Γ(ck,τ) = Max_▷(A)`

where `Max_▷` are the non-superseded maximal evidence objects under the claim-relative supersession partial order.

The frontier preserves:

- one current winner when authority/lineage rules resolve the claim;
- multiple non-conflicting views when they concern compatible subroles;
- multiple conflicting maxima when no valid supersession resolves disagreement;
- empty frontier when no admissible evidence exists.

Currentness standing can then be derived:

- empty admissible frontier -> `UNKNOWN` unless a separate absence/completeness proof applies;
- one/multiple compatible adequate maxima -> `CURRENT` for the evidence role;
- incompatible adequate maxima -> `CONFLICTED`;
- only evidence outside freshness/effective scope -> `STALE`;
- adequate evidence establishing lineage/version invalidation -> `NOT_CURRENT`.

Canonical law:

`CurrentView != LatestRecord`.

## 7. Conflict-preserving evidence composition

`ComposeEvidence_Γ(E, ck, τ) => <Frontier, ConflictSet, HistoricalSet, DerivationLedger>`

Composition may:

- eliminate superseded evidence from the current frontier while retaining it historically;
- preserve incomparable evidence;
- expose conflicts;
- derive bounded aggregate projections only with explicit derivation/model identity;
- never manufacture authority by aggregation.

`ConflictCannotBeResolvedByDroppingOneSide`.

`Aggregation != Adjudication`.

If a conflict needs authority resolution, that resolution must come from the claim owner's authority/supersession rules or an explicit external adjudication owner.

## 8. Absence and negative claims

Open-world absence is not negative evidence by default.

`NoObservation != NegativeObservation`.

`NoMatch != NoCapability`.

A negative existential claim such as `NoProvider(P)` requires a **coverage-completeness witness** appropriate to the query/cut/time scope, or another explicit source proof.

Define:

`Complete_Γ(π | query, cut, τ)`.

Only when completeness is justified may absence within π support a negative closed-world judgement.

`AbsenceToNegationRequiresClosureWitness`.

This is especially important for discovery, routing, dynamic membership and Agent/provider search.

## 9. Conservative projection refinement

For fixed `(Γ, Ω, targetJ, τ)`:

`π2 ⪰^c π1`

iff π2 is a conservative refinement of π1:

1. compatible subject/source role;
2. same target question or an explicitly admitted scope refinement;
3. all Ω-observable distinctions from π1 preserved;
4. provenance/truth role preserved without authority lift;
5. effective-time semantics compatible;
6. identity/lineage granularity refined with an explicit mapping;
7. no conflict hidden;
8. no previously visible dependency/support relation erased.

Then candidate adequacy theorem:

`Adequate(π1 | targetJ,Ω,τ) ∧ π2 ⪰^c π1 => Adequate(π2 | targetJ,Ω,τ)`.

The relation is partial and target-relative.

`ProjectionRefinementIsObservationAndTimeRelative`.

## 10. Projection equivalence

Define:

`π1 ≈_{Γ,Ω,targetJ,τ} π2`

when each conservatively refines the other with respect to the same target judgement/observation signature/time, or when an explicit abstraction witness proves indistinguishability for that target.

Projection equivalence is weaker than source identity and stronger than superficial view equality.

`EqualView != EquivalentProjection`.

`EquivalentProjection != SameSource`.

## 11. Identity transition calculus

Identity preservation is typed by identity role `ι`.

Define:

`TransitionId_Γ(x0, h, x1 | ι) => {PRESERVED, REPLACED, SPLIT, MERGED, INVALIDATED, UNKNOWN}`.

Examples:

- stable public profile across active-member failover: `PRESERVED`;
- exact active-member identity A->B: `REPLACED`;
- exact generation changes: prior generation identity `INVALIDATED` for current role;
- exact-path recovery with same generation/path: stable/exact parent identity may be `PRESERVED` even while admission fails;
- membership split/merge requires explicit lineage witness.

Canonical laws:

`IdentityTransitionIsRoleRelative`.

`RecoveryMayPreserveIdentityWithoutPreservingStanding`.

`StandingRecoveryDoesNotRestorePriorIdentityUnlessWitnessed`.

## 12. Binding transition calculus

A binding claim has a claim key including reference identity, target identity/granularity, binding version/generation and continuity role.

Typed events may yield:

- `BIND_PRESERVED`;
- `REBIND_EQUIVALENT`;
- `REBIND_NON_EQUIVALENT`;
- `BIND_STALE`;
- `BIND_INVALIDATED`;
- `BIND_UNKNOWN`.

Whether rebind preserves service continuity depends on K continuity requirements and J bridge witnesses.

`Rebinding != ContinuityPreservation`.

## 13. Standing bridge graph

The NDF4 distinction is represented as separate claim roles linked by typed bridge judgements, not one ordinal state machine.

### ClaimMatch

`ClaimMatch_Γ(candidate, K, π_discovery)`

means projected candidate metadata/claims match the requested predicate under the declared discovery scope.

It does **not** imply authority, verified capability, reachability, admission, or serviceability.

### VerifiedCapability

`VerifyCap_Γ(candidate, K, E, π) => VerifiedCapability`

requires appropriate owner/source/current evidence for the capability claim and relevant identity/version scope.

### Reachability

`Reachable_Γ(binding, path/cut, τ, E, π, H)`

requires a current binding/path/transport witness under the target scope.

### Serviceability

`Serviceable_Γ(candidate/binding, K, τ, E, π, H)`

requires the K-relevant combination of capability, reachability and additional service conditions; it is demand/contract relative.

Canonical non-implications:

`ClaimMatch ⇏ VerifiedCapability`.

`VerifiedCapability ⇏ Reachable`.

`Reachable ⇏ Serviceable`.

`HistoricalServiceability ⇏ CurrentServiceability`.

Each promotion requires a typed bridge witness.

`StandingPromotionRequiresWitness`.

## 14. Cross-owner continuation

Network serviceability may be consumed as a premise by Runtime/Harness, but:

`Serviceable_Network != Admitted_Runtime != AttemptSucceeded_Runtime`.

Harness candidate selection may consume ClaimMatch/VerifiedCapability projections, but:

`ClaimMatch_Network != Selected_Harness`.

Host/Research currentness can project into a Network-facing historical/currentness example but remains externally owned.

`ProjectedForeignCurrentness != NetworkAuthority`.

## 15. Workstation supersession pattern

Historical Workstation tests provide a clean claim-relative supersession example for parent health under one exact generation/path:

- an admission health fence can be newer than an older red watchdog and temporarily be the current health evidence source;
- once the watchdog produces newer evidence for the same generation/path/health role, the watchdog becomes current;
- a stale admission fence can be superseded by a newer fresh watchdog;
- a stale admission fence is not rescued by an even older watchdog;
- generation/path changes invalidate comparability/current identity rather than merely superseding the old claim value.

This supports:

`SameClaimLineageRequiredForTemporalSupersession`.

`GenerationChangeMayMigrateClaimInsteadOfSupersedingValue`.

## 16. Round-2 candidate laws

1. `SameLabel != SameClaim`.
2. `EvidenceRevision != EvidenceMutation`.
3. `DifferentScope != Conflict`.
4. `DifferentRole != Conflict`.
5. `NewerTimestamp != Supersession`.
6. `SupersessionIsClaimRelative`.
7. `Migration != Supersession`.
8. `Contradiction != Staleness`.
9. `CurrentView != LatestRecord`.
10. `ConflictCannotBeResolvedByDroppingOneSide`.
11. `Aggregation != Adjudication`.
12. `NoObservation != NegativeObservation`.
13. `NoMatch != NoCapability`.
14. `AbsenceToNegationRequiresClosureWitness`.
15. `ProjectionRefinementIsObservationAndTimeRelative`.
16. `EqualView != EquivalentProjection`.
17. `IdentityTransitionIsRoleRelative`.
18. `RecoveryMayPreserveIdentityWithoutPreservingStanding`.
19. `Rebinding != ContinuityPreservation`.
20. `StandingPromotionRequiresWitness`.
21. `SameClaimLineageRequiredForTemporalSupersession`.
22. `GenerationChangeMayMigrateClaimInsteadOfSupersedingValue`.

These are provisional derived-theory laws, not numbered Network Foundations.
