# Agentic Development Manifest (ADM) — v0.19 Draft

Ein entstehender, modellneutraler Standard und ein dateibasiertes Betriebssystem für autonome Multi-Agenten-Softwareentwicklung.

## Was ist ADM?

ADM definiert einen standardisierten, dateibasierten Prozess für moderne KI-Coding-Agenten wie Claude Code CLI, Codex CLI, Antigravity, Gemini CLI und GPT-Modelle.

Statt langlebige Chatfenster offen zu halten, etabliert ADM Git, strukturierte Handovers, Architecture Decision Records, Reviews, project-owned memory, Agent Registry, Handover Automation und SaaS Foundation Standards als Single Source of Truth des Projekts.

Der Chat ist nur ein temporärer Arbeitsplatz. Das Repository ist die Wahrheit.

## Dokumentation

- `docs/VISION.md` — Vision und Philosophie
- `docs/CONSTITUTION.md` — 10 Kernprinzipien
- `docs/OPERATING_SYSTEM.md` — `.ai/` als dateibasiertes Betriebssystem
- `docs/MULTI_AGENT_PARLIAMENT.md` — Rollen und Entscheidungsprozess
- `docs/SAAS_FOUNDATION_BLUEPRINT.md` — technischer Roadmap-Phase-2 SaaS Foundation Standard
- `docs/REVIEW_VALIDATION.md` — Review-Validator und Gate-Modi
- `docs/REVIEW_RUNBOOK.md` — operativer Ablauf für vollständige Review-Sets
- `docs/REPOSITORY_GOVERNANCE.md` — Branch protection, merge path, and release gate policy
- `docs/decisions/ADR-20260708-project-owned-memory.md` — Project-owned Memory architecture decision
- `docs/decisions/ADR-20260708-agent-registry.md` — Agent Registry architecture decision
- `docs/decisions/ADR-20260708-handover-automation.md` — Handover Automation architecture decision
- `docs/decisions/ADR-20260708-saas-foundation-standard.md` — Roadmap Phase 2 SaaS Foundation Standard architecture decision
- `.ai/agents/README.md` — Agent Registry runtime policy
- `templates/HANDOVER_TEMPLATE.md` — reusable structured handover template
- `spec/ADM_v1_DRAFT.md` — Spezifikation und ACP

## Repository Governance

`main` is the protected integration branch. Changes should enter through pull requests and pass `ADM Quality Gate`.

The expected repository settings are documented in `docs/REPOSITORY_GOVERNANCE.md`.

## Status

v0.19 Draft. Project-owned memory, Agent Registry, Handover Automation, and Roadmap Phase 2 SaaS Foundation Standard architecture are accepted. The next major roadmap block is Roadmap Phase 3 AI Foundation Standard.
