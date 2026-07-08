# Agentic Development Manifest (ADM) — v0.1 Draft

Ein entstehender, modellneutraler Standard und ein dateibasiertes Betriebssystem für autonome Multi-Agenten-Softwareentwicklung.

## Was ist ADM?

ADM definiert einen standardisierten, dateibasierten Prozess für moderne KI-Coding-Agenten wie Claude Code CLI, Codex CLI, Antigravity, Gemini CLI und GPT-Modelle.

Statt langlebige Chatfenster offen zu halten, etabliert ADM Git, strukturierte Handovers und Architecture Decision Records als Single Source of Truth des Projekts.

Der Chat ist nur ein temporärer Arbeitsplatz. Das Repository ist die Wahrheit.

## Dokumentation

- `docs/VISION.md` — Vision und Philosophie
- `docs/CONSTITUTION.md` — 10 Kernprinzipien
- `docs/OPERATING_SYSTEM.md` — `.ai/` als dateibasiertes Betriebssystem
- `docs/MULTI_AGENT_PARLIAMENT.md` — Rollen und Entscheidungsprozess
- `docs/SAAS_FOUNDATION_BLUEPRINT.md` — technischer SaaS-Blueprint
- `docs/REVIEW_VALIDATION.md` — Review-Validator und Gate-Modi
- `docs/REVIEW_RUNBOOK.md` — operativer Ablauf für vollständige Review-Sets
- `docs/REPOSITORY_GOVERNANCE.md` — Branch protection, merge path, and release gate policy
- `spec/ADM_v1_DRAFT.md` — Spezifikation und ACP

## Repository Governance

`main` is the protected integration branch. Changes should enter through pull requests and pass `ADM Quality Gate`.

The expected repository settings are documented in `docs/REPOSITORY_GOVERNANCE.md`.

## Status

v0.1 Draft. Noch kein stabiler Standard.
