# ADR-20260708-project-owned-memory

> ID: ADR-20260708-project-owned-memory
> Status: PROPOSED
> Last updated: 2026-07-08
> Owner: Principal Architect

## Status Overview

| Metric | Value |
| --- | --- |
| Confidence level | 9 |
| Affected modules | `docs/OPERATING_SYSTEM.md`, `.ai/README.md`, `spec/ADM_v1_DRAFT.md`, `prompts/master_prompt.md` |
| New dependencies | no |
| Security review | PENDING |
| Cost review | PENDING |
| Performance review | PENDING |

## 1. Context and Reason

ADM requires repository-backed truth. Agents must not reconstruct project state from hidden model memory, long-running chat windows, local scratch files, or vendor-specific tool state.

The repository already contains `.ai/` as a file-based operating layer, but the memory boundary is not explicit enough. Without a project-owned memory rule, future agents can mix durable project facts with transient notes, raw logs, private paths, or stale chat assumptions.

This ADR defines project-owned memory as an auditable, portable, repository-governed layer.

## 2. Decision

ADM adopts project-owned memory as a first-class architecture rule.

Project-owned memory is durable project knowledge that is owned by the repository, classified by purpose, and safe for future agents to read without depending on hidden model memory.

Authority order:

1. Canonical repository documents: specifications, constitution, governance docs, ADRs, runbooks.
2. Versioned runtime artifacts: completed reviews, handovers, accepted project decisions, curated memory notes.
3. Working artifacts: active tasks, planning notes, open questions, and research summaries.
4. Local transient artifacts: scratch files, logs, caches, prompt experiments, raw tool output.
5. Hidden model memory and chat history: never authoritative.

Directory ownership:

| Path | Purpose | Commit policy |
| --- | --- | --- |
| `docs/decisions/` | ADM standard architecture decisions | Versioned, reviewable |
| `.ai/decisions/` | Project-specific runtime decisions | Versioned only when future agents need them |
| `.ai/handover/` | Durable session handovers | Versioned when they describe meaningful state |
| `.ai/reviews/` | Completed review artifacts | Versioned when tied to a concrete scope |
| `.ai/memory/` | Curated durable memory notes | Versioned only after pruning and classification |
| `.ai/knowledge/` | Curated project knowledge and research summaries | Versioned only when source and confidence are clear |
| `.ai/tasks/` | Active or planned work state | Versioned when it coordinates future work |
| `.ai/tmp/`, `.ai/logs/`, `.ai/cache/`, `.ai/scratch/` | Local transient output | Never versioned |

Memory files must be concise, source-aware, and safe to share with any future repository agent.

## 3. Evidence

- The ADM master prompt already states that the repository is the source of truth and hidden model memory must not be used for project state.
- `docs/OPERATING_SYSTEM.md` already defines `.ai/` as a file-based control center with memory, tasks, decisions, reviews, and handovers.
- `.ai/README.md` already separates versioned governance artifacts from ignored transient local agent output.
- Prior release hardening established that governance-critical changes need durable review and release artifacts.

## 4. Alternatives

### Alternative A: Rely on chat memory and model memory

- Description: Agents continue from previous conversations and tool state without requiring explicit project-owned memory files.
- Reason for rejection: This is not portable, auditable, deterministic, or model-neutral. It also breaks handover between different CLI tools and agents.

### Alternative B: Store everything under `.ai/` by default

- Description: Every log, note, prompt, scratch result, and experiment is committed so future agents can inspect it.
- Reason for rejection: This pollutes the repository, leaks private context, increases review cost, and makes true project state harder to find.

### Alternative C: Keep only ADRs and handovers

- Description: The repository stores decisions and session summaries, but no curated memory or knowledge layer.
- Reason for rejection: ADRs and handovers are not enough for reusable project context, recurring constraints, vocabulary, known pitfalls, or stable research summaries.

## 5. Trade-offs

### Pros

- Improves handover quality across agents, tools, and chat windows.
- Keeps ADM model-neutral and repository-first.
- Reduces stale assumptions from hidden memory.
- Gives future validators and automation a clear target structure.
- Separates durable knowledge from transient tool noise.

### Cons

- Adds classification overhead for agents.
- Requires discipline to keep memory concise and current.
- Can create documentation debt if memory files are not pruned.
- May require later validator support to detect unsafe or stale memory artifacts.

## 6. Risks and Consequences

- Short-term risks: Agents may overuse `.ai/memory/` as a scratch directory.
- Long-term risks: Stale curated memory may become misleading if not reviewed.
- Mitigation plan: Keep transient directories ignored, document commit rules in `.ai/README.md`, and defer schema validation until the architecture is accepted.

## 7. ADM Exemptions

No ADM line-limit or quality-rule exemptions are introduced by this ADR.

## 8. Affected Files

- [x] `docs/decisions/ADR-20260708-project-owned-memory.md`
- [x] `spec/ADM_v1_DRAFT.md`
- [x] `docs/OPERATING_SYSTEM.md`
- [x] `.ai/README.md`
- [x] `prompts/master_prompt.md`
- [x] `README.md`
- [x] `ROADMAP.md`
- [x] `CHANGELOG.md`

## 9. Review Log

- [ ] Principal Architect: PENDING — review artifact required before acceptance.
- [ ] Devil's Advocate: PENDING — covered by Simplifier review artifact.
- [ ] Security Lead: PENDING — review artifact required before acceptance.
- [ ] Cost Engineer: PENDING — review artifact required before acceptance.
- [ ] Performance Lead: PENDING — review artifact required before acceptance.
- [ ] Simplifier: PENDING — review artifact required before acceptance.

## 10. Final Outcome

This ADR is proposed for v0.16. It should be promoted to ACCEPTED only after the v0.16 review set passes and the human maintainer approves the decision.