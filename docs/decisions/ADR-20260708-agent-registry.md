# ADR-20260708-agent-registry

> ID: ADR-20260708-agent-registry
> Status: ACCEPTED
> Last updated: 2026-07-08
> Owner: Principal Architect

## Status Overview

| Metric | Value |
| --- | --- |
| Confidence level | 9 |
| Affected modules | `docs/OPERATING_SYSTEM.md`, `.ai/README.md`, `.ai/agents/README.md`, `spec/ADM_v1_DRAFT.md`, `prompts/master_prompt.md` |
| New dependencies | no |
| Security review | PASSED |
| Cost review | PASSED |
| Performance review | PASSED |

## 1. Context and Reason

ADM already defines repository-backed truth, review governance, release gates, project-owned memory, and `.ai/` runtime artifacts.

The next missing Phase 1 component is a clear registry for agents. Without it, future sessions can invent roles, overstep responsibility boundaries, skip required initialization, or leave handovers that are hard to route to the next suitable agent.

This ADR defines the Agent Registry as a repository-owned role and responsibility layer. It is not an authentication system, a permission sandbox, or an automation engine.

## 2. Decision

ADM adopts an Agent Registry as a first-class architecture rule.

The Agent Registry describes durable agent roles, their responsibility boundaries, required initialization context, write expectations, and handover obligations.

The canonical registry location is `.ai/agents/`. The directory may contain a human-readable `README.md` and later one or more registry files such as `registry.md`, `registry.yml`, or role-specific files.

Required registry concepts:

| Concept | Meaning |
| --- | --- |
| `agent_id` | Stable repository-local identifier for an agent role |
| `role` | Human-readable role name |
| `mission` | Primary responsibility of the role |
| `reads` | Documents or `.ai/` areas the role must inspect before work |
| `writes` | Areas the role may update when in scope |
| `forbidden` | Areas the role must not change without explicit approval |
| `handover_to` | Recommended next role or role family |
| `review_scope` | Review responsibility, if any |

Agent Registry rules:

1. Agent roles are project-owned documentation, not model identities.
2. Registry entries must use repository-relative paths.
3. Registry entries must not contain secrets, private local paths, personal data, or vendor-specific hidden memory assumptions.
4. The registry may describe expected write areas, but it does not replace repository rulesets, CI, code review, or local sandboxing.
5. Agents must state their active role and scope before implementation.
6. Handover should name the recommended next registry role when that is useful.

## 3. Evidence

- `docs/OPERATING_SYSTEM.md` already reserves `.ai/agents/` in the file-based operating-system structure.
- `prompts/master_prompt.md` already requires agents to state role, scope, assumptions, and planned next action before implementation.
- Project-owned memory already defines the repository as the authority over durable context.
- Review governance already defines reusable specialist roles, but it does not yet define runtime role routing or agent ownership boundaries.

## 4. Alternatives

### Alternative A: Keep roles only in the master prompt

- Description: The master prompt names common agent behavior, but no repository-owned registry exists.
- Reason for rejection: A prompt-only role model is hard to audit, hard to evolve per project, and easy for future agents to skip or reinterpret.

### Alternative B: Build a strict permission engine now

- Description: Implement machine-enforced agent permissions, schemas, and validators immediately.
- Reason for rejection: This is premature. ADM first needs the architecture and vocabulary before enforcement can be designed safely.

### Alternative C: Use vendor-specific agent profiles

- Description: Store roles in Claude, Codex, IDE, or local tool configuration.
- Reason for rejection: This breaks model neutrality and prevents reliable handover between tools.

## 5. Trade-offs

### Pros

- Makes agent roles explicit, auditable, and portable.
- Reduces role confusion between planner, implementer, reviewer, and maintainer sessions.
- Supports better handover routing without requiring automation yet.
- Preserves model neutrality by keeping role definitions in the repository.
- Creates a clean foundation for later handover automation.

### Cons

- Adds another documentation surface that can become stale.
- Agents may treat the registry as hard security when it is only governance until validators exist.
- Too many roles can create process overhead.

## 6. Risks and Consequences

- Short-term risk: Agents may over-specify roles before the project needs them.
- Long-term risk: Registry files may drift from actual practice if handovers do not reference them.
- Mitigation plan: Keep v0.17 documentation-only, define minimal required fields, and defer validator enforcement and handover automation to later work.

## 7. ADM Exemptions

No ADM line-limit or quality-rule exemptions are introduced by this ADR.

## 8. Affected Files

- [x] `docs/decisions/ADR-20260708-agent-registry.md`
- [x] `.ai/agents/README.md`
- [x] `spec/ADM_v1_DRAFT.md`
- [x] `docs/OPERATING_SYSTEM.md`
- [x] `.ai/README.md`
- [x] `prompts/master_prompt.md`
- [x] `README.md`
- [x] `ROADMAP.md`
- [x] `CHANGELOG.md`

## 9. Review Log

- [x] Principal Architect: APPROVED — `REV-ARCH-20260708-agent-registry.md`
- [x] Security Lead: APPROVED — `REV-SEC-20260708-agent-registry.md`
- [x] Performance Lead: APPROVED — `REV-PERF-20260708-agent-registry.md`
- [x] Cost Engineer: APPROVED — `REV-COST-20260708-agent-registry.md`
- [x] Simplifier: APPROVED — `REV-SIMP-20260708-agent-registry.md`
- [x] Documentation Reviewer: APPROVED — `REV-DOC-20260708-agent-registry.md`

## 10. Final Outcome

Accepted for v0.17 after maintainer approval and successful validation of the full review set.