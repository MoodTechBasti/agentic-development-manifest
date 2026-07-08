# ADM — Adapter Prompt Standard

> Origin: accepted in v0.22 as Roadmap Phase 5
> Current sync: v0.29 Tool Verification Discovery Baseline
> Scope: prompt-layer standard, not runtime integration

The Adapter Prompt Standard defines how ADM tool-specific adapter prompts may layer on top of the canonical Master Prompt without replacing it.

It is the canonical **Roadmap Phase 5** standard. Roadmap Phase 5 is not an implementation phase for runtime integrations, local tool profiles, provider SDKs, workflows, validators, release automation, or MCP servers.

## Architecture Philosophy

ADM treats adapter prompts as thin compatibility layers between a concrete CLI agent and the canonical ADM operating contract.

Mandatory principles:

1. The ADM specification remains the canonical rule source.
2. `docs/MASTER_PROMPT_STANDARD.md` defines the canonical master-prompt behavior.
3. `prompts/master_prompt.md` remains the canonical onboarding prompt.
4. Adapter prompts may add tool-specific usage guidance only when it preserves canonical ADM behavior.
5. Adapter prompts must not invent repository truth, checks, commits, roles, approvals, review votes, CI results, or completed work.
6. Adapter prompts must not treat hidden model memory, chat history, tool cache, local profile state, or proprietary tool context as authoritative project truth.
7. Adapter prompts must not bypass GitHub governance, CI, review validation, ADR requirements, release hygiene, or handover obligations.

## 1. Core Vocabulary

| Term | Meaning |
| --- | --- |
| `adapter_prompt` | Tool-specific prompt that starts from `prompts/master_prompt.md` and adds bounded tool instructions. |
| `canonical_prompt` | The repository-owned `prompts/master_prompt.md`. |
| `adapter_boundary` | The rule that adapter prompts may specialize operation but never weaken ADM authority, quality gates, or governance. |
| `tool_capability` | A concrete CLI feature such as planning, diff inspection, command execution, file editing, test execution, or review support. |
| `tool_state` | Local or vendor-owned state such as hidden memory, chat context, caches, session state, profiles, or slash-command history. |

Tool capabilities may assist work. Tool state is never repository truth.

## 2. Authority Order

Adapter prompts must preserve this authority order:

1. `spec/ADM_v1_DRAFT.md`, `docs/CONSTITUTION.md`, `ROADMAP.md`, governance docs, release docs, foundation standards, Master Prompt Standard, Adapter Prompt Standard, and accepted ADRs.
2. `prompts/master_prompt.md`.
3. Versioned runtime artifacts: `.ai/reviews/`, `.ai/handover/`, `.ai/decisions/`, `.ai/agents/`.
4. Curated project context: `.ai/memory/`, `.ai/knowledge/`, `.ai/tasks/`.
5. Tool-specific adapter prompt instructions, only where they do not conflict with higher authority.
6. Local transient files as non-authoritative working notes.
7. Chat history, hidden model memory, local tool profiles, and tool caches: never authoritative project truth.

If an adapter conflicts with `prompts/master_prompt.md`, the canonical master prompt wins.

## 3. Minimal Adapter Scope

An ADM-compliant adapter prompt must define:

- supported tool or tool family,
- required canonical prompt dependency,
- tool-specific capabilities the agent may use,
- tool-specific limitations and known risk boundaries,
- forbidden overrides,
- required initialization behavior,
- validation and reporting expectations,
- release-hygiene expectations,
- handover expectations,
- fallback behavior when tool behavior is unavailable or unclear.

An adapter prompt must be usable as a starting instruction for that tool without copying the whole ADM specification.

## 4. Required Adapter Shape

Each adapter prompt should use this structure:

1. Purpose.
2. Canonical dependency.
3. Tool-specific operating guidance.
4. Forbidden behavior.
5. Quality gate handling.
6. Release hygiene handling.
7. Handover handling.
8. Output expectations.

Adapter prompts should reference canonical files instead of duplicating their full contents.

## 5. Allowed Adapter Behavior

Adapter prompts may:

- tell an agent how to use a CLI's planning, inspection, diff, terminal, or file-editing features,
- require read-only repository inspection before changes,
- require small, reviewable edits,
- require evidence for checks and CI claims,
- warn about known tool-specific risk patterns,
- route the agent back to `prompts/master_prompt.md` when scope is unclear.

## 6. Forbidden Adapter Behavior

Adapter prompts must not:

- override ADM authority order,
- weaken required initialization,
- skip scope declaration,
- skip ADR triggers,
- skip review-set requirements,
- skip PR hygiene,
- skip release hygiene,
- skip local validation or mark unrun checks as passed,
- treat a tool's approval, plan mode, cache, memory, or local profile as repository approval,
- introduce provider secrets, local machine paths, private URLs, raw logs, or hidden context into the repository,
- create branches, commits, pull requests, release tags, workflow changes, validator changes, local tool profiles, runtime integrations, or MCP integrations unless the human maintainer explicitly approved that task scope.

## 7. Initial Adapter Set

Roadmap Phase 5 starts with a deliberately small adapter set:

| Adapter | Status | Reason |
| --- | --- | --- |
| Claude Code CLI | Initial adapter | High operational relevance and current usage. |
| Codex CLI | Initial adapter | Confirms model-neutral behavior across a second CLI agent. |
| Generic CLI Agent | Initial adapter | Safe fallback for unknown or future CLI tools. |
| Gemini CLI | Deferred candidate | Requires Tool Verification before any later adapter PR. |
| Antigravity CLI | Deferred candidate | Requires Tool Verification before any later adapter PR. |

Deferred candidates must not be treated as accepted adapter prompts until current tool behavior is verified, documented, reviewed, and a later explicit PR adds them.

## 8. Relationship to Master Prompt Standard

The Master Prompt Standard defines canonical behavior. The Adapter Prompt Standard defines how tool-specific prompts may consume that behavior.

Adapter prompts are downstream artifacts. They must not become a second specification, a second master prompt, or a workaround for ADM governance.

## 9. Relationship to AI Foundation Standard

Adapter prompts are not provider adapters and not AI runtime architecture.

They do not define provider abstraction, model routing, prompt registry, evaluation, caching, AI cost tracking, AI artifact lifecycle, tool execution, or safety rules beyond preserving existing ADM requirements.

## 10. Relationship to Governance, Review, and Release Hygiene

Adapter work affects agent onboarding semantics. Material adapter prompt changes require:

- an accepted ADR when adapter semantics change,
- documentation synchronization,
- a complete six-role review set for roadmap phase acceptance or governance-significant changes,
- local validation before PR-ready claims,
- release-grade complete-set validation before tagging,
- correct distinction between the reviewed target commit and the final tag commit.

## 11. Relationship to Tool Verification

Tool Verification is the Roadmap Phase 8 discovery and governance gate before deferred or future adapter acceptance.

Before proposing a new tool-specific adapter, agents must read `docs/TOOL_VERIFICATION.md` and show current evidence for tool identity, instruction model, repository access, planning behavior, edit behavior, command behavior, review behavior, tool-state boundaries, governance risks, and Generic CLI Agent fallback.

Tool Verification does not itself accept an adapter. It only establishes whether a later adapter PR is eligible for review.

## 12. Final Audit

Before accepting adapter prompt work, verify:

- canonical master prompt remains authoritative,
- no adapter weakens repository-backed truth,
- no adapter depends on hidden memory, chat history, tool cache, or local profile state,
- no adapter bypasses GitHub governance, CI, review validation, ADRs, PR hygiene, release hygiene, or handover duties,
- adapter set remains intentionally small,
- deferred or future adapters have current Tool Verification evidence before proposal,
- README, Roadmap, Changelog, Specification, Operating System, Master Prompt Standard, and prompt files are synchronized.
