# Network Operational Realization Theory — Round 2
## Realization Algebra and Runtime Dogfood

Status: COMPLETE / OPERATIONAL REALIZATION ALGEBRA v0 SURVIVES

## 1. History-equivalence tournament

### Failed candidate A: same terminal state

Two histories can end with the same current state while differing in prior failure, compensation, consumed resources, identity lineage, unresolved loser branch or external effect. Those differences may matter to retry/recovery/currentness.

`EqualTerminalState != EquivalentHistory`.

### Failed candidate B: same serialized log shape

Two logs can show identical event labels while referring to different identities, epochs, owners or causal/dependency structures.

### Survivor

`H1 ≃_{Γ,Ω_H} H2` is observation-relative contextual equivalence preserving all `Ω_H`-visible boundary outcomes, causal/dependency closure, lineage, branch status, resource residual, temporal constraints and provenance.

PASS.

## 2. Hiding / causal closure tournament

### Counterexample

History:

`a -> x -> b`

Hide x and remove both edges. The summary now falsely permits a and b to appear causally independent.

### Result

Hiding internal events must preserve induced external causal reachability and all observable dependency/provenance consequences.

`HistoryHiding != EventErasure`.

`InternalEventHiding != CausalReachabilityErasure`.

`NormalizationRequiresCausalClosure`.

PASS.

## 3. Composition / associativity tournament

### Unconditional associativity counterexamples

- one consumable resource is allocated by an early composition;
- early branch cancellation suppresses an event visible to a later context;
- early hiding removes a shared dependency;
- one factorization crosses a claim/contract migration boundary differently;
- foreign-owner receipt references are identified differently.

### Survivor

Conditional associativity holds when both bracketings are merely factorizations of one finite admissible global realization graph with the same event identities, causal/dependency closure, resource residualization, branch semantics, migrations, bridge ownership and observation summary.

`HistoryAssociativityIsConditional`.

No universal monoid is admitted.

## 4. Identity tournament

An empty/open history can be a structural identity for disjoint graph composition. A boundary identity map can glue the same open realization boundary without adding an occurrence.

But WAIT/NO-OP/probe/heartbeat/retry are real events when they consume time, create evidence or alter standing.

`HistoryIdentityIsStructural`.

`NoOpOccurrence != HistoryIdentity`.

PASS.

## 5. Concurrency / independence tournament

### Counterexample

Two candidate-member health events have no known causal edge but share one parent anchor. They can be temporally unordered while their fates are correlated by the shared dependency.

### Result

Three notions are separated:

- causally unordered;
- concurrently realizable;
- independent for a named observation/dependency scope.

`CausallyUnordered != Independent`.

`ConcurrentPossible != ParallelSafe`.

`SharedDependencyCanCoupleUnorderedEvents`.

PASS.

## 6. Race/cancellation tournament

A hedged race may resolve a winner before all other attempts are known to be quiescent. A cancellation request can race with an already-started loser occurrence/effect.

Therefore branch history distinguishes never activated, activated, attempt-referenced, positive/negative/unknown outcome, cancel-requested, cancel-confirmed and quiesced states.

New laws:

- `WinnerKnown != OtherBranchesQuiescent`;
- `CancellationRequest != CancellationEffect`;
- `Cancelled != NeverStarted`;
- `Loser != Failed`;
- `RaceResolved != AllBranchesTerminated`.

PASS.

## 7. Retry / replay tournament

### Runtime pressure

The same request identity can be deduplicated, replayed from history, or admitted as a new attempt depending on the owning Runtime/operation contract. Network cannot infer attempt/effect identity from a request digest.

### Unknown-effect attack

If an earlier action has unknown consequential effect, unconditional retry can duplicate the effect.

### Result

Keep request, Attempt, Network occurrence and external effect identities distinct.

`SameRequest != SameAttempt`.

`SameRequestDigest != ExactlyOnceEffect`.

`UnknownOutcome != RetryPermission`.

`RetrySafetyRequiresEffectScopeWitness`.

PASS without annexing Runtime's retry/effect semantics.

## 8. Repair/recovery/reconciliation tournament

### Counterexample A

A repair command succeeds mechanically but fresh health evidence remains red.

Therefore:

`RepairSucceeded != RecoveryEstablished`.

### Counterexample B

Failover A->B restores broad any-provider service but violates exact-instance continuity.

`FailoverMayRecoverServiceWithoutPreservingExactIdentity`.

### Counterexample C

Fresh observation that a path is healthy is revalidation, not the repair that produced it.

`Revalidation != Repair`.

### Counterexample D

A recovered network relation may still fail the user's K requirement/deadline.

`RecoveryEstablished != RequirementSatisfied`.

### Result

Repair, revalidation, failover, recovery and reconciliation form distinct typed transitions.

PASS.

## 9. RBNF tournament

A boundary summary containing only initial/final state fails because it loses causal reachability, branch residuals, resource consumption and provenance.

A richer Realization Boundary Normal Form survives for finite acyclic H under fixed observation/abstraction witnesses:

`RBNF=<I_ext,O_ext,C*,D*,Λ*,B*,R_res,T*,P*,L_hidden>`.

The normal form preserves external causal/dependency closure, lineage, unresolved race/cancellation, resource/time residuals and bridge provenance.

`HistoryNormalFormIsObservationRelative`.

`RBNFRequiresCausalAndProvenanceClosure`.

Global uniqueness is not claimed.

## 10. Live Runtime receipt dogfood

Round 2 intentionally executed two harmless local commands in the isolated research workspace.

### Success case

`/usr/bin/true`

Runtime returned:

- durable Job and Attempt identities;
- `attemptState=succeeded`;
- `executionDisposition=succeeded`;
- `exitCode=0`;
- result and terminal-evidence artifacts;
- `deliveryDisposition=committed`;
- `semanticCompletionEvaluated=false`.

### Failure case

`/usr/bin/false`

Runtime returned:

- durable Job and Attempt identities;
- `attemptState=failed`;
- `executionDisposition=failed`;
- `exitCode=1`;
- result and terminal-evidence artifacts;
- `deliveryDisposition=committed`;
- `semanticCompletionEvaluated=false`.

Runtime task listing retains both records.

### Derived boundary result

Physical execution success/failure is real Runtime evidence, but neither receipt establishes Network occurrence or semantic completion by identity.

`RuntimeExecutionSuccess != NetworkOccurrence`.

`RuntimeExecutionSuccess != SemanticCompletion`.

`RuntimeExecutionFailure != NoHistory`.

`RuntimeReceipt != NetworkOutcomeByIdentity`.

This is direct dogfood of the Network↔Runtime owner membrane.

## 11. Workstation history re-evaluation

Historical Workstation failover/recovery remains consistent with the algebra:

- sticky B after A recovery proves failover has lineage/history rather than stateless winner recomputation;
- `lastRace` preserves information beyond current active member;
- recovery attempts/backoff can accumulate while current status remains UNAVAILABLE;
- recovery eligibility is typed by failure class;
- stale transient runtime is reconciled before fresh start.

These cases falsify winner-only, current-state-only and recovery=success models.

## 12. Round-2 verdict

Operational Realization Algebra v0 survives as a typed partial graph algebra with:

- observation-relative history equivalence;
- causality-preserving hiding;
- witnessed graph composition;
- conditional associativity;
- structural identities rather than no-op events;
- causal-unordered/concurrent/independent separation;
- explicit race cancellation/quiescence semantics;
- request/attempt/occurrence/effect identity separation;
- scoped retry safety under unknown effects;
- repair/revalidation/failover/recovery/reconciliation separation;
- observation-relative RBNF;
- direct Runtime receipt bridge dogfood.

No NCT v1, Capability Calculus v1, Projection & Currentness v1 or NDF reopen condition fires.

## 13. Round-3 frontier

Next step should be theorem/closure rather than more syntax:

1. formalize `Ω_H` contextual equivalence and RBNF preservation theorem;
2. prove/falsify conditional history associativity on finite acyclic fixed-global-graph fragments;
3. formalize safe independence witness and independence preservation under hiding/composition;
4. theorem-test race quiescence/cancellation and consequential loser uncertainty;
5. formalize retry admissibility under known-no-effect / known-effect / unknown-effect regimes;
6. theorem-test recovery composition and identity/standing preservation;
7. decide FREEZE / REPAIR / REJECT Operational Realization Theory v1;
8. if frozen, perform a final whole-NCT derived-theory reconciliation across K, Π/J and H without reopening Foundations.
