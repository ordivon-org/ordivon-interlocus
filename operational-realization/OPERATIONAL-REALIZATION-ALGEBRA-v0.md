# Ordivon Network Operational Realization Algebra v0

Status: PROVISIONAL DERIVED THEORY / ROUND-2 SURVIVOR

Upstream authorities:

- frozen `NCT_v1=<K,Π,H;J>_Γ`;
- frozen Network Capability Calculus v1;
- frozen Network Projection & Currentness Theory v1;
- Operational Realization Theory v0.

The surviving structure is a typed partial algebra over realization-history graphs. It is not a universal trace monoid, workflow language, Runtime execution algebra, or total-order event log.

## 1. History observation signature

Define a history observation signature:

`Ω_H=<BoundaryEventRoles,IdentityRoles,CausalVisibility,DependencyVisibility,BranchVisibility,ResourceVisibility,TemporalVisibility,ProvenanceVisibility,ForeignBridgeVisibility,OutcomeRoles>`.

`Ω_H` determines which distinctions an external Network context may observe.

At minimum an observation boundary may care about:

- externally exposed establishment/revocation/binding/forwarding/recovery outcomes;
- identity/lineage transitions;
- causal reachability among exposed events;
- dependency/support relations relevant to later J judgements;
- branch/race resolution and unresolved branch standing;
- usage/resource residuals;
- time/deadline/custody implications;
- provenance and foreign-owner bridge receipts;
- negative/partial/unknown outcomes.

## 2. History contextual equivalence

Two histories are observationally/contextually equivalent when no `Ω_H`-admissible continuation can distinguish them on allowed Network outcomes/judgements:

`H1 ≃_{Γ,Ω_H} H2`.

Equivalence does **not** require identical internal event sets or serialization. Internal events/order may differ when all `Ω_H`-visible consequences are preserved.

However, equivalence must preserve at least the `Ω_H`-visible closure of:

- boundary event roles and outcomes;
- causal reachability;
- dependency/support;
- identity/lineage/epoch transitions;
- branch/conflict/resolution status;
- resource residuals;
- temporal constraints;
- provenance/foreign bridge obligations.

Canonical laws:

`EqualTerminalState != EquivalentHistory`.

`SameSerializedLog != EquivalentHistory`.

`EquivalentHistory != SameOccurrenceSet`.

`HistoryEquivalenceIsObservationRelative`.

## 3. Causal abstraction / hiding

`Hide_H(S,H,Ω_H)` may hide internal events S only if an abstraction witness preserves every `Ω_H`-visible consequence.

When an internal causal chain:

`a ≺c x ≺c b`

is hidden, the abstraction must preserve the induced external causal reachability `a ≺c* b` if that relation is observable.

Likewise, hiding an internal shared dependency may not turn dependent branches into independent ones.

Canonical laws:

`HistoryHiding != EventErasure`.

`InternalEventHiding != CausalReachabilityErasure`.

`InternalDependencyHiding != IndependenceProof`.

`NormalizationRequiresCausalClosure`.

## 4. History graph composition

For histories `{H_i}` and explicit history wiring/gluing witness `W_h`:

`ComposeH_Γ({H_i},W_h)=>H_res`.

`W_h` identifies compatible open boundaries and specifies:

- event-identity equality vs distinctness;
- subject/lineage continuity;
- required causal/dependency edges;
- resource handoff/transformation;
- branch/cohort relations;
- contract/claim-epoch migrations;
- foreign-owner bridge admissibility;
- provenance transport.

Composition is partial: incompatible histories fail to compose.

### Non-composable examples

- gluing the same consumable resource output to two consumers without a split witness;
- introducing a causal cycle;
- composing mutually exclusive branch occurrences as if both occurred;
- splicing evidence/occurrences across incompatible identity epochs;
- treating two distinct Runtime Attempts as one Network occurrence without an identity witness.

`HistoryComposition != LogConcatenation`.

## 5. Conditional associativity

Let a finite global realization graph G be factored into three subhistories. Two bracketings are observationally equivalent if both are merely different factorizations of the same admissible G and all side conditions hold:

1. global event identities/gluing are identical modulo admitted alpha-renaming;
2. causal and dependency closure are the same;
3. resource transformations are compatible and residualization is confluent;
4. branch/conflict/cancellation semantics are unchanged;
5. migration/epoch boundaries are unchanged;
6. foreign bridge references keep the same owner/claim role;
7. no early hiding removes an `Ω_H`-visible distinction;
8. the same boundary outcomes/provenance summary is exposed.

Then:

`(H1 ⊗ H2) ⊗ H3 ≃_{Γ,Ω_H} H1 ⊗ (H2 ⊗ H3)`.

Canonical law:

`HistoryAssociativityIsConditional`.

Unconditional associativity remains rejected.

## 6. Identity elements are structural, not events

For disjoint/open history union, the empty graph may act as an identity when it contributes no event, time, dependency, resource or provenance effect.

For boundary gluing, a structural identity map may preserve the same open boundary without adding an occurrence.

An explicit WAIT, NO-OP, probe, retry, heartbeat, observation or attempted action is **not** an identity if it has event identity, consumes time/resources or changes evidence/currentness.

Canonical laws:

`HistoryIdentityIsStructural`.

`NoOpOccurrence != HistoryIdentity`.

`Wait != HistoryIdentity`.

## 7. Unordered vs concurrent vs independent

For events a,b:

### Causally unordered

`a ||_c b` when neither `a ≺c* b` nor `b ≺c* a` is established in H.

This is a graph relation, not an independence proof.

### Concurrently realizable

`ConcurrentPossible_Γ(a,b)` requires no conflict/exclusion edge plus compatible temporal/branch constraints.

### Independent

`Independent_Γ(a,b|Ω_H)` additionally requires a witness that relevant dependency/resource/provenance/authority relations do not couple the two events for the target observation.

Canonical laws:

`NoCausalEdge != Independence`.

`CausallyUnordered != Independent`.

`ConcurrentPossible != ParallelSafe`.

`SharedDependencyCanCoupleUnorderedEvents`.

## 8. Branch/race/cancellation algebra

A branch cohort history records branch state using event relations rather than one winner flag.

Useful branch realization statuses include:

- `NEVER_ACTIVATED`;
- `ACTIVATED`;
- `ATTEMPT_REFERENCED`;
- `OUTCOME_POSITIVE`;
- `OUTCOME_NEGATIVE`;
- `OUTCOME_UNKNOWN`;
- `CANCEL_REQUESTED`;
- `CANCEL_CONFIRMED`;
- `QUIESCED`;
- `LOSER_RESOLVED`.

These are history roles, not one universal implementation enum.

Canonical laws:

`WinnerKnown != OtherBranchesQuiescent`.

`CancellationRequest != CancellationEffect`.

`Cancelled != NeverStarted`.

`Loser != Failed`.

`RaceResolved != AllBranchesTerminated`.

`UnobservedLoser != NonOccurrence`.

A consequential hedged race cannot assume loser-effect absence merely because a winner has been selected.

## 9. Retry/replay identity algebra

Keep at least four identities distinct:

- request/proposal identity;
- Runtime Attempt identity;
- Network occurrence identity;
- external effect identity.

### Exact request replay

Re-presenting the same request/input identity does not determine whether the owner:

- returns historical support;
- creates a new Attempt;
- creates a new physical realization;
- suppresses duplicate effects;
- produces a duplicate effect.

Therefore:

`SameRequest != SameAttempt`.

`SameRequest != SameOccurrence`.

`SameRequestDigest != ExactlyOnceEffect`.

### Retry

A retry normally creates a fresh attempt/opportunity identity while linking to the prior failed/unknown history.

`RetryLineage(retry,prior)` is explicit.

A retry after unknown consequential effect requires a scoped admissibility witness from the effect/operation owner, such as deduplication, idempotency, fencing, reconciliation or explicit acceptance of duplication risk.

Canonical laws:

`UnknownOutcome != RetryPermission`.

`RetrySafetyRequiresEffectScopeWitness`.

`ReplaySemanticsBelongsToOwningContract`.

## 10. Repair / revalidation / failover / recovery / reconciliation algebra

These transitions are intentionally separate.

### Repair

`Repair(h,support0)=>support1`

changes support/configuration/binding/resource conditions.

### Revalidation

`Revalidate(E,Π,J)=>standing`

acquires/evaluates fresh evidence; it may establish that repair worked or failed. It is Projection/Currentness-facing and not itself a repair.

### Failover

`Failover(activeA,alternativeB,h)=>activeB`

changes active realization lineage. It may restore service for a broad K while violating exact-instance/session continuity.

### Recovery

`Recover_Γ(preFailure,h,post|ι,K,Π,J)`

establishes an admissible post-failure continuation under a specified identity role and contract requirement.

### Reconciliation

`Reconcile_Γ(history,evidence)=><standing,residuals,nextConstraints>`

resolves ambiguity/divergence about effects, identities, obligations or currentness, but does not erase history.

Canonical laws:

`RepairSucceeded != RecoveryEstablished`.

`Revalidation != Repair`.

`FailoverMayRecoverServiceWithoutPreservingExactIdentity`.

`RecoveryEstablished != RequirementSatisfied`.

`RecoveryRequiresIdentityRole`.

`Reconciliation != Revalidation`.

`ReconciliationMayConstrainRetry`.

## 11. Recovery pattern

A common but non-universal recovery pattern can be represented as:

`DEGRADE/FAIL`
`→ DETECT/OBSERVE`
`→ QUARANTINE or HOLD`
`→ REPAIR/FAILOVER/WAIT`
`→ REVALIDATE`
`→ RECOVERED_STANDING or CONTINUE_DEGRADED`
`→ RECONCILE residual history/obligations`.

Not every regime contains every step and the arrows are not universal total sequencing constraints. The pattern is a derived family of H/J/K transitions.

## 12. Realization Boundary Normal Form (RBNF)

For a finite acyclic history under fixed `Ω_H` and fixed abstraction/gluing witnesses, define:

`RBNF_{Γ,Ω_H}(H)=<I_ext,O_ext,C*,D*,Λ*,B*,R_res,T*,P*,L_hidden>`

where:

- `I_ext` — externally relevant incoming/open realization conditions;
- `O_ext` — externally exposed Network events/outcomes;
- `C*` — causal reachability closure among observable boundary events;
- `D*` — dependency/support closure required by later judgements;
- `Λ*` — identity/epoch/migration lineage summary;
- `B*` — unresolved/resolved branch/race/cancellation summary;
- `R_res` — resource/usage residual;
- `T*` — externally relevant temporal constraints/residuals;
- `P*` — provenance/foreign bridge summary;
- `L_hidden` — witness ledger justifying abstraction of internal events.

RBNF is an observation-relative semantic summary, not a claim that internal history never matters.

Candidate preservation law:

`H ≃_{Γ,Ω_H} RBNF_{Γ,Ω_H}(H)`

when abstraction is causally/dependency/provenance closed and all residuals are preserved.

Canonical laws:

`HistoryNormalFormIsObservationRelative`.

`EquivalentBoundaryState != EquivalentHistory`.

`RBNFRequiresCausalAndProvenanceClosure`.

No globally unique canonical history normal form is claimed.

## 13. Runtime receipt bridge dogfood

Round-2 isolated Runtime dogfood created two real Jobs against the same research source revision.

### Successful Runtime Job

- executable: `/usr/bin/true`;
- Runtime Attempt state: `succeeded`;
- execution disposition: `succeeded`;
- exitCode: 0;
- delivery disposition: `committed`;
- result/terminal evidence artifacts present;
- `semanticCompletionEvaluated=false`.

### Failed Runtime Job

- executable: `/usr/bin/false`;
- Runtime Attempt state: `failed`;
- execution disposition: `failed`;
- exitCode: 1;
- delivery disposition: `committed`;
- result/terminal evidence artifacts present;
- `semanticCompletionEvaluated=false`.

The Runtime registry preserves both durable histories.

Therefore:

`RuntimeExecutionSuccess != NetworkOccurrence`.

`RuntimeExecutionSuccess != SemanticCompletion`.

`RuntimeExecutionFailure != NoHistory`.

`RuntimeReceipt != NetworkOutcomeByIdentity`.

A Network realization may use a Runtime receipt only through an explicit bridge rule proving which Network occurrence/outcome the Runtime execution supports.

## 14. Workstation recovery/failover algebra dogfood

Existing Workstation tests remain consistent with the algebra:

- sticky active selection preserves B after A recovers, demonstrating failover lineage rather than stateless reselection;
- `lastRace` retains cohort/winner/timing evidence beyond current active identity;
- same-path recovery uses outage-cycle-bounded attempts/backoff and may remain UNAVAILABLE;
- recovery eligibility depends on failure class;
- stale runtime material is reconciled before a new start;
- stable public authority can remain while lease/active realization changes.

These cases support branch-history retention, repair/recovery separation and RBNF lineage/resource/provenance fields.

## 15. Round-2 candidate laws

1. `HistoryEquivalenceIsObservationRelative`.
2. `EqualTerminalState != EquivalentHistory`.
3. `HistoryHiding != EventErasure`.
4. `NormalizationRequiresCausalClosure`.
5. `HistoryAssociativityIsConditional`.
6. `HistoryIdentityIsStructural`.
7. `CausallyUnordered != Independent`.
8. `ConcurrentPossible != ParallelSafe`.
9. `WinnerKnown != OtherBranchesQuiescent`.
10. `CancellationRequest != CancellationEffect`.
11. `Cancelled != NeverStarted`.
12. `Loser != Failed`.
13. `SameRequest != SameAttempt`.
14. `SameRequestDigest != ExactlyOnceEffect`.
15. `UnknownOutcome != RetryPermission`.
16. `RetrySafetyRequiresEffectScopeWitness`.
17. `RepairSucceeded != RecoveryEstablished`.
18. `Revalidation != Repair`.
19. `FailoverMayRecoverServiceWithoutPreservingExactIdentity`.
20. `RecoveryEstablished != RequirementSatisfied`.
21. `ReconciliationMayConstrainRetry`.
22. `HistoryNormalFormIsObservationRelative`.
23. `RBNFRequiresCausalAndProvenanceClosure`.
24. `RuntimeExecutionSuccess != NetworkOccurrence`.
25. `RuntimeExecutionSuccess != SemanticCompletion`.
26. `RuntimeExecutionFailure != NoHistory`.

These remain derived Network laws, not numbered Foundations.
