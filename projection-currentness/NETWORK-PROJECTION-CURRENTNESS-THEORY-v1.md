# Ordivon Network Projection & Currentness Theory v1

Status: FROZEN DERIVED THEORY at the current evidence frontier

Upstream authorities:

- frozen `NCT_v1=<K,Π,H;J>_Γ`;
- frozen Network Capability Calculus v1.

This theory owns Network-facing projection, evidence-currentness, adequacy, identity/binding currentness and standing-bridge semantics. It does not own underlying source reality, generic epistemology/statistics, Host continuity, Research authority, Harness selection or Runtime execution/effect truth.

## 1. Projection carrier

A projection family is:

`Φ=<SubjectRole,SourceRole,ProjectionSchema,TruthRole,OwnerBoundary>`.

A concrete projection instance is:

`π=<pid,Φ,scope,sourceRef,relationWitness,view,provenance,effectiveScope,producedAt>`.

Projection values are grounded representations, not source truth generators.

`ProjectionRepresentation != SourceTruth`.

Truth roles remain typed and distinct:

`SourceΠ != ObservationΠ != InferenceΠ != BeliefΠ != HistoricalΠ`.

## 2. Claim identity

Evidence comparison starts from a typed claim key:

`ck=<subjectRole,subjectIdentity,claimRole,scopeCut,lineageRole,contractVersion,effectiveDomain>`.

A **claim epoch** `ε(ck)` is the maximal interval/version/generation/binding lineage within which the claim identity and supersession semantics remain stable enough for same-claim comparison.

Generation/path/version/binding transitions may end one epoch and begin another.

`SameLabel != SameClaim`.

`SameClaim != SameClaimEpoch` when an admitted migration changes identity semantics.

## 3. Evidence carrier

`e=<eid,ck,truthRole,authorityRole,sourceRef,value,effectiveScope,producedAt,provenance>`.

Evidence identity is immutable.

`EvidenceRevision != EvidenceMutation`.

Correction creates a new evidence object plus a correction/supersession relation; history is retained.

## 4. Claim-local authority policy

No universal authority lattice is admitted.

Each claim role resolves authority through a typed policy:

`AP_Γ(ck)=<claimOwner,admissibleAuthorityRoles,comparisonRules,supersessionRules,correctionRules,migrationRules>`.

`AuthorityCompatible_Γ(e1,e2|ck)` is evaluated only under AP for that claim role/scope.

Authority relationships may therefore differ across:

- health;
- identity;
- binding;
- capability verification;
- serviceability;
- imported Security/Normative/World facts;
- externally owned Host/Runtime/Harness claims.

Canonical laws:

`AuthorityCompatibilityIsClaimLocal`.

`AuthorityRankDoesNotGlobalize`.

`ProjectionCannotAdjudicateBeyondClaimOwnerPolicy`.

## 5. Evidence comparability

`Comparable_Γ(e1,e2|ck,τ)` requires:

1. equal claim key/epoch, or an explicit comparison/migration witness accepted by AP;
2. compatible truth roles for the target judgement;
3. overlapping/equated effective scope for the target query;
4. compatible lineage identity;
5. authority roles admitted by AP.

Different claim roles/scopes/epochs may coexist without conflict.

`DifferentScope != Conflict`.

`DifferentRole != Conflict`.

`DifferentEpoch != SameClaimConflict` by default.

## 6. Supersession within one claim epoch

For one claim epoch ε:

`e2 ▷_{Γ,ck,ε} e1`

iff AP admits e2 as replacing e1 for the current target query while preserving same-claim lineage.

Supersession requires comparable evidence, admitted authority/correction semantics, effective-scope precedence and stable claim identity.

### Epoch-local supersession theorem

If AP's precedence/correction relation is irreflexive and transitive for ε, claim identity is unchanged, and effective-scope precedence composes consistently, then `▷` is a strict partial order within ε.

Therefore it is acyclic.

Cross-epoch migration edges are **not supersession edges** and do not participate in this transitivity theorem.

Canonical laws:

`SupersessionIsEpochLocal`.

`SupersessionTransitivityStopsAtMigration`.

`Migration != Supersession`.

`NewerTimestamp != Supersession`.

`Supersession != Erasure`.

## 7. Migration graph

Claim transitions are explicit:

`MigrateClaim_Γ(ck_0,h,w)=>ck_1`.

Examples:

- generation G1 -> G2;
- path P1 -> P2;
- binding A -> B;
- K contract v1 -> v2;
- identity granularity any-provider -> exact-instance/session.

Migration relates claim epochs but does not automatically transport standing/evidence truth.

`MigrationDoesNotCarryStandingByDefault`.

`CrossEpochSplicingForbidden`.

Evidence from ε0 can be reused under ε1 only through an explicit transport/migration witness specifying which predicates survive.

## 8. Evidence frontier

For a target `(ck,ε,τ)` let A be the admissible evidence set after claim/authority/scope/truth-role filtering.

`Frontier_Γ(ck,ε,τ)=Max_▷(A)`.

### Frontier determinacy theorem

If A is finite, or more generally every admissible chain has a maximal element sufficient for the query, and `▷` is a strict partial order, then the maximal frontier set is unique and independent of evidence input order.

For live streams, the theorem applies to an explicit query cutoff/materialized snapshot or another structure satisfying the maximality condition.

An infinite strictly ascending evidence chain with no maximal element is outside this theorem and must not be misclassified as an empty/UNKNOWN frontier merely because `Max` is absent.

Canonical laws:

`CurrentView != LatestRecord`.

`FrontierDeterminacyRequiresMaximalityCondition`.

`InputOrderDoesNotDetermineFrontier`.

## 9. Conflict preservation

For maximal evidence objects in the frontier:

`Conflict_Γ(e1,e2|ck,ε,τ)`

holds when they are comparable/currently admissible for the same claim and support incompatible standings while neither supersedes the other.

Under deterministic AP/comparison/conflict rules, conflict detection over the unique frontier is itself input-order independent.

`ComposeEvidence` returns:

`<Frontier,ConflictSet,HistoricalSet,DerivationLedger>`.

Canonical laws:

`ConflictCannotBeResolvedByDroppingOneSide`.

`Aggregation != Adjudication`.

`ConflictPreservationIsFrontierInvariant`.

## 10. Currentness judgement

Currentness remains role/scope/time/evidence/history indexed:

`Current_Γ(x|role,scope,τ,E,H)=>c`.

Evidence-currentness standings include typed values such as:

- CURRENT;
- STALE;
- UNKNOWN;
- CONFLICTED;
- NOT_CURRENT;
- NOT_APPLICABLE.

These are orthogonal to domain values such as AVAILABLE/UNAVAILABLE/REACHABLE/SERVICEABLE.

`Currentness != PositiveStanding`.

`Unavailable != Unknown != Stale != False`.

`StatusStringEquality != SemanticRoleEquality`.

## 11. Absence and negative claims

Open-world absence remains non-negative by default:

`NoObservation != NegativeObservation`.

`NoMatch != NoCapability`.

A negative existential conclusion from absence requires:

`Complete_Γ(π|query,cut,τ)`

or another owner-provided explicit negative proof.

`AbsenceToNegationRequiresClosureWitness`.

A current authoritative negative observation is different from absence and may directly support a negative domain standing if its owner semantics admits that interpretation.

## 12. Conservative projection refinement

For fixed `(Γ,Ω,targetJ,τ,ε)`:

`π2 ⪰^c π1`

iff π2 preserves every distinction required by targetJ/Ω, including:

- subject/source role;
- effective scope/time semantics;
- truth role/provenance;
- identity/lineage mapping;
- dependency/support distinctions;
- existing conflicts;
- all target-J bridge predicates.

### Adequacy preservation theorem

If:

`Adequate_Γ(π1|targetJ,Ω,τ,ε)`

and

`π2 ⪰^c π1`

then:

`Adequate_Γ(π2|targetJ,Ω,τ,ε)`.

The theorem requires the **same judgement target, observation signature, claim epoch and target time**.

Changing targetJ/Ω/time/epoch is a new adequacy question, not a counterexample.

Canonical laws:

`AdequacyPreservationRequiresFixedTarget`.

`ProjectionRefinementIsObservationAndTimeRelative`.

## 13. Projection refinement vs evidence update

A conservative projection refinement is a better/compatible representation of the same relevant source/evidence standing for the fixed target.

An **evidence update** introduces new evidence, new effective scope, new identity epoch, new conflict or new source facts.

These are different operations.

`ProjectionRefinement != EvidenceUpdate`.

A projection refinement may preserve an existing standing derivation; an evidence update may legitimately invalidate it.

`MoreInformationFromSameStanding != NewStandingEvidence`.

## 14. Projection equivalence

`π1 ≈_{Γ,Ω,targetJ,τ,ε} π2`

when they mutually conservatively refine each other or an explicit abstraction witness proves target-relative indistinguishability while preserving all required provenance/currentness distinctions.

`EqualView != EquivalentProjection`.

`EquivalentProjection != SameSource`.

## 15. Identity and binding transitions

Identity transition:

`TransitionId_Γ(x0,h,x1|ι)=>{PRESERVED,REPLACED,SPLIT,MERGED,INVALIDATED,UNKNOWN}`.

Binding transition:

`TransitionBind_Γ(b0,h,b1|χ)=>{PRESERVED,REBIND_EQUIVALENT,REBIND_NON_EQUIVALENT,STALE,INVALIDATED,UNKNOWN}`.

Canonical laws:

`IdentityTransitionIsRoleRelative`.

`RecoveryMayPreserveIdentityWithoutPreservingStanding`.

`Rebinding != ContinuityPreservation`.

`NominalEquality != IdentityContinuity`.

## 16. Standing bridge graph

Keep distinct:

- `ClaimMatch`;
- `VerifiedCapability`;
- `Reachability`;
- `Serviceability`.

Each promotion requires typed bridge evidence/history/contract predicates.

`ClaimMatch ⇏ VerifiedCapability`.

`VerifiedCapability ⇏ Reachable`.

`Reachable ⇏ Serviceable`.

`StandingPromotionRequiresWitness`.

### Bridge-stability theorem under conservative refinement

Suppose a standing derivation D for target J uses bridge witnesses W over projection π1, fixed K, claim epoch ε and target time τ.

If π2 conservatively refines π1 and explicitly preserves every W predicate/identity/provenance distinction used by D, while K/ε/τ remain unchanged, then D transports to π2.

This does **not** apply when:

- new evidence changes the frontier;
- K demand changes;
- identity epoch migrates;
- target time advances past freshness/deadline validity;
- a new conflict invalidates a witness.

Canonical laws:

`StandingDerivationIsSnapshotRelative`.

`ServiceabilityTransportRequiresStablePremises`.

`EvidenceUpdateMayInvalidateStanding`.

## 17. Multi-generation historical retention

For epochs:

`ε1 --m12--> ε2 --m23--> ε3`

retain evidence sets independently:

`E_ε1`, `E_ε2`, `E_ε3`.

The current frontier for ε3 cannot directly combine values/witnesses from ε1 or ε2 unless migration transport explicitly carries those predicates forward.

Historical evidence remains queryable under its original epoch/effective scope.

Canonical laws:

`HistoricalRetention != CurrentAdmissibility`.

`CrossEpochSplicingForbidden`.

`RecoveredStanding != RetroactiveStanding`.

`Recovery != HistoryReset`.

## 18. Workstation closure evidence

Current read-only observations during Round 3 remain consistent with the theory:

- `surf-clash`: current observation, stable current generation/capability digests, domain status UNAVAILABLE and unhealthy operational projections;
- `finance-okx`: stable profile/authority identity, two configured members, but current domain status UNKNOWN with no eligible/active member and inactive/unreachable listener/service.

Historical tests additionally establish:

- newer admission fence may temporarily supersede older watchdog evidence for the same generation/path health claim;
- newer watchdog evidence then becomes current for that same claim;
- stale fence is not rescued by older watchdog evidence;
- transient red health may preserve exact parent identity;
- exact-path recovery/backoff may preserve identity while admission fails closed;
- generation/path change invalidates the prior exact identity epoch.

This is direct pressure for epoch-local supersession, role-specific identity, frontier semantics and migration separation.

No network mutation was performed.

## 19. Cross-owner recovery pressure

An old Network research Task may remain currently READY as a Host continuity fact while later semantic owner authority classifies it as historical/not-current for recovery.

These are distinct claim roles/keys, not conflicting values of one claim.

`CrossRoleCurrentnessNeedNotAgree`.

`ProjectedForeignCurrentness != NetworkAuthority`.

## 20. Owner membrane

Network Projection & Currentness Theory imports rather than owns:

- World/Physics/domain source truth;
- generic probability/statistics/epistemology;
- Normative/Security authority/legitimacy/trust semantics;
- Host task continuity;
- Research System authority/current-recovery decisions;
- Harness selection/invocation;
- Runtime execution/effect truth.

Claim-local AP may reference those owner rules opaquely without recreating them.

`ProjectionOfExternalTruth != OwnershipTransfer`.

## 21. Closure status

Network Projection & Currentness Theory v1 is FROZEN at the current evidence frontier.

Freeze is justified because:

- projection family/instance and truth-role separation survives;
- role-indexed currentness survives real negative-current observations;
- claim-local authority replaces the rejected universal authority lattice;
- epoch-local supersession forms a strict partial order under explicit owner-policy side conditions;
- evidence-frontier determinacy and conflict preservation hold on finite/maximality-satisfying query snapshots;
- migration is separated from supersession and prevents cross-generation evidence splicing;
- conservative projection refinement preserves adequacy for fixed targets;
- standing derivations transport only under conservative refinement with stable premises;
- evidence updates/currentness changes may invalidate standing without contradicting refinement theorems;
- Workstation and stale-ready recovery pressure fit without owner leakage;
- no NCT v1, Capability Calculus v1 or NDF FoundationReopenCondition fired.

This is strong provisional derived-theory closure, not machine-checked universal proof, generic epistemic completeness or external academic novelty claim.

## 22. Projection & Currentness Reopen Conditions

Reopen v1 if a concrete case establishes one of:

1. a Network-facing projection/currentness responsibility not representable by typed projection, claim, evidence, authority policy, frontier, transition and bridge structures;
2. a claim role requiring one universal authority lattice across unrelated owners to remain coherent;
3. a same-epoch supersession cycle satisfying all stated owner-policy conditions;
4. a finite/maximality-satisfying evidence set whose frontier depends on input order;
5. a valid current conflict erased by the frontier construction under the stated rules;
6. a conservative refinement satisfying all stated fixed-target conditions that destroys prior adequacy;
7. a standing derivation satisfying all stable-premise/refinement conditions that fails to transport;
8. a sound current capability/serviceability proof requiring un-witnessed cross-epoch evidence splicing;
9. absence in an open-world projection soundly proving negation without a completeness/negative witness;
10. an upstream NCT/Capability Calculus/NDF reopen condition.

No such condition is currently established.
