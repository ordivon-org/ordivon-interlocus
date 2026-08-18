# Ordivon Network Capability Calculus v0

Status: PROVISIONAL DERIVED THEORY / ROUND-1 SURVIVOR

Upstream authority: frozen `NCT_v1=<K,Π,H;J>_Γ`.

This calculus defines K-side contract structure. It does not claim that a contract declaration is a live capability, and it does not replace Π/H/J.

## 1. Polarized clause

The minimal K atom is a typed polarized clause:

`κ = <id, role, subject, predicate, μ, scope, version>`

where:

- `role ∈ {Assume, Require, Offer, Guarantee}`;
- `polarity(Assume)=polarity(Require)=−`;
- `polarity(Offer)=polarity(Guarantee)=+`;
- `subject` names the Network-owned capability/requirement role under the current cut;
- `predicate` may include opaque imported predicates from SCD/Security/Normative/Physics/etc.;
- `μ` is a typed modality bundle;
- `scope` is the query/cut/time/principal scope;
- `version` identifies immutable clause/contract-version lineage.

Role tags are retained even when polarity is shared:

- Assume = premise expected from environment/upstream composition;
- Require = demand/satisfaction criterion to be discharged;
- Offer = exposed capability role;
- Guarantee = conditional property promised by a provider/interface.

`Assume != Require` and `Offer != Guarantee`, although they share variance polarity in provider-substitution reasoning.

## 2. Modality bundle

`μ = <q, u, χ, θ>`

- `q` — quantifier/standing mode;
- `u` — usage mode/algebra reference;
- `χ` — continuity/substitution mode;
- `θ` — temporal validity/satisfaction mode.

These are typed families, not four universal scalar lattices.

### Quantifier q

Examples include possible, controller-selectable, probabilistic, almost-sure, guaranteed, bounded variants.

No universal total strength order is admitted.

Use only a witnessed implication/preorder:

`q1 =>_Γ q2`

when the imported/regime semantics proves that q1 is at least as strong as q2 at the same conditioning/scope.

`QuantifierDifference != ScalarStrengthDifference`.

### Usage u

Usage is capability-family-specific. A usage theory may admit explicit operations such as:

- reuse;
- consume;
- reserve;
- exclusive-use;
- share;
- split;
- merge;
- discard;
- transfer.

No universal contraction/duplication or linearity rule is assumed.

`NoImplicitDuplication`: a consumable/exclusive capability cannot be discharged multiple times without an explicit usage witness.

`TypedUsage != UniversalLinearResource`.

### Continuity χ

`χ` defines which substitutions preserve a continuing requirement/association.

Examples:

- any-provider satisfying predicate P;
- equivalence-class provider;
- exact instance;
- association/session lineage;
- explicitly substitutable cohort.

Demand strengthening may narrow admissible substitutions:

`χ' ⊆ χ`.

A Harness selection event may therefore induce `K -> K'` from any-provider to exact-instance/session continuity, but the selection event remains Harness-owned and requires an explicit H bridge witness.

### Temporal θ

Temporal mode may express validity window, deadline, freshness, lifetime, future-contact condition, or another imported time predicate.

`Wait != TemporalIdentity`.

Temporal compatibility is a judgement over θ plus Π/H, not a universal interval-intersection rule.

## 3. Contract object

A K contract is:

`K = <kid, C, D, V>`

where:

- `kid` = immutable contract identity;
- `C` = finite or recursively described set of polarized clauses;
- `D` = declared dependency/support hypergraph among clauses/imported support roles;
- `V` = version/migration metadata.

D is a contract dependency declaration, not proof that the dependency/source is currently true or independent. Actual dependency/currentness is grounded through Π/H/J.

## 4. Predicate/clause compatibility

A positive clause `p` may discharge a negative clause `n` only through a typed discharge witness:

`p ⊣_w n`

The witness w must justify, where applicable:

1. subject/predicate entailment or admissible substitution;
2. `q_p => q_n`;
3. usage compatibility and resource accounting;
4. continuity compatibility;
5. temporal compatibility;
6. version/migration compatibility;
7. dependency/provenance compatibility;
8. owner-import predicates required by n.

Syntactic field equality is neither necessary nor sufficient.

## 5. No single universal refinement direction

The calculus distinguishes at least two refinement-like relations.

### Provider substitution refinement

`K' ⊑prov K`

means a provider/interface satisfying K' may safely stand where K was expected.

Under matched clause roles:

- negative side (Assume/Require): K' may demand no more than K;
- positive side (Offer/Guarantee): K' must provide at least what K provided;
- all modality changes require witnessed implication/compatibility.

This is polarity/variance sensitive.

### Demand strengthening

`D' ⊒req D`

means D' accepts a subset of the realizations/providers accepted by D.

Examples:

- any-provider(P) -> exact-instance(A);
- eventual delivery -> delivery before deadline;
- best-effort -> guaranteed under declared scope.

This is not provider refinement and must not reuse the same order silently.

Canonical law:

`ProviderRefinement != DemandStrengthening`.

More generally:

`RefinementDirectionIsRoleRelative`.

## 6. Composition as witnessed wiring/discharge

Rather than defining one universal sequential/parallel operator, the core calculus uses a typed wiring witness W:

`Compose_Γ({K_i}, W, Π, H) => K_res`

W maps selected negative clauses to positive clauses:

`W : n <- p [w]`

with discharge witness w.

Derived operator families are wiring patterns:

- parallel/open composition: little or no internal discharge;
- serial/service composition: downstream negative clauses discharged by upstream positives;
- branch/choice: branch-qualified wiring and quantifier preservation;
- feedback/recursive composition: cyclic wiring subject to base/fixed-point admissibility;
- transformation composition: positive clause converted through an H/owner witness before discharge.

The residual K contains:

- externally undischarged negative clauses;
- externally exposed positive clauses;
- updated usage/residual clauses;
- explicit dependency/provenance lineage;
- conditional derived offers/guarantees where a proof rule admits them.

`ContractComposition != LiveCapabilityComposition`.

A composed K describes conditional capability structure. Live standing still requires J over σ/Π/H.

## 7. Dependency discipline

Alternative realizations are clauses/branches. Independence is a J-level property grounded in Π dependency projections and H/provenance.

`AlternativeRealization != IndependentRealization`.

A contract may assert `Guarantee(Independent(...))`, but the claim requires external/source evidence; multiplicity alone cannot establish it.

Composition preserves support lineage. Shared support cannot be erased by hiding an internal clause.

`HiddenDependency != DischargedDependency`.

## 8. Residual contract

Partial service/use does not merely delete a Require clause.

Residual update is typed:

`Residualize_Γ(K, Π_pre, H, o, Π_post) => K'`

and is validated by J/Eval.

Residualization may:

- discharge a requirement;
- weaken/strengthen remaining quantity/quality/time conditions as contract semantics permit;
- consume/reserve/split a usage-bearing offer;
- narrow continuity after selection;
- preserve dormant obligations through wait/store;
- supersede a clause only with an explicit witness.

## 9. Contract evolution / meta-contract

Version migration is a history-mediated transition:

`Migrate_Γ(K_v, H_mig, witness) => K_v'`.

A meta-contract may constrain admissible K transitions, but negotiation does not retroactively establish the old/new capability standing.

`NegotiatedContract != RealizedCapability`.

## 10. Recursive contracts

Recursive contract graphs are admissible descriptions.

However:

`ContractCycle != CapabilityWitness`.

A cyclic discharge graph can establish live capability only with at least one of:

- grounded base capability/support;
- explicit establishment history;
- imported justified least/greatest fixed-point semantics with admissibility/guard conditions;
- another non-circular witness accepted by J.

The calculus makes no universal decidability claim for recursive refinement/composition.

## 11. Core judgements/interfaces to J

The K calculus exports candidate derivations to the NCT judgement layer:

- `ClauseEntails_Γ(p,n | Π,H)`;
- `ProviderRefines_Γ(K',K | Π,H)`;
- `DemandStrengthens_Γ(D',D)`;
- `Compatible_Γ(K1,K2 | W,Π,H)`;
- `Discharge_Γ(p,n | w,Π,H)`;
- `Compose_Γ({K_i},W,Π,H) => K_res`;
- `Residualize_Γ(K,Π_pre,H,o,Π_post) => K'`;
- `UsageAdmissible_Γ(u, operation | Π,H)`;
- `ContinuityAdmissible_Γ(χ, substitution | Π,H)`;
- `Migrate_Γ(K_v,H_mig,w) => K_v'`.

None of these by itself asserts `Cap_Γ(...)` unless the capability-standing judgement is separately discharged.

## 12. v0 laws / anti-laws

1. `ProviderRefinement != DemandStrengthening`.
2. `RefinementDirectionIsRoleRelative`.
3. `SyntacticMatch != Discharge`.
4. `ContractComposition != LiveCapabilityComposition`.
5. `QuantifierDifference != ScalarStrengthDifference`.
6. `TypedUsage != UniversalLinearResource`.
7. `NoImplicitDuplication`.
8. `AlternativeRealization != IndependentRealization`.
9. `HiddenDependency != DischargedDependency`.
10. `Wait != TemporalIdentity`.
11. `NegotiatedContract != RealizedCapability`.
12. `ContractCycle != CapabilityWitness`.

These are provisional derived-calculus laws, not numbered Network Foundations.
