# ADR-20260708-saas-foundation-standard

> ID: ADR-20260708-saas-foundation-standard
> Status: ACCEPTED
> Last updated: 2026-07-08
> Owner: Principal Architect

## Status Overview

| Metric | Value |
| --- | --- |
| Confidence level | 9 |
| Affected modules | `docs/SAAS_FOUNDATION_BLUEPRINT.md`, `spec/ADM_v1_DRAFT.md`, `docs/OPERATING_SYSTEM.md`, `prompts/master_prompt.md` |
| New dependencies | no |
| Security review | PASSED |
| Cost review | PASSED |
| Performance review | PASSED |

## 1. Context and Reason

ADM Phase 1 established the repository operating system: governance, release gates, project-owned memory, Agent Registry, and Handover Automation.

The next roadmap gap is Roadmap Phase 2: a canonical SaaS Foundation Standard. ADM already had a SaaS blueprint, but it was still an early draft and did not fully define the minimum architecture vocabulary for users, organizations, tenants, workspaces, roles, permissions, billing readiness, quotas, jobs, observability, admin systems, and data lifecycle.

Without this standard, future product repositories can build features before the foundation is explicit. That creates predictable rework: tenant boundaries get added late, billing logic leaks into product code, jobs run in request paths, usage is counted without cost attribution, and admin or audit capabilities are missing when customer support begins.

This ADR promotes the SaaS blueprint into a Roadmap Phase 2 standard. Roadmap phases in `ROADMAP.md` are distinct from the ADM lifecycle phases in `spec/ADM_v1_DRAFT.md`.

## 2. Decision

ADM adopts the SaaS Foundation Standard as the canonical Roadmap Phase 2 architecture block.

The standard defines the minimum architecture concepts that must be considered before building product-specific SaaS features:

| Area | Required decision |
| --- | --- |
| Identity | How users authenticate and relate to business entities. |
| Organizations | Whether ownership, billing, and membership live on an organization layer. |
| Tenants | What data, config, limits, jobs, storage, and audit records are isolated by. |
| Workspaces | Whether collaboration happens below organization or tenant level. |
| Memberships | How users join, leave, transfer ownership, and lose access. |
| Roles and permissions | Which actions are allowed, and where server-side authorization lives. |
| Billing readiness | How plans, subscriptions, provider adapters, and billing states are represented without provider lock-in. |
| Entitlements and quotas | Which features and usage limits are plan-controlled. |
| Usage and cost | How usage is aggregated per user, workspace, tenant, feature, request, worker time, and external provider. |
| Jobs and workers | How long-running work is retried, timed out, made idempotent, and diagnosed. |
| Observability and admin | How logs, metrics, request IDs, audit logs, job status, and support diagnostics are exposed safely. |
| Data lifecycle | How uploads, processing, exports, archives, deletes, backups, restores, logs, caches, and temporary files are handled. |

The standard keeps a Modular Monolith First posture. It requires clear boundaries but does not require microservices, a specific auth provider, a specific payment provider, or a specific queue technology.

## 3. Scope Boundary

v0.19 is documentation and architecture only.

It does not add:

- runtime SaaS implementation,
- database schema,
- generated code,
- validator enforcement,
- workflow changes,
- provider integrations,
- billing provider logic,
- AI provider architecture,
- real jobs or queues,
- release automation.

Future PRs may add schema, validator, checklist, or workflow support only after the Roadmap Phase 2 vocabulary remains stable.

## 4. Relationship to Phase 1

The SaaS Foundation Standard depends on Roadmap Phase 1 but does not replace it.

- Project-owned Memory stores durable SaaS decisions and constraints when future agents need them.
- Agent Registry can route SaaS architecture work to suitable roles.
- Handover Automation must record SaaS-related risks, open decisions, checks, and next steps.
- Review Governance remains the approval mechanism for architecture-critical changes.

## 5. Relationship to Roadmap Phase 3 AI Foundation

Roadmap Phase 2 prepares for AI-heavy SaaS systems but does not define the full AI layer.

Roadmap Phase 2 must make AI costs, tenant boundaries, data lifecycle, jobs, and observability possible. Roadmap Phase 3 will define provider abstraction, prompt registry, tool registry, evaluation, routing, fallback, caching, and AI-specific safety rules.

## 6. Evidence

- `ROADMAP.md` marks Roadmap Phase 1 as complete and names Roadmap Phase 2 as SaaS Foundation Standard.
- `README.md` states that the next major roadmap block after v0.18 is SaaS Foundation Standard.
- `docs/SAAS_FOUNDATION_BLUEPRINT.md` already contained the core topics but needed canonical vocabulary, boundaries, and phase scoping.
- `spec/ADM_v1_DRAFT.md` already requires foundation build before product features.

## 7. Alternatives

### Alternative A: Keep the SaaS blueprint as a loose draft

- Description: Continue using the existing blueprint as informal guidance.
- Reason for rejection: Informal guidance is not strong enough for reusable ADM adoption. Future agents need canonical terms and phase boundaries.

### Alternative B: Add validators and schemas immediately

- Description: Implement machine-checkable SaaS Foundation validation in v0.19.
- Reason for rejection: The vocabulary must be accepted first. Premature enforcement would freeze unstable terms and create false confidence.

### Alternative C: Skip SaaS Foundation and move directly to AI Foundation

- Description: Define provider abstraction, prompt registry, evaluation, and routing before SaaS basics.
- Reason for rejection: AI systems still need tenancy, cost attribution, jobs, observability, permissions, and data lifecycle. Skipping Roadmap Phase 2 would push SaaS risk into Roadmap Phase 3.

## 8. Trade-offs

### Pros

- Creates a clear Roadmap Phase 2 standard before product-specific implementation.
- Reduces late rework around tenant, billing, permission, job, cost, and audit boundaries.
- Keeps ADM provider-neutral and modular-monolith-first.
- Gives future validators a stable target without implementing enforcement yet.
- Separates SaaS Foundation from the later AI Foundation.

### Cons

- Adds more architecture vocabulary to maintain.
- Can feel heavy for very small tools unless the standard explicitly allows minimal variants.
- May need future pruning if some fields prove too broad.

## 9. Risks and Consequences

- Short-term risk: Agents may treat the standard as a mandate to overbuild every SaaS system.
- Long-term risk: Future validators could become too rigid for small products.
- Mitigation plan: Keep v0.19 documentation-only, define minimal allowed variants, and delay schema or validator enforcement until after the standard is reviewed in practice.

## 10. ADM Exemptions

No ADM line-limit or quality-rule exemptions are introduced by this ADR.

## 11. Affected Files

- [x] `docs/decisions/ADR-20260708-saas-foundation-standard.md`
- [x] `docs/SAAS_FOUNDATION_BLUEPRINT.md`
- [x] `spec/ADM_v1_DRAFT.md`
- [x] `docs/OPERATING_SYSTEM.md`
- [x] `prompts/master_prompt.md`
- [x] `README.md`
- [x] `ROADMAP.md`
- [x] `CHANGELOG.md`

## 12. Review Log

- [x] Principal Architect: APPROVED — `REV-ARCH-20260708-saas-foundation-standard.md`
- [x] Security Lead: APPROVED — `REV-SEC-20260708-saas-foundation-standard.md`
- [x] Performance Lead: APPROVED — `REV-PERF-20260708-saas-foundation-standard.md`
- [x] Cost Engineer: APPROVED — `REV-COST-20260708-saas-foundation-standard.md`
- [x] Simplifier: APPROVED — `REV-SIMP-20260708-saas-foundation-standard.md`
- [x] Documentation Reviewer: APPROVED — `REV-DOC-20260708-saas-foundation-standard.md`

## 13. Final Outcome

Accepted for v0.19 after maintainer approval and successful validation of the full review set.
