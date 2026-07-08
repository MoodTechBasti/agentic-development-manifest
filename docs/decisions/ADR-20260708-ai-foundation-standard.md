# ADR-20260708-ai-foundation-standard

> ID: ADR-20260708-ai-foundation-standard
> Status: ACCEPTED
> Last updated: 2026-07-08
> Owner: Principal Architect

## Status Overview

| Metric | Value |
| --- | --- |
| Confidence level | 9 |
| Affected modules | `docs/AI_FOUNDATION_STANDARD.md`, `docs/SAAS_FOUNDATION_BLUEPRINT.md`, `spec/ADM_v1_DRAFT.md`, `docs/OPERATING_SYSTEM.md`, `prompts/master_prompt.md` |
| New dependencies | no |
| Security review | PASSED |
| Cost review | PASSED |
| Performance review | PASSED |

## 1. Context and Reason

ADM Roadmap Phase 2 established the SaaS Foundation Standard: users, organizations, tenants, workspaces, memberships, roles, permissions, billing readiness, quotas, jobs, observability, admin diagnostics, data lifecycle, developer experience, tests, and performance budgets.

The next roadmap gap is Roadmap Phase 3: a canonical AI Foundation Standard. ADM already names the AI topics in `ROADMAP.md`, but they are not yet defined as a reusable architecture block.

Without this standard, future product repositories can embed AI features directly into product code. That creates predictable rework: provider contracts leak into features, prompts become unversioned strings, tools execute without explicit scope, evaluations are skipped, costs cannot be attributed, fallback behavior is improvised, caches ignore tenant context, and safety rules live only inside prompt text.

This ADR accepts the AI Foundation Standard as the Roadmap Phase 3 architecture block. Roadmap phases in `ROADMAP.md` remain distinct from ADM lifecycle phases in `spec/ADM_v1_DRAFT.md`.

## 2. Decision

ADM adopts the AI Foundation Standard as the canonical Roadmap Phase 3 architecture block.

The standard defines the minimum AI architecture concepts that must be considered before building product-specific AI features:

| Area | Required decision |
| --- | --- |
| Provider abstraction | How provider and model capabilities stay replaceable and normalized. |
| Prompt registry | How prompts are identified, versioned, owned, evaluated, and changed. |
| Tool registry | Which tools exist, which scopes they require, and which side effects they may have. |
| Evaluation | How quality, safety, cost, latency, and regressions are measured. |
| AI cost tracking | How cost is attributed by user, tenant, feature, prompt, tool, provider, request, job, and cache behavior. |
| Routing | How tasks choose provider, model class, quality tier, cost tier, or local execution. |
| Fallback | What happens during provider failure, timeout, cost limit, quality failure, or safety block. |
| Caching | Which AI artifacts can be cached, for how long, and under which tenant and data-lifecycle rules. |
| Safety rules | How data, prompts, tools, outputs, logs, cache, evaluation and human approval are constrained. |

The standard keeps a documentation-only posture. It requires explicit boundaries but does not require a provider SDK, runtime framework, prompt database, tool execution engine, model router, validator, workflow, or schema.

## 3. Scope Boundary

v0.20 is documentation and architecture only.

It does not add:

- runtime AI implementation,
- provider SDK integration,
- generated code,
- prompt execution,
- real model calls,
- real tool execution,
- database schema,
- validator enforcement,
- workflow changes,
- provider secrets,
- release automation.

Future PRs may add schema, validator, checklist, workflow support, provider adapters, or runtime code only after the Roadmap Phase 3 vocabulary remains stable and the maintainer explicitly approves that narrower scope.

## 4. Relationship to Roadmap Phase 2

The AI Foundation Standard depends on the SaaS Foundation Standard but does not replace it.

Roadmap Phase 2 defines SaaS system boundaries:

- users, organizations, tenants, workspaces and memberships,
- roles, permissions, support access and audit,
- billing readiness, entitlements, quotas, usage and cost tracking,
- jobs, workers, observability, admin diagnostics and data lifecycle.

Roadmap Phase 3 adds AI-specific boundaries on top:

- provider abstraction,
- prompt and tool governance,
- evaluation,
- AI cost attribution,
- routing, fallback and caching,
- AI safety and artifact lifecycle.

AI features must attach to the SaaS boundaries instead of creating parallel user, tenant, permission, billing, job, logging or lifecycle rules.

## 5. Evidence

- `ROADMAP.md` names Roadmap Phase 3 as AI Foundation Standard and lists provider abstraction, prompt registry, tool registry, evaluation, cost tracking, routing, fallback, caching, and safety rules.
- `docs/SAAS_FOUNDATION_BLUEPRINT.md` excludes deep AI provider architecture, Prompt Registry, Evaluation Framework and model routing from Roadmap Phase 2 and now points those concerns to `docs/AI_FOUNDATION_STANDARD.md`.
- `spec/ADM_v1_DRAFT.md` preserves model-neutrality and defines the Roadmap Phase 3 AI Foundation boundary separately from lifecycle phases.
- `prompts/master_prompt.md` warns against vendor lock-in and requires documentation of significant architecture decisions.

## 6. Alternatives

### Alternative A: Keep AI topics only in the roadmap

- Description: Leave Roadmap Phase 3 as a one-line roadmap item.
- Reason for rejection: Roadmap text is not enough for reusable adoption. Future agents need canonical terms and explicit boundaries before AI work starts.

### Alternative B: Implement provider adapters immediately

- Description: Add concrete provider interfaces, SDK adapters, prompt execution, caching code or model routing in v0.20.
- Reason for rejection: That would mix standard definition with runtime implementation and provider choice. The vocabulary must stabilize first.

### Alternative C: Treat AI as normal SaaS feature work

- Description: Let product teams handle prompts, tools, provider calls, caching and evaluation inside feature-specific ADRs.
- Reason for rejection: AI adds cross-cutting cost, safety, data, tool and provider risks that product features should not define independently every time.

## 7. Trade-offs

### Pros

- Creates a clear Roadmap Phase 3 standard before product-specific AI implementation.
- Reduces provider lock-in, prompt drift, tool sprawl, hidden cost and unsafe caching.
- Keeps ADM model-neutral and provider-neutral.
- Gives future validators a stable target without enforcing it yet.
- Cleanly connects AI architecture to the existing SaaS Foundation boundaries.

### Cons

- Adds more architecture vocabulary to maintain.
- Can feel heavy for small AI experiments unless minimal variants stay allowed.
- May need future pruning if some fields prove too broad.

## 8. Risks and Consequences

- Short-term risk: Agents may treat the standard as a mandate to build a complete AI platform.
- Long-term risk: Future validators could become too rigid for experimental or local-only AI features.
- Security risk: Prompt registry and evaluation documents could tempt teams to store sensitive examples.
- Mitigation plan: Keep v0.20 documentation-only, forbid provider/runtime implementation in this PR, require minimal variants, and preserve explicit data-lifecycle and safety boundaries.

## 9. ADM Exemptions

No ADM line-limit or quality-rule exemptions are introduced by this ADR.

## 10. Affected Files

- [x] `docs/decisions/ADR-20260708-ai-foundation-standard.md`
- [x] `docs/AI_FOUNDATION_STANDARD.md`
- [x] `docs/SAAS_FOUNDATION_BLUEPRINT.md`
- [x] `spec/ADM_v1_DRAFT.md`
- [x] `docs/OPERATING_SYSTEM.md`
- [x] `prompts/master_prompt.md`
- [x] `README.md`
- [x] `ROADMAP.md`
- [x] `CHANGELOG.md`

## 11. Review Log

- [x] Principal Architect: APPROVED — `REV-ARCH-20260708-ai-foundation-standard.md`
- [x] Security Lead: APPROVED — `REV-SEC-20260708-ai-foundation-standard.md`
- [x] Performance Lead: APPROVED — `REV-PERF-20260708-ai-foundation-standard.md`
- [x] Cost Engineer: APPROVED — `REV-COST-20260708-ai-foundation-standard.md`
- [x] Simplifier: APPROVED — `REV-SIMP-20260708-ai-foundation-standard.md`
- [x] Documentation Reviewer: APPROVED — `REV-DOC-20260708-ai-foundation-standard.md`

## 12. Final Outcome

Accepted for v0.20 after maintainer approval and successful validation of the full review set.
