# Network Projection & Currentness Theory — Round 1
## Projection, Currentness and Evidence Destructive Tests

Status: COMPLETE / v0 CANDIDATE SURVIVES

## 1. Boolean-currentness attack

### Counterexample A — Workstation stable identity vs health

The current Workstation `surf-clash` anchor observation has a current generation/capability projection while its current operational status is `UNAVAILABLE`, with namespace/resolver/transport/required-target/service health false.

Therefore a current observation can support a negative domain standing.

### Counterexample B — configured pool vs current live standing

The current `finance-okx` egress observation preserves a stable profile/authority digest and configured member count 2 while reporting `status=UNKNOWN`, `eligibleMembers=[]`, `activeMember=null`, `listenerReachable=false` and inactive service.

Stable boundary identity and configuration therefore coexist with unknown/unavailable live standing.

### Counterexample C — Host continuity vs semantic recovery

The old `task:network-post-foundations-open-exploration-20260818` remains Host `READY` at revision 7, while later Network owner consolidation is completed and Research-System legacy dogfood classifies the old route as historical/not-current for semantic recovery.

The same historical object is current as a Host continuity fact but not current as semantic research authority.

### Verdict

Currentness must be role/scope/time/evidence/history indexed. One Boolean field fails.

`CrossRoleCurrentnessNeedNotAgree`.

## 2. Status-collapse attack

Candidate mistake:

`UNKNOWN < STALE < UNAVAILABLE < FALSE`.

This fails because the words describe different dimensions.

- STALE: evidential/currentness relation;
- UNAVAILABLE: domain operational standing, possibly backed by current evidence;
- UNKNOWN: may be evidential insufficiency or a domain owner status, depending on typed role;
- FALSE/impossible: semantic claim requiring a proof/source witness.

### Verdict

Three-axis status taxonomy required: truth role × evidence-currentness × domain value.

`Unavailable != Unknown != Stale != False`.

## 3. Newer-evidence supersession attack

A later observation should not automatically supersede an older observation if:

- it comes from a weaker/different authority;
- it concerns a different generation/binding/cohort;
- its effective scope differs;
- it is an inference while the older record is authoritative source evidence;
- migration/rebinding rules do not establish claim continuity.

Conversely, authoritative newer health evidence can supersede a stale health/admission fence for the same role/lineage while the old evidence remains historically valid.

### Verdict

`NewerTimestamp != StrongerAuthority`.

`NewerEvidence != AutomaticSupersession`.

`Supersession != Erasure`.

## 4. Evidence accumulation monotonicity attack

Adding evidence can make a previously simple claim harder rather than easier:

- a second current source conflicts with the first;
- new generation evidence shows a previous binding is stale;
- a dependency projection reveals two apparent alternatives share one support path;
- a fresh negative health observation invalidates an older positive inference.

### Verdict

Certainty/current standing is not monotone in evidence count.

`EvidenceAccumulationIsNotMonotoneInCertainty`.

## 5. Projection-detail monotonicity attack

Candidate mistake:

`more fields/detail => more adequate projection`.

Counterexamples:

- additional fields come from a different stale generation;
- finer topology changes the query/cut rather than refining the same projection;
- extra inferred fields are mistaken for source facts;
- added member identity reveals an equivalence assumption was false;
- additional detail omits provenance and makes the view less safely reusable.

### Survivor

Adequacy is monotone only under **conservative projection refinement** preserving subject/source role, target scope, Ω-observable distinctions, provenance and truth-role discipline at a fixed effective time.

`ProjectionDetail != ProjectionRefinement`.

`AdequacyMonotonicityRequiresConservativeRefinement`.

## 6. Identity recovery attack

Workstation history already demonstrates cases where:

- stable public profile/authority identity persists;
- health/admission standing degrades;
- active lease/member may change;
- newer evidence allows recovery;
- generation/path changes invalidate exact identity even if stable names/ports remain.

Therefore identity continuity requires a role-specific lineage witness.

`NominalEquality != IdentityContinuity`.

`Recovery != HistoryReset`.

`RecoveredStanding != RetroactiveStanding`.

## 7. Standing implication attack

Candidate chain:

`IdentityCurrent -> HealthCurrent -> Reachable -> Serviceable`.

This is not universal.

- current identity can be unhealthy;
- current binding can point to an unavailable destination;
- transport reachability can exist while application service is not serviceable;
- Network serviceability does not imply Runtime admission/success.

### Verdict

No universal status chain. Cross-role implication requires typed bridge witnesses.

`StandingCompositionRequiresBridgeWitness`.

## 8. Projection derivation / authority-lift attack

Combining two observations or running a model over them may produce a useful inference, but the inference cannot silently become source authority.

A derived projection must retain source identities, derivation/model identity, effective-scope rule and conflict/uncertainty standing.

### Verdict

`InferenceDoesNotLiftSourceAuthority`.

`ConflictCannotBeHiddenByAggregation`.

## 9. Current Workstation evidence used

Read-only observations during Round 1:

### surf-clash

- current observation returned `status=UNAVAILABLE`;
- current generation and capability digests were present;
- namespace/resolver/transport/required-target/service health were false.

This is the cleanest witness that currentness and positive standing are orthogonal.

### finance-okx

- stable profile/authority digest present;
- configured memberCount=2;
- domain status `UNKNOWN`;
- no eligible members;
- no active member;
- listener unreachable;
- service inactive;
- `no-eligible-member` watchdog disposition.

This supports stable identity vs current lease/service standing separation and typed UNKNOWN semantics.

No network mutation was performed.

## 10. Host/Research cross-owner evidence used

Read-only Host observations:

- old Network open-exploration task: revision 7, state READY, historical pre-repair frontier;
- current Network research consolidation: revision 3, COMPLETED, later semantic owner authority;
- Research-System legacy fixture dogfood: completed and explicitly reports Network stale-ready PASS.

This is not Network ownership of Host/Research currentness. It is a destructive example proving role-indexed currentness and historical projection preservation are required.

## 11. Round-1 verdict

Projection & Currentness Theory v0 survives with:

- typed projection family + instance;
- explicit truth-role separation;
- role/scope/time/evidence/history-indexed currentness;
- orthogonal domain standing vs evidence-currentness;
- typed freshness/supersession/conflict relations;
- conservative projection refinement rather than detail-count monotonicity;
- role-specific identity continuity;
- bridge-witnessed standing composition;
- recovery without history reset;
- provenance-preserving derived projections.

No NCT v1, Capability Calculus v1 or NDF reopen condition fires.

## 12. Round-2 frontier

Next step should develop the actual currentness/projection calculus:

1. formalize claim keys, authority/lineage and supersession partial orders;
2. formalize conflict resolution vs conflict preservation;
3. define evidence/currentness composition across multiple projection sources;
4. define conservative projection refinement and equivalence theorems;
5. define role-specific identity/binding/currentness transition calculus;
6. reconstruct discovery->binding->reachability->serviceability as typed bridge chain without universal implication;
7. dogfood against healthy/degraded/recovered Workstation history and stale-ready research recovery;
8. determine whether a compact `Projection Calculus + Currentness Algebra` v0 survives.
