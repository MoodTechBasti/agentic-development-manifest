# ADR-20260708-handover-automation

> ID: ADR-20260708-handover-automation
> Status: ACCEPTED
> Last updated: 2026-07-08
> Owner: Principal Architect

## Status Overview

| Metric | Value |
| --- | --- |
| Confidence level | 9 |
| Affected modules | `docs/OPERATING_SYSTEM.md`, `templates/HANDOVER_TEMPLATE.md`, `spec/ADM_v1_DRAFT.md`, `prompts/master_prompt.md`, `.ai/README.md`, `.ai/agents/README.md` |
| New dependencies | no |
| Security review | PASSED |
| Cost review | PASSED |
| Performance review | PASSED |

## 1. Context and Reason

ADM already defines repository-backed truth, project-owned memory, review governance, release gates, and Agent Registry role routing.

The remaining Phase 1 gap is Handover Automation: future agents need a predictable handover structure that can later be checked or generated without turning automation into an authority source.

Current handovers are useful but partly prose-driven. Without explicit field boundaries, agents can omit verification results, invent next roles, lose task state, or claim CI-readiness without evidence.

This ADR defines Handover Automation as an architecture rule and field model. It does not implement validators, workflows, generators, schemas, bots, or release automation.

## 2. Decision

ADM adopts Handover Automation as a documentation-first architecture layer.

Handover Automation means that session handovers use stable, repository-owned fields so later tools can prefill, lint, or validate them safely.

Canonical handover location:

- Runtime handovers: `.ai/handover/`
- Reusable template: `templates/HANDOVER_TEMPLATE.md`

Required handover concepts:

| Concept | Meaning |
| --- | --- |
| `session_id` | Stable identifier for the handover instance |
| `timestamp` | Time of handover creation with timezone |
| `outgoing_agent` | Agent or tool ending the session |
| `active_role` | Registry role used during the session, if applicable |
| `target_recipient` | Next agent, maintainer, or general recipient |
| `completed_tasks` | Work completed in the session |
| `open_tasks` | Work not yet completed |
| `blocked_tasks` | Work blocked by missing input, failed checks, or policy limits |
| `changed_files` | New, changed, or deleted repository paths |
| `checks_run` | Commands or checks executed and their results |
| `review_status` | Review artifacts, votes, validation mode, and CI-readiness |
| `agent_routing` | Recommended next registry role and rationale |
| `risks` | Known risks, assumptions, and mitigations |
| `next_steps` | Concrete recommended follow-up work |

Machine-checkable fields may include identifiers, repository paths, role IDs, status values, review-set metadata, and commit SHAs.

Human-review fields include summaries, rationale, risk quality, and the usefulness of notes for the next agent.

## 3. Automation Boundaries

Future automation may:

1. Prefill a handover from git status, branch metadata, review files, active tasks, and Agent Registry entries.
2. Check that required fields exist.
3. Check that referenced files use repository-relative paths.
4. Check that referenced review sets, target refs, and target commits are consistent.
5. Check that a recommended next role exists in Agent Registry when a registry file is present.
6. Warn when checks are marked passed without command evidence.
7. Report missing risks, blockers, or next steps as advisory findings.

Future automation must not:

1. Invent checks, commits, review votes, or CI results.
2. Mark work complete when required validation was not run.
3. Remove risks to create a green status.
4. Treat hidden model memory, chat history, local scratch files, or tool caches as authoritative input.
5. Commit credentials, private URLs, private local paths, raw logs, or sensitive data.
6. Merge pull requests, create release tags, or mutate branch protection.
7. Replace human approval for governance, release, or security-sensitive changes.

## 4. Relationship to Project-owned Memory

Handover files are runtime history, not canonical project truth.

Durable conclusions that must survive beyond one session should be moved or summarized into the correct repository-owned layer:

| Destination | Use when |
| --- | --- |
| `docs/decisions/` | ADM standard architecture decision |
| `.ai/decisions/` | Project-specific runtime decision |
| `.ai/memory/` | Curated durable project fact or constraint |
| `.ai/knowledge/` | Curated research or source-aware project knowledge |
| `.ai/tasks/` | Active or planned work state |
| `.ai/handover/` | Session transition and immediate continuation state |

Handover Automation may reference memory and tasks, but it must not silently overwrite them.

## 5. Relationship to Agent Registry

Agent Registry defines durable roles and routing hints. Handover Automation consumes those hints.

A handover should record:

- the active registry role, if relevant,
- the recommended next registry role or role family,
- the reason for that routing,
- any missing or ambiguous registry role as an explicit open question.

Automation must not invent a new role when the registry lacks one. It may only suggest that a registry update is needed.

## 6. Evidence

- `docs/OPERATING_SYSTEM.md` already defines `.ai/handover/` as part of the file-based operating system.
- `templates/HANDOVER_TEMPLATE.md` already provides a reusable handover shape.
- `prompts/master_prompt.md` already requires significant sessions to end with a handover.
- Project-owned Memory already defines `.ai/handover/` as versioned runtime history.
- Agent Registry already defines `handover_to` as role routing metadata.

## 7. Alternatives

### Alternative A: Keep handovers as free-form prose

- Description: Agents write narrative summaries without field-level structure.
- Reason for rejection: Free-form handovers are hard to validate, hard to route, and easy to make incomplete.

### Alternative B: Implement a strict validator now

- Description: Add schema validation, CI enforcement, and workflow changes immediately.
- Reason for rejection: The field model and boundaries must be accepted first. Premature enforcement would freeze unclear semantics.

### Alternative C: Use chat transcript export as handover

- Description: Store raw chat logs or hidden model memory exports.
- Reason for rejection: This is not concise, not model-neutral, not safe for secrets, and not repository-governed.

## 8. Trade-offs

### Pros

- Makes session continuation more reliable across agents and tools.
- Gives future validators a clear target without implementing them yet.
- Connects Agent Registry, Project-owned Memory, reviews, tasks, and handovers.
- Reduces false CI-readiness and missing-risk handovers.

### Cons

- Adds structure to every significant handover.
- Can become busywork if agents overfill low-value fields.
- Requires discipline to keep handovers concise and evidence-based.

## 9. Risks and Consequences

- Short-term risk: Agents may treat template completeness as proof of work quality.
- Long-term risk: Automation may be over-trusted as an approval mechanism.
- Mitigation plan: Keep v0.18 documentation-only, separate machine-checkable structure from human-review content, and defer validators/workflows to later PRs.

## 10. ADM Exemptions

No ADM line-limit or quality-rule exemptions are introduced by this ADR.

## 11. Affected Files

- [x] `docs/decisions/ADR-20260708-handover-automation.md`
- [x] `spec/ADM_v1_DRAFT.md`
- [x] `docs/OPERATING_SYSTEM.md`
- [x] `templates/HANDOVER_TEMPLATE.md`
- [x] `prompts/master_prompt.md`
- [x] `README.md`
- [x] `ROADMAP.md`
- [x] `CHANGELOG.md`

## 12. Review Log

- [x] Principal Architect: APPROVED — `REV-ARCH-20260708-handover-automation.md`
- [x] Security Lead: APPROVED — `REV-SEC-20260708-handover-automation.md`
- [x] Performance Lead: APPROVED — `REV-PERF-20260708-handover-automation.md`
- [x] Cost Engineer: APPROVED — `REV-COST-20260708-handover-automation.md`
- [x] Simplifier: APPROVED — `REV-SIMP-20260708-handover-automation.md`
- [x] Documentation Reviewer: APPROVED — `REV-DOC-20260708-handover-automation.md`

## 13. Final Outcome

Accepted for v0.18 after maintainer approval and successful validation of the full review set.