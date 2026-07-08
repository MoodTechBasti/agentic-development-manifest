# ADR-20260708-master-prompt-standard

> ID: ADR-20260708-master-prompt-standard
> Status: ACCEPTED
> Last updated: 2026-07-08
> Owner: Principal Architect

## Status Overview

| Metric | Value |
| --- | --- |
| Confidence level | 9 |
| Affected modules | `docs/MASTER_PROMPT_STANDARD.md`, `prompts/master_prompt.md`, `spec/ADM_v1_DRAFT.md`, `docs/OPERATING_SYSTEM.md`, `README.md`, `ROADMAP.md` |
| New dependencies | no |
| Security review | PASSED |
| Cost review | PASSED |
| Performance review | PASSED |

## 1. Context and Reason

ADM Roadmap Phase 2 established the SaaS Foundation Standard. Roadmap Phase 3 established the AI Foundation Standard.

The next roadmap gap is Roadmap Phase 4: Master Prompt. ADM already has `prompts/master_prompt.md`, but that file is an operational onboarding prompt, not yet a formally accepted standard for how the ADM specification is converted into a model-neutral CLI-agent instruction.

Without a Master Prompt Standard, future agents can change the prompt ad hoc, duplicate specification rules inconsistently, skip authority boundaries, or mix canonical ADM behavior with tool-specific adapter behavior.

This ADR accepts the Master Prompt Standard as the Roadmap Phase 4 architecture block. Roadmap phases in `ROADMAP.md` remain distinct from ADM lifecycle phases in `spec/ADM_v1_DRAFT.md`.

## 2. Decision

ADM adopts the Master Prompt Standard as the canonical Roadmap Phase 4 architecture block.

The standard defines the minimum behavior an ADM master prompt must provide before an agent starts implementation work:

| Area | Required decision |
| --- | --- |
| Authority order | How repository truth outranks chat history, hidden model memory, local scratch files, and tool caches. |
| Required initialization | Which repository documents and `.ai/` artifacts an agent must inspect before implementation. |
| Scope declaration | How an agent states role, task boundary, assumptions, exclusions, and next action before making changes. |
| Operating rules | Which facts, checks, commits, roles, reviews, approvals, and CI results must never be invented. |
| Decision rules | When ADRs are required and when minor edits should not be over-governed. |
| Quality gates | Which local checks and review validation duties apply before PR-ready or release-ready claims. |
| Review contract | How complete six-role review sets bind to `review_set_id`, `target_ref`, and stable `target_commit`. |
| Foundation triggers | When SaaS Foundation and AI Foundation standards become mandatory context. |
| Handover contract | How significant sessions end with evidence-based, repository-relative handovers. |
| Adapter boundary | How the canonical master prompt stays separate from tool-specific adapter prompts. |

The standard keeps a documentation-only posture. It does not require runtime code, provider integrations, CLI adapters, schema changes, validator changes, workflow changes, MCP integration, or tool-specific prompt profiles.

## 3. Scope Boundary

v0.21 is documentation, prompt hardening, ADR, specification sync, roadmap/changelog sync, and review artifacts only.

It does not add:

- runtime implementation,
- provider SDK integration,
- tool integration,
- CLI-specific adapter prompts,
- local tool profiles,
- MCP integration,
- database schema,
- validator enforcement,
- workflow changes,
- release automation,
- release tag.

Future PRs may define adapter prompts, schemas, validators, workflow support, or tool-specific profiles only after the Roadmap Phase 4 vocabulary remains stable and the maintainer explicitly approves that narrower scope.

## 4. Relationship to Prior Roadmap Phases

The Master Prompt Standard depends on prior ADM standards and operationalizes them.

Roadmap Phase 1 defines repository operating-system concepts: governance, project-owned memory, Agent Registry, Handover Automation, review validation, and release gates.

Roadmap Phase 2 defines SaaS Foundation boundaries: users, organizations, tenants, workspaces, memberships, roles, permissions, billing readiness, quotas, jobs, observability, admin diagnostics, data lifecycle, testing, and performance budgets.

Roadmap Phase 3 defines AI Foundation boundaries: provider abstraction, prompt registry, tool registry, evaluation, AI cost tracking, routing, fallback, caching, safety, observability, audit, and AI artifact lifecycle.

Roadmap Phase 4 does not replace those documents. It makes sure a fresh CLI-agent session is forced to read, respect, and report against them.

## 5. Relationship to Adapter Prompts

Adapter prompts are deliberately out of scope.

The canonical master prompt must remain model-neutral. It may be consumed by Claude Code, Codex, Gemini CLI, Antigravity, or another CLI-agent, but it must not depend on any one tool's hidden memory, proprietary permissions, slash commands, context-window behavior, or platform-specific syntax.

Tool-specific prompts belong to Roadmap Phase 5 or later adapter work.

## 6. Evidence

- `ROADMAP.md` defines Roadmap Phase 4 as converting the specification into a model-neutral CLI-agent master prompt.
- `prompts/master_prompt.md` already contains the core onboarding behavior, quality checks, PR hygiene, decision rules, SaaS Foundation rules, AI Foundation rules, handover rules, and reporting expectation.
- `spec/ADM_v1_DRAFT.md` already states that every agent must begin with `prompts/master_prompt.md`.
- `docs/OPERATING_SYSTEM.md` already defines the repository-owned runtime artifacts the prompt must route agents through.

## 7. Alternatives

### Alternative A: Only edit `prompts/master_prompt.md`

- Description: Harden the existing prompt without adding a standard document or ADR.
- Reason for rejection: Roadmap Phase 4 is a governance block. Treating it as a copy edit would break the pattern used for Roadmap Phase 2 and Roadmap Phase 3.

### Alternative B: Implement prompt validators now

- Description: Add schemas or validator enforcement for master-prompt sections.
- Reason for rejection: The semantics must be accepted first. Premature validator work could freeze unstable wording and create false confidence.

### Alternative C: Build tool-specific prompts immediately

- Description: Add separate prompts for Claude Code, Codex, Gemini CLI, Antigravity, or IDE agents in v0.21.
- Reason for rejection: That would mix canonical standard definition with adapter work. The roadmap reserves adapter prompts for later.

## 8. Trade-offs

### Pros

- Makes the master prompt a first-class ADM standard instead of an informal prompt file.
- Reduces agent drift during fresh-context sessions.
- Preserves model neutrality and CLI-first behavior.
- Creates a clean boundary between canonical prompt behavior and future adapter prompts.
- Gives future validators a stable target without enforcing it yet.

### Cons

- Adds another documentation surface to maintain.
- Can increase onboarding overhead if agents treat every listed document as equally relevant for tiny tasks.
- May need future pruning if the prompt becomes too long or repetitive.

## 9. Risks and Consequences

- Short-term risk: Agents may over-read or over-report for small changes.
- Long-term risk: Tool-specific assumptions may leak into the canonical master prompt.
- Governance risk: Agents may confuse Roadmap Phase 4 Master Prompt with Lifecycle Phase 4 Simplification.
- Mitigation plan: Keep v0.21 documentation-only, explicitly preserve the Roadmap/Lifecycle distinction, and defer adapter prompts, schemas, validators, workflows, and runtime integrations.

## 10. ADM Exemptions

No ADM line-limit or quality-rule exemptions are introduced by this ADR.

## 11. Affected Files

- [x] `docs/decisions/ADR-20260708-master-prompt-standard.md`
- [x] `docs/MASTER_PROMPT_STANDARD.md`
- [x] `prompts/master_prompt.md`
- [x] `spec/ADM_v1_DRAFT.md`
- [x] `docs/OPERATING_SYSTEM.md`
- [x] `README.md`
- [x] `ROADMAP.md`
- [x] `CHANGELOG.md`

## 12. Review Log

- [x] Principal Architect: APPROVED — `REV-ARCH-20260708-master-prompt-standard.md`
- [x] Security Lead: APPROVED — `REV-SEC-20260708-master-prompt-standard.md`
- [x] Performance Lead: APPROVED — `REV-PERF-20260708-master-prompt-standard.md`
- [x] Cost Engineer: APPROVED — `REV-COST-20260708-master-prompt-standard.md`
- [x] Simplifier: APPROVED — `REV-SIMP-20260708-master-prompt-standard.md`
- [x] Documentation Reviewer: APPROVED — `REV-DOC-20260708-master-prompt-standard.md`

## 13. Final Outcome

Accepted for v0.21 after maintainer approval and successful validation of the full review set.
