# ADR-20260708-session-continuity-baseline

> ID: ADR-20260708-session-continuity-baseline
> Status: ACCEPTED
> Last updated: 2026-07-08
> Owner: Principal Architect

## Status Overview

| Metric | Value |
| --- | --- |
| Confidence level | 9 |
| Affected modules | `ROADMAP.md`, `README.md`, `CHANGELOG.md`, `spec/ADM_v1_DRAFT.md`, `docs/OPERATING_SYSTEM.md`, `.ai/README.md`, `.ai/handover/README.md`, `templates/HANDOVER_TEMPLATE.md`, `prompts/master_prompt.md` |
| New dependencies | no |
| Security review | PASSED |
| Cost review | PASSED |
| Performance review | PASSED |

## 1. Context and Reason

Roadmap Phase 7 is the Handover and Session Continuity phase.

ADM already accepted Project-owned Memory, Agent Registry, Handover Automation, Master Prompt Standard, Adapter Prompt Standard, Review and Validation Hardening, Foundation Consistency and Release Hygiene, Review Archive Policy, and Review Archive Migration Batch 1.

The remaining Phase 7 gap is not automation implementation. v0.18 already defined Handover Automation as a documentation-first architecture layer and explicitly deferred validators, schemas, workflows, generators, and runtime behavior.

The remaining gap is the continuity contract for a new agent session:

- how the next agent discovers the latest durable handover,
- which repository files are authoritative,
- what happens when handover evidence is missing or ambiguous,
- how checks, review status, target refs, commits, risks, and next steps are reported without invention,
- how session continuity stays separate from chat history, hidden model memory, local scratch files, raw logs, and tool caches.

Without this baseline, future agents can still restart from chat memory, assume a stale handover is current, treat a template as proof of work, or hide uncertainty behind confident prose.

## 2. Decision

ADM accepts Roadmap Phase 7 as the Session Continuity Baseline.

Session Continuity means that a future agent can resume work from repository-owned evidence before relying on any transient conversation, model memory, local profile, or tool cache.

Canonical continuity sources, in authority order:

1. Canonical repository documents: `spec/`, `docs/`, `ROADMAP.md`, `README.md`, accepted ADRs, governance and release runbooks.
2. Versioned runtime artifacts: `.ai/handover/`, `.ai/reviews/`, `.ai/reviews/archive/`, `.ai/decisions/`, `.ai/agents/`.
3. Curated project context: `.ai/memory/`, `.ai/knowledge/`, `.ai/tasks/`.
4. Local transient files only as non-authoritative working context.
5. Chat history, hidden model memory, local scratch files, raw logs, local tool profiles, and tool caches are never authoritative project truth.

The canonical handover discovery policy is documented in `.ai/handover/README.md`.

## 3. Required Continuity Behavior

A new ADM-controlled agent session must:

1. Establish the repository state from git and canonical documents before implementing.
2. Check `.ai/handover/` when a previous session could affect the task.
3. Determine the latest handover from explicit timestamp metadata first and filename timestamp second.
4. Treat conflicting or missing handover evidence as `UNKNOWN` or `AMBIGUOUS`.
5. Report ambiguity instead of reconstructing state from memory.
6. Preserve `NOT RUN` for checks that were not executed or proven by cited CI evidence.
7. Preserve repository-relative paths for changed files and evidence.
8. Carry forward open risks, blockers, and next steps unless repository evidence proves they are resolved.
9. Use Agent Registry role IDs only when they exist or explicitly report a missing role gap.
10. Treat handover status as continuation context, not approval.

## 4. Handover Status Model

ADM accepts these continuity status values for durable handovers:

| Status | Meaning |
| --- | --- |
| `READY` | The next agent has enough repository evidence to continue the stated next task. |
| `PARTIAL` | Some evidence exists, but the next agent must verify missing checks, scope, or state before implementation. |
| `BLOCKED` | Work cannot continue without a named blocker being resolved. |
| `UNKNOWN` | The handover cannot establish a reliable continuation state. |

`READY` does not mean merged, approved, released, CI-passed, or validated. It only means the handover is usable for the next continuation step.

## 5. Relationship to v0.18 Handover Automation

v0.18 defines which handover concepts may later be prefilling, linting, or cross-checking targets.

v0.28 defines how agents use handover evidence for session continuity before such automation exists.

Therefore:

- v0.18 is the automation boundary.
- v0.28 is the continuation behavior baseline.
- v0.28 does not replace or broaden v0.18.
- v0.28 does not implement the deferred linter, schema, workflow, generator, or runtime.

## 6. Non-goals

This baseline does not introduce:

- runtime code,
- real automation,
- Handover linter,
- new review validator mode,
- workflow changes,
- release automation,
- provider SDKs,
- MCP integration,
- local tool profiles,
- Gemini CLI or Antigravity CLI adapters,
- branch-protection changes,
- review archive migration,
- Phase 8 work,
- v1 release-candidate claims.

## 7. Evidence Rules

Session continuity evidence must be:

- repository-owned,
- repository-relative,
- explicit about freshness and uncertainty,
- non-sensitive,
- reviewable in git.

A handover must not include credentials, private URLs, private local paths, raw logs, hidden memory dumps, or raw chat transcripts.

If an agent cannot prove a fact from repository evidence, it must say so.

## 8. Alternatives

### Alternative A: Continue from chat memory

- Description: Agents use the prior conversation as primary continuity state.
- Reason for rejection: Chat memory is not portable, auditable, model-neutral, or reviewable.

### Alternative B: Implement a Handover linter now

- Description: Add schema and CI enforcement for handovers immediately.
- Reason for rejection: Phase 7 needs a stable human-readable continuity baseline first. Premature enforcement would freeze semantics too early.

### Alternative C: Create a central handover index

- Description: Add a generated or manually maintained index of active handovers.
- Reason for rejection: That creates another state surface and risks drift. Discovery by timestamp and filename is enough for v0.28.

## 9. Trade-offs

### Pros

- Makes fresh agent sessions more reliable.
- Reduces dependency on long-running chats and hidden memory.
- Keeps ADM repository-first and model-neutral.
- Clarifies what a handover can and cannot prove.
- Gives future handover linting a stable target without implementing it now.

### Cons

- Adds one more policy file under `.ai/handover/`.
- Adds small template overhead.
- Still depends on human discipline until a future linter is explicitly approved.

## 10. Risks and Consequences

- Short-term risk: Agents may treat `READY` as approval.
- Mitigation: `READY` is defined only as continuation readiness, not CI, review, merge, or release approval.

- Long-term risk: Handovers may become stale.
- Mitigation: latest-handover discovery must report ambiguity and stale evidence instead of guessing.

- Process risk: Phase 7 can drift into automation.
- Mitigation: v0.28 explicitly excludes linter, workflow, validator, runtime, and release automation work.

## 11. ADM Exemptions

No ADM line-limit or quality-rule exemptions are introduced by this ADR.

## 12. Affected Files

- [x] `docs/decisions/ADR-20260708-session-continuity-baseline.md`
- [x] `.ai/handover/README.md`
- [x] `templates/HANDOVER_TEMPLATE.md`
- [x] `docs/OPERATING_SYSTEM.md`
- [x] `spec/ADM_v1_DRAFT.md`
- [x] `prompts/master_prompt.md`
- [x] `.ai/README.md`
- [x] `README.md`
- [x] `ROADMAP.md`
- [x] `CHANGELOG.md`

## 13. Review Log

- [x] Principal Architect: APPROVED — `REV-ARCH-20260708-session-continuity-baseline.md`
- [x] Security Lead: APPROVED — `REV-SEC-20260708-session-continuity-baseline.md`
- [x] Performance Lead: APPROVED — `REV-PERF-20260708-session-continuity-baseline.md`
- [x] Cost Engineer: APPROVED — `REV-COST-20260708-session-continuity-baseline.md`
- [x] Simplifier: APPROVED — `REV-SIMP-20260708-session-continuity-baseline.md`
- [x] Documentation Reviewer: APPROVED — `REV-DOC-20260708-session-continuity-baseline.md`

## 14. Final Outcome

Accepted for v0.28 after maintainer approval and release-grade validation of the complete review set.
