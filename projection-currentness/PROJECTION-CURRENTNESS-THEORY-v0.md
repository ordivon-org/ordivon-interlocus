# Ordivon Network Projection & Currentness Theory v0

Status: PROVISIONAL DERIVED THEORY / ROUND-1 SURVIVOR

Upstream authority:

- frozen `NCT_v1=<K,Π,H;J>_Γ`;
- frozen Network Capability Calculus v1.

## 1. Projection family and projection instance

A projection family is a typed schema:

`Φ = <SubjectRole, SourceRole, ProjectionSchema, TruthRole, OwnerBoundary>`

A concrete projection instance is:

`π = <pid, Φ, scope, sourceRef, relationWitness, view, provenance, effectiveScope, producedAt>`

where:

- `pid` — projection-instance identity;
- `Φ` — projection family/type;
- `scope` — query/cut/principal/time scope used to select the projection;
- `sourceRef` — typed reference to the source reality/evidence/history object being projected;
- `relationWitness` — the declared projection/abstraction relation from source role to view;
- `view` — projected Network-facing value/structure;
- `provenance` — authority, derivation, observation, model and lineage metadata required to interpret the view;
- `effectiveScope` — interval/event/cohort/version scope to which the view semantically applies;
- `producedAt` — production/observation time, which is not by itself the effective time or authority order.

Projection instances do not create source truth.

`ProjectionRepresentation != SourceTruth`.

## 2. Projection truth roles

At minimum keep distinct:

- `SourceΠ` — Network-facing projection directly grounded in authoritative source state/history;
- `ObservationΠ` — observation/evidence-bearing view;
- `InferenceΠ` — model/inference-derived view;
- `BeliefΠ` — consumer/agent belief state;
- `HistoricalΠ` — preserved projection whose effective/current role is explicitly historical;
- `CounterfactualΠ` — optional analytical projection not asserting actual current standing.

Canonical separation:

`SourceΠ != ObservationΠ != InferenceΠ != BeliefΠ != HistoricalΠ`.

No truth-role lift is automatic.

## 3. Currentness is a judgement, not a field

Canonical form:

`Current_Γ(x | role, scope, τ, E, H) => c`

where currentness standing `c` is one of a typed family such as:

- `CURRENT` — adequate evidence/history supports that x is current for the named role/scope;
- `STALE` — x/evidence was applicable but no longer satisfies the named currentness condition;
- `UNKNOWN` — available evidence is insufficient to decide the named currentness condition;
- `CONFLICTED` — currently admissible evidence/projections support incompatible standings that are not yet resolved by authority/supersession rules;
- `NOT_CURRENT` — adequate evidence establishes that the named identity/binding/version/role is no longer current;
- `NOT_APPLICABLE` — currentness role does not apply under the declared scope/cut.

These are **currentness/evidential standings**, not domain capability/service values.

A projection may be `CURRENT` while its domain value is `UNAVAILABLE`, `FAILED`, `NO_ELIGIBLE_MEMBER`, or another negative operational standing.

Canonical law:

`Currentness != PositiveStanding`.

## 4. Domain standing is orthogonal to evidence currentness

Define:

`Value_Γ(π | role) = v`

and separately:

`Current_Γ(π | role,scope,τ,E,H) = c`.

Examples:

- current observation + `v=UNAVAILABLE`;
- current observation + `v=UNKNOWN` at the capability domain layer;
- stale observation + historically `v=AVAILABLE`;
- current evidence proving `v=UNAVAILABLE`.

Therefore:

`CurrentNegativeEvidence != StaleEvidence`.

`UnknownCapabilityStanding != StaleObservation`.

`Unavailable != Unknown != Stale != False`.

Semantic falsehood/impossibility remains a separate J/source claim requiring an adequate proof/witness.

## 5. Evidence object and evidence relation

Use a typed evidence object:

`e = <eid, owner, claimRole, subject, scope, effectiveScope, observedAt, producedAt, payloadRef, provenance, authorityRole>`

Evidence does not carry universal scalar trust/freshness.

### Freshness

`Fresh_Γ(e | claimRole, scope, τ, H)`

is role/scope/history relative.

### Supersession

`e2 ▷_Γ e1`

only if an explicit authority/lineage rule shows e2 supersedes e1 for the same or intentionally migrated claim role/scope.

A later timestamp alone is insufficient.

Canonical laws:

`NewerTimestamp != StrongerAuthority`.

`NewerEvidence != AutomaticSupersession`.

`Supersession != Erasure`.

Superseded evidence remains valid historical/provenance material where its original effective scope matters.

### Conflict

`Conflict_Γ(e1,e2 | claimKey)`

when both are admissible for comparison and support incompatible values/currentness standings without a valid supersession/authority resolution.

Adding evidence can therefore create conflict.

`EvidenceAccumulationIsNotMonotoneInCertainty`.

## 6. Projection adequacy

`Adequate_Γ(π | targetJ, Ω)`

means π preserves the distinctions/provenance needed by the target judgement under observation signature Ω.

Adequacy is not equivalent to detail count, byte size or field count.

`MoreDetail != MoreAdequate`.

Define a **conservative projection refinement**:

`π2 ⪰_{Γ,Ω} π1`

only when:

1. subject/source role remains compatible;
2. scope/cut is unchanged or explicitly refined without changing the target question;
3. every Ω-observable distinction of π1 is preserved by π2;
4. provenance/truth role is preserved or strengthened without illicit lifting;
5. added distinctions do not invalidate previously assumed equivalence/identity relations;
6. effective/current time semantics are compared at the same target instant/interval.

Then, for a fixed target judgement/time:

`Adequate(π1) ∧ ConservativeRefinement(π2,π1) => Adequate(π2)`

may hold.

But arbitrary added detail is not conservative refinement.

Canonical laws:

`ProjectionDetail != ProjectionRefinement`.

`AdequacyMonotonicityRequiresConservativeRefinement`.

## 7. Projection comparison and incomparability

Two projections may be incomparable because they differ in:

- query/cut;
- source authority;
- effective time;
- truth role;
- model/inference assumptions;
- identity granularity;
- observation signature.

No universal total projection order is admitted.

`ProjectionComparisonIsTypedAndPartial`.

## 8. Identity currentness

Identity standing is role-specific.

Possible roles include:

- stable public capability/profile identity;
- exact provider/member identity;
- generation/path identity;
- binding identity;
- association/session identity;
- cohort/lineage identity.

A stable public identity may remain current while a lease/member/health standing changes.

`StableBoundaryIdentity != CurrentLeaseStanding`.

Conversely, a generation/path change may make exact identity `NOT_CURRENT` even when names/ports remain unchanged.

`NominalEquality != IdentityContinuity`.

## 9. Health, admission, reachability, serviceability

These are distinct J-level projections/judgements, not a single status chain.

Canonical separation:

`IdentityCurrent != HealthCurrent != BindingCurrent != AdmissionStanding != Reachable != Serviceable`.

There is no universal implication chain among all roles without explicit bridge conditions.

Examples:

- identity current + health unavailable;
- binding current + destination health stale;
- reachable + application service not serviceable;
- serviceable Network surface + Runtime operation not admitted;
- historical successful attempt + no current Network serviceability evidence.

`StandingCompositionRequiresBridgeWitness`.

## 10. Recovery and lineage

Recovery is represented by H, while Π/J determine which identities and standings survive across it.

For an object x across histories `h0 -> hrecover -> h1`, identity continuity requires a lineage witness appropriate to the identity role.

Recovery may:

- preserve stable boundary identity;
- change active member/lease identity;
- supersede stale health evidence;
- change admission from closed to open;
- preserve historical failure evidence;
- invalidate exact generation identity.

Canonical laws:

`Recovery != HistoryReset`.

`RecoveredStanding != RetroactiveStanding`.

A capability becoming AVAILABLE again does not mean it was AVAILABLE during the degraded interval.

## 11. Stale semantic route vs live continuity fact

A cross-owner object can be current under one role and historical under another.

Example pattern:

`Current(x | HostContinuityRole) = CURRENT`

while an external semantic owner/Research System determines:

`Current(x | SemanticRecoveryAuthorityRole) = NOT_CURRENT/HISTORICAL`.

Network Projection Theory does not own Host/Research currentness, but the pattern proves currentness must be role-indexed.

Canonical law:

`CrossRoleCurrentnessNeedNotAgree`.

## 12. Source/observation/inference composition

Projection derivation must preserve provenance and truth role:

`Derive_Γ(π1,...,πn, model/witness) => πd`.

The derived projection records:

- all source projection identities/roles needed for replay;
- derivation/model identity;
- effective-scope intersection/combination rule;
- uncertainty/conflict standing where applicable;
- no automatic authority upgrade.

Canonical laws:

`DerivedProjectionAuthority <= DeclaredDerivationAuthority`.

`InferenceDoesNotLiftSourceAuthority`.

`ConflictCannotBeHiddenByAggregation`.

## 13. Round-1 status taxonomy

The theory deliberately separates three dimensions:

### A. Truth role

`Source / Observation / Inference / Belief / Historical / Counterfactual`.

### B. Evidence-currentness standing

`CURRENT / STALE / UNKNOWN / CONFLICTED / NOT_CURRENT / NOT_APPLICABLE`.

### C. Domain value/standing

Domain-specific values such as:

`AVAILABLE / UNAVAILABLE / UNKNOWN / REACHABLE / UNREACHABLE / SERVICEABLE / NOT_SERVICEABLE / CLAIM_MATCH / ...`

The same word `UNKNOWN` may appear in a domain vocabulary and the currentness vocabulary; implementations must type/qualify the role rather than compare raw strings.

Canonical law:

`StatusStringEquality != SemanticRoleEquality`.

## 14. Owner membrane

Projection & Currentness Theory owns Network-facing projection/currentness semantics only.

It imports rather than owns:

- underlying reality/source truth from World/Physics/domain owners;
- Host Task continuity/currentness;
- Research System authority/current-recovery truth;
- Runtime Attempt/execution/effect truth;
- Harness selection/invocation truth;
- Security/Authority legitimacy/trust truth;
- generic statistical inference/calibration/epistemology.

`ProjectionOfExternalTruth != OwnershipTransfer`.

## 15. Round-1 candidate laws

1. `Currentness != PositiveStanding`.
2. `CurrentNegativeEvidence != StaleEvidence`.
3. `UnknownCapabilityStanding != StaleObservation`.
4. `Unavailable != Unknown != Stale != False`.
5. `NewerTimestamp != StrongerAuthority`.
6. `NewerEvidence != AutomaticSupersession`.
7. `Supersession != Erasure`.
8. `EvidenceAccumulationIsNotMonotoneInCertainty`.
9. `MoreDetail != MoreAdequate`.
10. `ProjectionDetail != ProjectionRefinement`.
11. `AdequacyMonotonicityRequiresConservativeRefinement`.
12. `ProjectionComparisonIsTypedAndPartial`.
13. `NominalEquality != IdentityContinuity`.
14. `StandingCompositionRequiresBridgeWitness`.
15. `Recovery != HistoryReset`.
16. `RecoveredStanding != RetroactiveStanding`.
17. `CrossRoleCurrentnessNeedNotAgree`.
18. `InferenceDoesNotLiftSourceAuthority`.
19. `ConflictCannotBeHiddenByAggregation`.
20. `StatusStringEquality != SemanticRoleEquality`.

These are provisional derived-theory laws, not Network Foundations.
