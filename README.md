# Agentic Development Manifest (ADM) — v0.24 Draft

Ein entstehender, modellneutraler Standard und ein dateibasiertes Betriebssystem für autonome Multi-Agenten-Softwareentwicklung.

## Was ist ADM?

ADM definiert einen standardisierten, dateibasierten Prozess für moderne KI-Coding-Agenten wie Claude Code CLI, Codex CLI, Antigravity, Gemini CLI und GPT-Modelle.

Statt langlebige Chatfenster offen zu halten, etabliert ADM Git, strukturierte Handovers, Architecture Decision Records, Reviews, project-owned memory, Agent Registry, Handover Automation, SaaS Foundation Standards, AI Foundation Standards, Master Prompt Standards, Adapter Prompt Standards, Roadmap Continuation, v1-Readiness-Kriterien sowie Review and Validation Hardening als Single Source of Truth des Projekts.

Der Chat ist nur ein temporärer Arbeitsplatz. Das Repository ist die Wahrheit.

## Dokumentation

- `docs/VISION.md` — Vision und Philosophie
- `docs/CONSTITUTION.md` — 10 Kernprinzipien
- `docs/OPERATING_SYSTEM.md` — `.ai/` als dateibasiertes Betriebssystem
- `docs/MULTI_AGENT_PARLIAMENT.md` — Rollen und Entscheidungsprozess
- `docs/SAAS_FOUNDATION_BLUEPRINT.md` — technischer Roadmap-Phase-2 SaaS Foundation Standard
- `docs/AI_FOUNDATION_STANDARD.md` — technischer Roadmap-Phase-3 AI Foundation Standard
- `docs/MASTER_PROMPT_STANDARD.md` — technischer Roadmap-Phase-4 Master Prompt Standard
- `docs/ADAPTER_PROMPT_STANDARD.md` — technischer Roadmap-Phase-5 Adapter Prompt Standard
- `docs/REVIEW_VALIDATION.md` — Review-Validator und Gate-Modi
- `docs/REVIEW_RUNBOOK.md` — operativer Ablauf für vollständige Review-Sets
- `docs/REPOSITORY_GOVERNANCE.md` — Branch protection, merge path, and release gate policy
- `docs/decisions/ADR-20260708-project-owned-memory.md` — Project-owned Memory architecture decision
- `docs/decisions/ADR-20260708-agent-registry.md` — Agent Registry architecture decision
- `docs/decisions/ADR-20260708-handover-automation.md` — Handover Automation architecture decision
- `docs/decisions/ADR-20260708-saas-foundation-standard.md` — Roadmap Phase 2 SaaS Foundation Standard architecture decision
- `docs/decisions/ADR-20260708-ai-foundation-standard.md` — Roadmap Phase 3 AI Foundation Standard architecture decision
- `docs/decisions/ADR-20260708-master-prompt-standard.md` — Roadmap Phase 4 Master Prompt Standard architecture decision
- `docs/decisions/ADR-20260708-adapter-prompt-standard.md` — Roadmap Phase 5 Adapter Prompt Standard architecture decision
- `docs/decisions/ADR-20260708-roadmap-continuation-v1-readiness.md` — Roadmap continuation and v1 readiness architecture decision
- `docs/decisions/ADR-20260708-review-validation-hardening-baseline.md` — Roadmap Phase 6 review and validation hardening baseline decision
- `.ai/agents/README.md` — Agent Registry runtime policy
- `templates/HANDOVER_TEMPLATE.md` — reusable structured handover template
- `prompts/adapters/` — tool-specific adapter prompts layered below the canonical master prompt
- `spec/ADM_v1_DRAFT.md` — Spezifikation und ACP

## Repository Governance

`main` is the protected integration branch. Changes should enter through pull requests and pass `ADM Quality Gate`.

The expected repository settings are documented in `docs/REPOSITORY_GOVERNANCE.md`.

## Status

v0.24 Draft. Project-owned memory, Agent Registry, Handover Automation, Roadmap Phase 2 SaaS Foundation Standard, Roadmap Phase 3 AI Foundation Standard, Roadmap Phase 4 Master Prompt Standard, Roadmap Phase 5 Adapter Prompt Standard, Roadmap Continuation with v1 Readiness Criteria, and Roadmap Phase 6 Review and Validation Hardening Baseline architecture are accepted. Roadmap Phase 6 preserves the existing `advisory`, `existing-strict`, and `complete-set` validation distinction, normalizes implemented ADR status, and adds targeted scope-filtering regression coverage without workflow hardening, release automation, runtime code, MCP integration, provider SDKs, or adapter expansion. Gemini CLI and Antigravity CLI remain deferred adapter candidates.
