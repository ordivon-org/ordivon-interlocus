# Ordivon Network Operational Realization Theory v1

Status: FROZEN DERIVED THEORY at the current evidence frontier

Upstream authorities:

- frozen `NCT_v1=<K,Π,H;J>_Γ`;
- frozen Network Capability Calculus v1;
- frozen Network Projection & Currentness Theory v1.

This theory owns Network-facing realization-history structure over H. It does not own Harness intent/selection, Runtime Operation/Attempt/execution/effect truth, Host continuity, World causality, generic process/concurrency mathematics, or K/Π/J semantics.

## 1. Realization carrier

A Network realization event is:

`η=<eid,eventRole,subjectRole,subjectIdentity,ownerRole,epoch,preRefs,postRefs,resourceDelta,timeEnvelope,bridgeRefs,provenance>`.

A realization history is:

`H=<hid,V,≺c,≺d,#,Λ,B,T,P>`

with immutable events, causal precedence, support/dependency precedence, branch/conflict relations, identity/epoch lineage, branch/cohort annotations, temporal constraints and provenance/owner-bridge ledger.

For a finite materialized history, causal precedence is acyclic.

`StateRevisit != HistoricalCycle`.

`SerializationOrder != CausalOrder`.

`TemporalPrecedence != Causality`.

## 2. Event-owner membrane

Keep distinct:

`Proposal != Admission != Attempt != NetworkOccurrence != ExternalEffect != NetworkOutcome != Evidence != Satisfaction`.

Foreign-owner events enter only by typed bridge reference plus an explicit bridge rule.

`ForeignEventReference != NetworkOwnership`.

`RuntimeAttempt != NetworkRealizationByIdentity`.

`RuntimeReceipt != NetworkOutcomeByIdentity`.

## 3. History observation signature

Define:

`Ω_H=<BoundaryEventRoles,IdentityRoles,CausalVisibility,DependencyVisibility,BranchVisibility,ResourceVisibility,TemporalVisibility,ProvenanceVisibility,ForeignBridgeVisibility,OutcomeRoles,ContinuationSurface>`.

`ContinuationSurface` declares which open event/identity/resource/branch/epoch interfaces a future admissible continuation may attach to.

This addition is necessary because a history summary may preserve all current observations yet still be non-equivalent if it removes a future continuation attachment point.

Canonical laws:

`CurrentObservability != FutureComposability`.

`AbstractionClosureRequiresContinuationSurface`.

## 4. Contextual history equivalence

`H1 ≃_{Γ,Ω_H} H2`

iff no `Ω_H`-admissible Network continuation can distinguish H1 and H2 on allowed outcomes/judgements/composability.

Equivalence preserves the `Ω_H`-visible closure of:

- external event roles/outcomes;
- causal reachability;
- dependency/support;
- identity/epoch/migration lineage;
- branch/conflict/cancellation/quiescence;
- resource residuals;
- temporal constraints/residuals;
- provenance/foreign-owner receipts;
- future continuation surface.

`EqualTerminalState != EquivalentHistory`.

`SameSerializedLog != EquivalentHistory`.

`EquivalentHistory != SameOccurrenceSet`.

`HistoryEquivalenceIsObservationRelative`.

## 5. Hiding / abstraction

`Hide_H(S,H,Ω_H)` is admissible only with an abstraction witness preserving all required current and future boundary consequences.

If `a ≺c x ≺c b` and x is hidden, external causal reachability `a ≺c* b` must remain if observable or continuation-relevant.

Hidden shared dependencies/resources may not be converted into independence.

`HistoryHiding != EventErasure`.

`InternalEventHiding != CausalReachabilityErasure`.

`InternalDependencyHiding != IndependenceProof`.

`NormalizationRequiresCausalClosure`.

## 6. History composition

`ComposeH_Γ({H_i},W_h)=>H_res`

is partial graph composition under explicit gluing witness `W_h` covering:

- event identity equality/distinctness;
- subject/lineage continuity;
- causal/dependency edges;
- resource handoff/transformation;
- branch/conflict/cancellation semantics;
- contract/claim epoch migration;
- foreign-owner bridge admissibility;
- provenance and continuation-surface transport.

`HistoryComposition != LogConcatenation`.

`ConcatenableLogs != ComposableRealizations`.

## 7. Conditional history associativity theorem

For a finite acyclic global realization graph G, let P1 and P2 be two bracketed factorizations of G.

If:

1. event identities/gluing are the same modulo admitted alpha-renaming;
2. causal and dependency closure are identical;
3. resource transformations/residuals are equal or confluent;
4. branch/conflict/cancellation/quiescence semantics are unchanged;
5. migration/epoch boundaries are unchanged;
6. foreign-owner bridge roles/receipts are preserved;
7. no early hiding removes an `Ω_H`-visible distinction or continuation attachment point;
8. boundary outcomes/provenance/continuation surfaces are equal;

then:

`P1(G) ≃_{Γ,Ω_H} P2(G)`.

This is the **Conditional History Associativity Theorem** for the finite acyclic fixed-global-history fragment.

Unconditional associativity is rejected.

`HistoryAssociativityIsConditional`.

## 8. Structural identities

An empty/open history graph may be identity for disjoint graph union when it contributes no event/time/dependency/resource/provenance effect.

A boundary identity map may preserve an open continuation surface without adding an occurrence.

WAIT/NO-OP/probe/heartbeat/retry are not identities when they have event identity, consume time/resources, create evidence or change standing.

`HistoryIdentityIsStructural`.

`NoOpOccurrence != HistoryIdentity`.

`Wait != HistoryIdentity`.

## 9. Concurrency and bounded independence

For events a,b:

`CausallyUnordered(a,b)` means neither causally precedes the other in the known H graph.

`ConcurrentPossible(a,b)` additionally requires compatible branch/time/conflict constraints.

Independence is stronger and target-relative.

Define an independence witness:

`IW_Γ(a,b|Σ,Ω_H)=<dependencyCut,resourceCut,authorityCut,lineageCut,coverageWitness>`

where Σ is the relevant support/observation cut and `coverageWitness` states that the cut is adequate for the named independence judgement.

`Independent_Γ(a,b|Σ,Ω_H)` holds only when IW establishes no coupling relevant to Ω_H across dependency, consumable/exclusive resource, authority/control or lineage dimensions.

Canonical laws:

`NoCausalEdge != Independence`.

`CausallyUnordered != Independent`.

`ConcurrentPossible != ParallelSafe`.

`IndependenceIsCutRelative`.

### Independence preservation theorem

Independence of a,b is preserved under hiding/composition only if:

- the exported IW remains valid after abstraction;
- no newly composed history introduces a shared dependency/resource/authority/lineage coupling inside the declared cut;
- the coverage witness remains adequate.

Therefore:

`IndependentBeforeComposition != IndependentAfterComposition` by default.

## 10. Branch / race / cancellation / quiescence

Branch realization roles remain distinct:

- never activated;
- activated;
- attempt referenced;
- positive/negative/unknown outcome;
- cancel requested;
- cancel confirmed;
- quiesced;
- loser resolved.

`WinnerKnown != OtherBranchesQuiescent`.

`CancellationRequest != CancellationEffect`.

`Cancelled != NeverStarted`.

`Loser != Failed`.

`RaceResolved != AllBranchesTerminated`.

### Quiescence certificate

A consequential branch is quiescent only under a typed owner/evidence witness:

`Quiescent_Γ(branch|effectScope,τ,E,H)`.

The witness may be supplied by the actual attempt/effect owner and can establish cancellation completion, no further admissible occurrence/effect, or another bounded quiescence condition.

### Race completion rule

For purely observational/non-consequential races, winner resolution may be sufficient for the consumer contract.

For races whose losing branches can cause consequential effects, safe race closeout requires either:

- quiescence certificates for relevant losers; or
- effect reconciliation/deduplication/fencing that makes residual loser uncertainty admissible.

Canonical law:

`ConsequentialRaceCompletionRequiresQuiescenceOrReconciliation`.

## 11. Retry / replay / effect regimes

Keep distinct:

- request identity;
- owner Attempt identity;
- Network occurrence identity;
- external effect identity.

`SameRequest != SameAttempt`.

`SameRequest != SameOccurrence`.

`SameRequestDigest != ExactlyOnceEffect`.

Define prior effect standing for the consequence relevant to the retry decision:

- `KNOWN_NO_EFFECT`;
- `KNOWN_EFFECT`;
- `UNKNOWN_EFFECT`.

These are imported/owner-witnessed effect standings, not Network guesses.

### Retry admissibility

`RetryAdmissible_Γ(prior,goal,K,effectScope,W)` requires:

#### KNOWN_NO_EFFECT

Retry may proceed if K/time/resource/identity constraints still admit it. Known-no-effect does not itself prove current capability.

#### KNOWN_EFFECT

Retry is admissible only when repeating the effect is desired/allowed or a typed idempotency/deduplication/compensation/fencing contract makes repetition safe.

#### UNKNOWN_EFFECT

Unconditional consequential retry is not admitted merely from uncertainty. It requires reconciliation, deduplication/idempotency/fencing, or an explicit policy accepting duplicate-effect risk.

Canonical laws:

`UnknownOutcome != RetryPermission`.

`RetrySafetyRequiresEffectScopeWitness`.

`KnownNoEffect != CurrentRetryCapability`.

`KnownEffect != RetryForbiddenByDefinition`.

`ReplaySemanticsBelongsToOwningContract`.

## 12. Repair / revalidation / failover / recovery / reconciliation

Keep separate:

`Repair != Revalidation != Failover != Recovery != Reconciliation`.

Repair changes support/configuration/binding/resource conditions.

Revalidation acquires/evaluates fresh evidence of standing.

Failover changes active realization lineage.

Recovery establishes an admissible post-failure continuation under explicit identity role and K/J conditions.

Reconciliation resolves ambiguous/divergent effect, identity, currentness or residual-obligation standing without erasing history.

`RepairSucceeded != RecoveryEstablished`.

`Revalidation != Repair`.

`FailoverMayRecoverServiceWithoutPreservingExactIdentity`.

`RecoveryEstablished != RequirementSatisfied`.

`Reconciliation != Undo`.

## 13. Recovery composition theorem

Let:

`R01: x0 --h1--> x1`

and

`R12: x1 --h2--> x2`

be two admitted recovery transitions.

### Identity transport

For a named identity role ι, preservation composes only if:

- R01 preserves ι with witness w01;
- R12 preserves the **same semantic identity role** ι with witness w12;
- w01 and w12 compose across the intermediate epoch/lineage;
- no intervening migration invalidates ι.

Then identity preservation x0->x2 may be derived.

`IdentityPreservationMayComposeWithLineageWitness`.

### Standing transport

Recovered standing does **not** compose from history alone. At the composition boundary and target time, K/Π/J premises must be revalidated.

A second recovery may preserve identity yet current health/serviceability/deadline standing may differ.

`RecoveryChain != SingleRecovery`.

`StandingRecoveryRequiresRevalidationAtCompositionBoundary`.

`IdentityPreservation != StandingPreservation`.

## 14. Failure, partial outcome and reconciliation

`Failure != NoHistory`.

`FailedHistory != EmptyHistory`.

`PartialOutcome != NoOutcome`.

`UnknownOutcome != FailedOutcome`.

A compensation/reconciliation event creates new history rather than deleting the prior event.

`Compensation != Erasure`.

`NetEquivalentState != SameHistory`.

`Reconciliation != HistoryRewrite`.

## 15. Resource / wait / forwarding specializations

Resource transitions remain typed by capability-family usage semantics:

`Δr_η:R_in --[w]--> <R_out,R_residual>`.

`ResourceTransformationRequiresWitness`.

`Transformation != Duplication`.

WAIT/STORE/CARRY remain first-class H:

`Wait != Identity`.

`NoForwardingDuringInterval != NoRealizationHistory`.

Forwarding remains a specialization:

`H_fwd ⊂ H`.

`Reachability != ForwardingOccurrence`.

`ForwardingOccurrence != DeliveryOutcome`.

## 16. Realization Boundary Normal Form

For a finite acyclic history H under fixed `Ω_H` and fixed abstraction/gluing witnesses:

`RBNF_{Γ,Ω_H}(H)=<I_ext,O_ext,C*,D*,Λ*,B*,R_res,T*,P*,Q*,L_hidden>`

where:

- `I_ext` — external incoming/open realization conditions;
- `O_ext` — exposed Network events/outcomes;
- `C*` — external causal reachability closure;
- `D*` — dependency/support closure required by later judgements;
- `Λ*` — identity/epoch/migration lineage summary;
- `B*` — branch/race/cancellation/quiescence summary;
- `R_res` — resource/usage residual;
- `T*` — temporal constraints/residuals;
- `P*` — provenance/foreign-owner bridge summary;
- `Q*` — continuation surface/open attachment summary;
- `L_hidden` — abstraction witness ledger for hidden events.

### RBNF preservation theorem

If:

1. H is finite/acyclic;
2. abstraction preserves all `Ω_H` current observations;
3. causal and dependency closure are retained;
4. identity/epoch lineage and branch/quiescence state are retained;
5. resource/time residuals are retained;
6. provenance/foreign bridge requirements are retained;
7. continuation surface Q* is complete for all `Ω_H`-admissible future composition;

then:

`H ≃_{Γ,Ω_H} RBNF_{Γ,Ω_H}(H)`.

This theorem is observation/continuation-relative. Expanding Ω_H or allowing new attachment points can invalidate an earlier normalization proof.

Canonical laws:

`HistoryNormalFormIsObservationRelative`.

`RBNFRequiresCausalAndProvenanceClosure`.

`RBNFRequiresContinuationClosure`.

`ObservationOrContinuationExpansionMayInvalidateRBNF`.

No universal canonical history normal form is claimed.

## 17. Runtime receipt dogfood

The isolated Round-2 Runtime jobs remain direct owner-boundary witnesses:

- `/usr/bin/true`: Runtime Attempt/execution succeeded, exit 0, durable artifacts/committed delivery, `semanticCompletionEvaluated=false`;
- `/usr/bin/false`: Runtime Attempt/execution failed, exit 1, durable artifacts/committed delivery, `semanticCompletionEvaluated=false`.

Therefore:

`RuntimeExecutionSuccess != NetworkOccurrence`.

`RuntimeExecutionSuccess != SemanticCompletion`.

`RuntimeExecutionFailure != NoHistory`.

A Runtime receipt supports a Network occurrence only through a typed bridge theorem/contract.

## 18. Workstation recovery/race pressure

Historical Workstation tests remain compatible with v1:

- sticky failover preserves lineage rather than recomputing historylessly;
- lastRace retains information beyond current winner;
- winner resolution does not logically prove loser quiescence;
- same-path recovery/backoff may preserve identity while standing is UNAVAILABLE;
- recovery eligibility depends on failure class;
- stale runtime is reconciled before fresh start;
- stable boundary authority persists while active lease/realization changes.

No production/network mutation is required for v1 closure.

## 19. Owner membrane

Operational Realization Theory imports rather than owns:

- Harness selection/invocation intent;
- Runtime Operation/Attempt/execution/effect semantics;
- World/Physics physical causality and external effects;
- Projection/Currentness evidence authority;
- Capability Calculus contract/requirement semantics;
- Host continuity;
- Normative/Security legitimacy/trust predicates;
- generic concurrency/process mathematics.

`BridgeEvent != ImportedOntology`.

`ComposedHistory != OwnerMerge`.

## 20. Closure status

Network Operational Realization Theory v1 is FROZEN at the current evidence frontier.

Freeze is justified because:

- typed partial-order realization history survives hostile regimes;
- owner separation across proposal/attempt/occurrence/effect/outcome/evidence survives live Runtime dogfood;
- history equivalence and RBNF preservation are explicit observation+continuation-relative theorems;
- conditional history associativity survives on finite acyclic fixed-global histories;
- independence requires positive cut-relative witness and does not arise from missing order edges;
- race closeout distinguishes winner resolution from loser quiescence and consequential effect uncertainty;
- retry admissibility is typed by effect knowledge and owner-provided effect-scope witnesses;
- repair/revalidation/failover/recovery/reconciliation remain distinct;
- recovery identity composition is lineage-qualified while standing requires boundary revalidation;
- failure/compensation/recovery preserve history rather than rewriting it;
- no NCT v1, Capability Calculus v1, Projection & Currentness v1 or NDF reopen condition fired.

This is strong provisional derived-theory closure, not a machine-checked universal process algebra, global causal model, generic exactly-once theory, or external novelty claim.

## 21. Operational Realization Reopen Conditions

Reopen v1 if a concrete case establishes one of:

1. a Network-owned realization responsibility not representable by typed events/history graph, bridge refs and K/Π/J interfaces;
2. a finite acyclic history satisfying all RBNF closure conditions whose admissible continuation/outcome differs after normalization;
3. two factorizations satisfying all stated conditional associativity side conditions but yielding distinguishable histories;
4. a valid independence judgement derivable from causal unorderedness alone without dependency/resource/authority/lineage coverage;
5. a consequential race that can safely close with unresolved effectful losers without quiescence/reconciliation/effect-scope protection;
6. an unknown consequential effect that universally licenses safe retry without owner/effect-scope witness;
7. chained recovery standing that transports without K/Π/J revalidation despite changed target time/evidence/requirements;
8. a Runtime/Harness/World fact that must become Network-owned execution/control/effect ontology for H to remain coherent;
9. an upstream NCT/Capability/Projection/NDF reopen condition.

No such condition is currently established.
