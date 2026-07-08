# Agentic Development Manifest (ADM) — v0.30 Draft

Ein entstehender, modellneutraler Standard und ein dateibasiertes Betriebssystem für autonome Multi-Agenten-Softwareentwicklung.

## Was ist ADM?

ADM definiert einen standardisierten, dateibasierten Prozess für moderne KI-Coding-Agenten wie Claude Code CLI, Codex CLI, Antigravity, Gemini CLI und GPT-Modelle.

Statt langlebige Chatfenster offen zu halten, etabliert ADM Git, strukturierte Handovers, Session Continuity, Architecture Decision Records, Reviews, project-owned memory, Agent Registry, Handover Automation, SaaS Foundation Standards, AI Foundation Standards, Master Prompt Standards, Adapter Prompt Standards, Roadmap Continuation, v1-Readiness-Kriterien, Review and Validation Hardening, Foundation Consistency and Release Hygiene, Review Archive Policy sowie Review Archive Migration als Single Source of Truth des Projekts.

Der Chat ist nur ein temporärer Arbeitsplatz. Das Repository ist die Wahrheit. Deferred oder zukünftige Tool-Adapter benötigen Tool Verification, bevor sie als Adapter-PR geeignet sind.

## Dokumentation

- `docs/VISION.md` — Vision und Philosophie
- `docs/CONSTITUTION.md` — 10 Kernprinzipien
- `docs/OPERATING_SYSTEM.md` — `.ai/` als dateibasiertes Betriebssystem
- `docs/MULTI_AGENT_PARLIAMENT.md` — Rollen und Entscheidungsprozess
- `docs/SAAS_FOUNDATION_BLUEPRINT.md` — technischer Roadmap-Phase-2 SaaS Foundation Standard
- `docs/AI_FOUNDATION_STANDARD.md` — technischer Roadmap-Phase-3 AI Foundation Standard
- `docs/MASTER_PROMPT_STANDARD.md` — technischer Roadmap-Phase-4 Master Prompt Standard
- `docs/ADAPTER_PROMPT_STANDARD.md` — technischer Roadmap-Phase-5 Adapter Prompt Standard
- `docs/TOOL_VERIFICATION.md` — Roadmap-Phase-8 Discovery- und Governance-Gate für deferred/future Adapter
- `docs/REVIEW_VALIDATION.md` — Review-Validator und Gate-Modi
- `docs/REVIEW_RUNBOOK.md` — operativer Ablauf für vollständige Review-Sets
- `docs/RELEASE_RUNBOOK.md` — manueller Release-Validierungs- und Tagging-Ablauf
- `docs/REPOSITORY_GOVERNANCE.md` — Branch protection, merge path, ruleset audit, and release gate policy
- `docs/decisions/ADR-20260708-project-owned-memory.md` — Project-owned Memory architecture decision
- `docs/decisions/ADR-20260708-agent-registry.md` — Agent Registry architecture decision
- `docs/decisions/ADR-20260708-handover-automation.md` — Handover Automation architecture decision
- `docs/decisions/ADR-20260708-saas-foundation-standard.md` — Roadmap Phase 2 SaaS Foundation Standard architecture decision
- `docs/decisions/ADR-20260708-ai-foundation-standard.md` — Roadmap Phase 3 AI Foundation Standard architecture decision
- `docs/decisions/ADR-20260708-master-prompt-standard.md` — Roadmap Phase 4 Master Prompt Standard architecture decision
- `docs/decisions/ADR-20260708-adapter-prompt-standard.md` — Roadmap Phase 5 Adapter Prompt Standard architecture decision
- `docs/decisions/ADR-20260708-roadmap-continuation-v1-readiness.md` — Roadmap continuation and v1 readiness architecture decision
- `docs/decisions/ADR-20260708-review-validation-hardening-baseline.md` — Roadmap Phase 6 review and validation hardening baseline decision
- `docs/decisions/ADR-20260708-foundation-consistency-release-hygiene-baseline.md` — Foundation consistency and release hygiene baseline decision
- `docs/decisions/ADR-20260708-review-archive-policy.md` — Review Archive Policy baseline decision
- `docs/decisions/ADR-20260708-review-archive-migration-batch-1.md` — Review Archive Migration Batch 1 decision
- `docs/decisions/ADR-20260708-session-continuity-baseline.md` — Roadmap Phase 7 Session Continuity Baseline decision
- `docs/decisions/ADR-20260708-tool-verification-discovery-baseline.md` — Roadmap Phase 8 Tool Verification Discovery Baseline decision
- `docs/decisions/ADR-20260708-review-archive-migration-batch-2.md` — Review Archive Migration Batch 2 decision
- `.ai/agents/README.md` — Agent Registry runtime policy
- `.ai/handover/README.md` — Handover discovery and Session Continuity policy
- `templates/HANDOVER_TEMPLATE.md` — reusable structured handover template
- `prompts/adapters/` — tool-specific adapter prompts layered below the canonical master prompt
- `spec/ADM_v1_DRAFT.md` — Spezifikation und ACP

## Repository Governance

`main` is the protected integration branch. Changes should enter through pull requests and pass `ADM Quality Gate`.

The expected repository settings are documented in `docs/REPOSITORY_GOVERNANCE.md`. GitHub rulesets are external settings and must be manually audited before governance-relevant releases.

## Status

v0.30 Draft. Project-owned memory, Agent Registry, Handover Automation, Roadmap Phase 2 SaaS Foundation Standard, Roadmap Phase 3 AI Foundation Standard, Roadmap Phase 4 Master Prompt Standard, Roadmap Phase 5 Adapter Prompt Standard, Roadmap Continuation with v1 Readiness Criteria, Roadmap Phase 6 Review and Validation Hardening Baseline, Foundation Consistency and Release Hygiene Baseline, Review Archive Policy, Review Archive Migration Batch 1, Roadmap Phase 7 Session Continuity Baseline architecture, Roadmap Phase 8 Tool Verification Discovery Baseline, and Review Archive Migration Batch 2 are accepted.

v0.26 defines the Review Archive Policy baseline. Historical review sets may live under `.ai/reviews/archive/<review_set_id>/`, and the standard validator path continues to validate direct `.ai/reviews/*.md` files only.

v0.27 migrates completed historical review sets up to v0.25 into `.ai/reviews/archive/<review_set_id>/` while keeping the current v0.26 review set active under `.ai/reviews/`.

v0.28 defines repository-owned Session Continuity for future agents. New sessions must derive continuation state from canonical repository documents, `.ai/handover/`, reviews, tasks, memory, decisions, and agent registry evidence before using transient chat or model context.

v0.29 defines Tool Verification as a required discovery and governance gate before deferred or future adapter prompts. Gemini CLI and Antigravity CLI remain deferred candidates.

v0.30 migrates the completed v0.26 Review Archive Policy, v0.27 Review Archive Migration Batch 1, and v0.28 Session Continuity Baseline review sets into `.ai/reviews/archive/<review_set_id>/` while keeping v0.29 as the active release evidence under `.ai/reviews/`.

v0.30 does not implement Gemini CLI adapter, Antigravity CLI adapter, any other new adapter, runtime code, MCP integration, provider SDKs, local tool profiles, workflow changes, validator changes, release automation, Handover linting, branch-protection changes, review index generation, additional review archive migration beyond Batch 2, Phase 9 work, or a v1 release candidate.
