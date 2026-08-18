# Network Projection & Currentness Theory — Round 2
## Projection Calculus and Currentness Algebra

Status: COMPLETE / CALCULUS v0 SURVIVES

## 1. Claim-key tournament

### Candidate mistake

Compare evidence by subject string plus timestamp.

### Counterexample

`surf-clash` under stable profile identity, exact generation identity, health role and serviceability role can produce different legitimate currentness relations. A generation change means a later record may refer to a **different exact claim identity**, not a newer value of the same claim.

### Result

Evidence comparison requires a typed claim key:

`ck=<subjectRole,subjectIdentity,claimRole,scopeCut,lineageRole,contractVersion,effectiveDomain>`.

`SameLabel != SameClaim`.

## 2. Supersession tournament

### Workstation matched case

Historical `test_newer_admission_fence_overrides_older_red_watchdog_cache_only_until_watchdog_catches_up` shows:

1. newer admission-fence evidence can outrank older red watchdog evidence for the same generation/path health claim;
2. once watchdog evidence becomes newer for that same claim, watchdog becomes the current evidence source;
3. reaching the watchdog failure threshold changes the admissible health judgement.

`test_stale_admission_fence_is_superseded_by_newer_fresh_watchdog` confirms a stale fence can be superseded by newer fresh watchdog evidence.

`test_stale_admission_fence_fails_when_watchdog_has_not_caught_up` shows an older watchdog cannot rescue a stale fence merely because it exists.

### Result

Supersession is a claim/authority/lineage/effective-scope relation, not latest timestamp selection.

`e2 ▷_{Γ,ck} e1` is partial, not total.

`CurrentView != LatestRecord`.

## 3. Evidence frontier

A current claim is evaluated over the set of non-superseded admissible evidence:

`Frontier_Γ(ck,τ)=Max_▷(A)`.

This yields a clean interpretation:

- no frontier evidence -> UNKNOWN unless closure/negative proof exists;
- compatible adequate maxima -> CURRENT evidence standing;
- incompatible maxima -> CONFLICTED;
- only out-of-scope/expired evidence -> STALE;
- positive lineage-invalidating evidence -> NOT_CURRENT.

This avoids both last-write-wins and destructive conflict resolution.

## 4. Conflict-preserving composition

### Attack

Suppose two current admissible sources disagree. Aggregating them into one boolean or choosing an arbitrary winner hides provenance and can turn conflict into false certainty.

### Result

`ComposeEvidence` returns frontier + conflicts + history + derivation ledger.

`ConflictCannotBeResolvedByDroppingOneSide`.

`Aggregation != Adjudication`.

Authority resolution belongs to the claim owner/adjudication owner, not to projection aggregation itself.

## 5. Absence-to-negation attack

### Discovery pressure

Workstation discovery tests explicitly preserve the distinction between candidate discovery and admission/current effect authority. Search or registry candidates remain non-admissible and require owner revalidation.

An empty discovery result in an open-world search therefore cannot imply `NoProvider(P)`.

### Result

`NoObservation != NegativeObservation`.

`NoMatch != NoCapability`.

Negative existential inference requires `Complete_Γ(π|query,cut,τ)` or another explicit proof.

`AbsenceToNegationRequiresClosureWitness`.

## 6. Projection refinement/equivalence tournament

Round 1 rejected detail-count monotonicity. Round 2 defines conservative refinement relative to fixed Γ/Ω/targetJ/time.

A refinement must preserve all prior Ω-observable distinctions, provenance/truth role, source compatibility, effective-time semantics, identity mapping and conflicts.

Candidate adequacy theorem:

`Adequate(π1) ∧ π2 ⪰^c π1 => Adequate(π2)`.

Equivalence is target-relative mutual conservative refinement or a justified abstraction witness:

`π1 ≈_{Γ,Ω,targetJ,τ} π2`.

### Verdict

SURVIVES as partial typed relation.

`EqualView != EquivalentProjection`.

## 7. Identity/currentness transition tournament

Historical Workstation tests show:

- transient health red can leave exact parent identity current;
- generation change makes that identity not current;
- transient namespace registration gap need not destroy the same parent identity;
- exact-path recovery/backoff can preserve child/parent identity while admission fails closed;
- changing parent path invalidates exact identity.

Therefore identity transitions are role-indexed:

`TransitionId(x0,h,x1|ι)`.

### Result

`RecoveryMayPreserveIdentityWithoutPreservingStanding`.

`IdentityTransitionIsRoleRelative`.

## 8. Binding transition tournament

Rebinding must distinguish:

- broad any-provider/equivalence continuity;
- exact instance continuity;
- exact session/association continuity;
- generation/path binding.

The same A->B rebind may preserve one continuity role and invalidate another.

### Result

`Rebinding != ContinuityPreservation`.

Binding currentness is a claim key and transition relation, not a raw locator equality test.

## 9. ClaimMatch -> VerifiedCapability -> Reachability -> Serviceability tournament

### Workstation discovery evidence

Historical discovery tests explicitly enforce:

- implementation/search candidates are not admission authority;
- primary/operator sources may identify an owner/provider but still require final revalidation;
- structured IANA/BGP-style sources are discovery/registry/routing clues, not live routing/admission truth;
- validation memory can reweight ranking without authorizing effects.

This is a direct engineering manifestation of:

`ClaimMatch ⇏ VerifiedCapability`.

### Further separations

A verified capability may be currently unreachable.

A reachable transport endpoint may not satisfy application/service K requirements.

A serviceable Network capability may still be rejected by Runtime admission.

### Result

Standing is a bridge graph, not an ordinal ladder. Every promotion requires typed evidence/history/contract witnesses.

`StandingPromotionRequiresWitness`.

## 10. Stale-ready cross-owner dogfood

Old Network open-exploration remains a current Host READY continuity fact, while later Network owner authority and Research-System recovery classify it as historical/not-current for semantic recovery.

This maps naturally to two different claim keys/roles rather than one contradictory status:

- `ck_host_continuity`;
- `ck_semantic_recovery_authority`.

Because the claim roles differ, the observations coexist rather than conflict.

This directly supports:

`DifferentRole != Conflict`.

`CrossRoleCurrentnessNeedNotAgree`.

Network does not own either external currentness semantics.

## 11. Migration vs supersession

A generation/path change is not best described as “new evidence says old generation false”. It creates a new exact-generation claim identity while evidence for the previous generation becomes historical/not-current for the present role.

Similarly, K contract migration or rebinding may migrate claim keys.

### Result

`Migration != Supersession`.

`GenerationChangeMayMigrateClaimInsteadOfSupersedingValue`.

This preserves history and prevents evidence from different identity epochs being spliced.

## 12. Round-2 verdict

Projection Calculus + Currentness Algebra v0 survives with:

- typed claim keys;
- immutable evidence identities;
- partial comparability;
- claim-relative supersession partial order;
- evidence-frontier semantics;
- conflict-preserving composition;
- coverage-witnessed absence-to-negation;
- conservative projection refinement/equivalence;
- typed identity/binding transitions;
- bridge-witnessed ClaimMatch/VerifiedCapability/Reachability/Serviceability graph;
- migration separated from supersession.

No NCT v1, Capability Calculus v1 or NDF reopen condition fires.

## 13. Round-3 frontier

The next step should be theorem/closure pressure:

1. define authority-role compatibility without inventing a universal authority lattice;
2. prove/falsify transitivity and acyclicity conditions for supersession under claim migration;
3. formalize evidence-frontier determinacy and conflict preservation;
4. prove/falsify conservative refinement adequacy preservation;
5. formalize bridge composition and determine when serviceability derivations are stable under projection refinement;
6. test historical retention/currentness under recovery and multi-generation churn;
7. decide FREEZE / REPAIR / REJECT Projection & Currentness Theory v1.
