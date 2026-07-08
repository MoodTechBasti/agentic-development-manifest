---
template_id: ADM-TMP-REV-SEC
template_type: review
review_type: security
role: Security Engineer
template_status: accepted
version: 1.2.0
last_updated: 2026-07-08
runtime_target: .ai/reviews/
review_id: REV-SEC-20260708-adapter-prompt-standard
review_set_id: RSV-20260708-adapter-prompt-standard
target_ref: adm-v022-adapter-prompt-standard
target_commit: 9a04eb2bbd6770848fddac5afc2813cdec498977
review_status: PASSED
review_date: 2026-07-08
reviewer_agent: Security Engineer
target: v0.22 Roadmap Phase 5 Adapter Prompt Standard
target_files: [docs/decisions/ADR-20260708-adapter-prompt-standard.md, docs/ADAPTER_PROMPT_STANDARD.md, prompts/adapters/README.md, prompts/adapters/claude_code_cli.md, prompts/adapters/codex_cli.md, prompts/adapters/generic_cli_agent.md, docs/MASTER_PROMPT_STANDARD.md, prompts/master_prompt.md, spec/ADM_v1_DRAFT.md, docs/OPERATING_SYSTEM.md, README.md, ROADMAP.md, CHANGELOG.md]
ci_ready: true
confidence_score: 9
---

# Security Review: v0.22 Adapter Prompt Standard

## Scope

Reviewed adapter authority, hidden-memory boundaries, local tool-state handling, forbidden overrides, and the absence of runtime or secret-bearing configuration.

## Findings

- Strengths: The standard explicitly rejects hidden model memory, chat history, tool cache, and local profile state as authoritative project truth.
- Strengths: Adapter prompts are not allowed to bypass GitHub governance, CI, review validation, ADRs, PR hygiene, or handover duties.
- Strengths: No secrets, provider credentials, local tool profiles, MCP integration, runtime code, or provider SDK integration are introduced.
- Strengths: Deferred candidates reduce the risk of encoding unverified Gemini CLI or Antigravity CLI behavior.
- Risk: Future maintainers may treat a tool's local permission or plan state as approval if adapter boundaries are weakened.

## Security Gates

- [x] No secrets or credentials introduced.
- [x] No provider or tool integration introduced.
- [x] No local tool profile or permission engine introduced.
- [x] No weakening of repository-backed truth or handover evidence rules.

## Review Vote

- Vote: APPROVED
- CI-ready: true
