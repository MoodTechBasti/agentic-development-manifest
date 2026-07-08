# ADR-20260708-adapter-prompt-standard

> ID: ADR-20260708-adapter-prompt-standard
> Status: ACCEPTED
> Last updated: 2026-07-08
> Owner: Principal Architect

## Status Overview

| Metric | Value |
| --- | --- |
| Confidence level | 9 |
| Affected modules | `docs/ADAPTER_PROMPT_STANDARD.md`, `prompts/adapters/`, `docs/MASTER_PROMPT_STANDARD.md`, `prompts/master_prompt.md`, `spec/ADM_v1_DRAFT.md`, `docs/OPERATING_SYSTEM.md`, `README.md`, `ROADMAP.md` |
| New dependencies | no |
| Security review | PASSED |
| Cost review | PASSED |
| Performance review | PASSED |

## 1. Context and Reason

ADM Roadmap Phase 4 accepted the Master Prompt Standard as the canonical model-neutral onboarding contract for CLI agents.

The next roadmap gap is Roadmap Phase 5: Adapters. ADM already states that tool-specific prompts belong outside the canonical master prompt. Without an Adapter Prompt Standard, future adapter prompts can duplicate canonical rules inconsistently, weaken governance, rely on hidden tool memory, or smuggle CLI-specific behavior into `prompts/master_prompt.md`.

This ADR accepts the Adapter Prompt Standard as the Roadmap Phase 5 architecture block. Roadmap phases in `ROADMAP.md` remain distinct from ADM lifecycle phases in `spec/ADM_v1_DRAFT.md`.

## 2. Decision

ADM adopts the Adapter Prompt Standard as the canonical Roadmap Phase 5 architecture block.

The standard defines a thin adapter layer for tool-specific prompts. Adapter prompts must build on:

1. `spec/ADM_v1_DRAFT.md`,
2. `docs/MASTER_PROMPT_STANDARD.md`,
3. `prompts/master_prompt.md`,
4. accepted ADRs and governance documents.

The initial accepted adapter set is deliberately small:

| Adapter | Decision |
| --- | --- |
| `prompts/adapters/claude_code_cli.md` | Accepted initial adapter. |
| `prompts/adapters/codex_cli.md` | Accepted initial adapter. |
| `prompts/adapters/generic_cli_agent.md` | Accepted initial fallback adapter. |

Gemini CLI and Antigravity CLI remain deferred candidates. They may be added later only after current tool behavior is verified and the maintainer explicitly approves that narrower scope.

## 3. Scope Boundary

v0.22 is documentation, prompt adapter, ADR, specification sync, roadmap/changelog sync, and review artifacts only.

It does not add:

- runtime implementation,
- provider SDK integration,
- tool integration,
- local tool profiles,
- MCP integration,
- database schema,
- validator enforcement,
- workflow changes,
- release automation,
- release tag,
- Gemini CLI adapter,
- Antigravity CLI adapter,
- provider secrets.

Future PRs may add more adapter prompts, schema support, validators, workflow support, local tool profiles, or runtime integrations only after this adapter vocabulary remains stable and the maintainer explicitly approves that narrower scope.

## 4. Adapter Authority

Adapter prompts are downstream from the canonical ADM documents.

They may explain how a concrete CLI agent should operate, but they must not override:

- repository-backed truth,
- required initialization,
- scope declaration,
- ADR triggers,
- review governance,
- release governance,
- PR hygiene,
- quality checks,
- handover duties,
- SaaS Foundation boundaries,
- AI Foundation boundaries,
- Master Prompt Standard boundaries.

If an adapter prompt conflicts with `prompts/master_prompt.md`, the canonical master prompt wins.

## 5. Evidence

- `ROADMAP.md` defines Roadmap Phase 5 as adapter prompts for specific CLI tools after the canonical standard is stable.
- `docs/MASTER_PROMPT_STANDARD.md` explicitly reserves Claude-, Codex-, Gemini-, Antigravity-, IDE-, MCP-, and provider-specific behavior for later adapter work.
- `prompts/master_prompt.md` already forbids smuggling Claude-, Codex-, Gemini-, Antigravity-, IDE-, MCP-, or provider-specific behavior into the canonical master prompt.
- `spec/ADM_v1_DRAFT.md` already states that hidden model memory and chat history are never authoritative project truth.
- Project-owned Memory, Agent Registry, Handover Automation, and Review Governance already define the operating boundaries adapter prompts must preserve.

## 6. Alternatives

### Alternative A: Add all named adapters immediately

- Description: Add Claude Code CLI, Codex CLI, Gemini CLI, Antigravity CLI, and generic adapters in one PR.
- Reason for rejection: Too broad. Gemini CLI and Antigravity CLI need current tool-behavior verification before accepted specialization.

### Alternative B: Only add a generic adapter

- Description: Avoid tool-specific adapters and provide only a generic CLI-agent prompt.
- Reason for rejection: Roadmap Phase 5 exists to prove that concrete CLI adapters can layer on ADM without weakening the canonical prompt.

### Alternative C: Put tool-specific guidance into `prompts/master_prompt.md`

- Description: Expand the canonical master prompt with Claude, Codex, Gemini, and Antigravity sections.
- Reason for rejection: This breaks the adapter boundary accepted in Roadmap Phase 4 and makes the canonical prompt vendor/tool-specific.

### Alternative D: Implement adapter validators now

- Description: Add schemas or validators for adapter prompt structure.
- Reason for rejection: The adapter vocabulary and file layout should be accepted before enforcement is designed.

## 7. Trade-offs

### Pros

- Keeps the canonical master prompt stable and model-neutral.
- Gives concrete CLI agents usable starting prompts without duplicating ADM rules.
- Reduces risk of hidden memory, chat history, or tool cache becoming project truth.
- Preserves governance, reviews, CI, ADRs, and handover obligations.
- Provides a safe generic fallback for unknown CLI agents.

### Cons

- Adds another documentation surface to keep synchronized.
- Adapter prompts can drift if they copy too much canonical text.
- Tool behavior may change faster than ADM documentation.
- Future maintainers may be tempted to add every new CLI immediately.

## 8. Risks and Consequences

- Short-term risk: Agents may confuse adapter guidance with canonical ADM authority.
- Long-term risk: Adapter prompts may duplicate the master prompt and become stale.
- Security risk: Tool-specific hidden memory, cache, local profile state, or permission behavior may be treated as trusted project state.
- Governance risk: Adapter prompts may be used to bypass review, ADR, CI, PR hygiene, or handover rules.
- Mitigation plan: Keep adapters thin, require canonical prompt dependency, defer unstable candidates, and preserve complete review and release validation.

## 9. ADM Exemptions

No ADM line-limit or quality-rule exemptions are introduced by this ADR.

## 10. Affected Files

- [x] `docs/decisions/ADR-20260708-adapter-prompt-standard.md`
- [x] `docs/ADAPTER_PROMPT_STANDARD.md`
- [x] `prompts/adapters/README.md`
- [x] `prompts/adapters/claude_code_cli.md`
- [x] `prompts/adapters/codex_cli.md`
- [x] `prompts/adapters/generic_cli_agent.md`
- [x] `docs/MASTER_PROMPT_STANDARD.md`
- [x] `prompts/master_prompt.md`
- [x] `spec/ADM_v1_DRAFT.md`
- [x] `docs/OPERATING_SYSTEM.md`
- [x] `README.md`
- [x] `ROADMAP.md`
- [x] `CHANGELOG.md`

## 11. Review Log

- [x] Principal Architect: APPROVED — `REV-ARCH-20260708-adapter-prompt-standard.md`
- [x] Security Lead: APPROVED — `REV-SEC-20260708-adapter-prompt-standard.md`
- [x] Performance Lead: APPROVED — `REV-PERF-20260708-adapter-prompt-standard.md`
- [x] Cost Engineer: APPROVED — `REV-COST-20260708-adapter-prompt-standard.md`
- [x] Simplifier: APPROVED — `REV-SIMP-20260708-adapter-prompt-standard.md`
- [x] Documentation Reviewer: APPROVED — `REV-DOC-20260708-adapter-prompt-standard.md`

## 12. Final Outcome

Accepted for v0.22 after maintainer approval and successful validation of the full review set.
