# ADM — Master Prompt Standard (v0.21 Draft)

Der Master Prompt Standard definiert, wie die ADM-Spezifikation in eine modellneutrale Startanweisung für CLI-Agenten übersetzt wird.

Er ist der kanonische **Roadmap-Phase-4-Standard**. Diese Roadmap-Phase ist nicht identisch mit **Lifecycle Phase 4 — Simplification** aus `spec/ADM_v1_DRAFT.md`.

Ziel ist kein Tool-Adapter und kein Anbieterprofil. Ziel ist ein kleiner, überprüfbarer Master Prompt, der jedem Agenten vor Arbeitsbeginn dieselben Autoritäten, Grenzen, Qualitätsregeln und Übergabepflichten gibt.

## Architektur-Philosophie

ADM behandelt den Master Prompt als ausführbare Arbeitsvereinbarung zwischen Repository und Agent.

Pflichtprinzipien:

1. Die Spezifikation bleibt die kanonische Regelquelle.
2. Der Master Prompt übersetzt Regeln in operative Agentenschritte.
3. Der Prompt bleibt modellneutral und CLI-first.
4. Der Prompt darf keine Repository-Wahrheit erfinden.
5. Der Prompt muss Scope, Rolle, Checks, Reviews und Handover erzwingen.
6. Der Prompt darf keine Runtime-, Provider-, Workflow- oder Validator-Änderung implizieren.

## 1. Kernbegriffe

| Begriff | Bedeutung |
| --- | --- |
| `master_prompt` | Modellneutrale Startanweisung für Agenten in ADM-kontrollierten Repositories. |
| `agent_onboarding` | Initialisierungsschritte, die ein Agent vor Umsetzung oder Review ausführt. |
| `authority_order` | Rangfolge der Quellen, aus denen ein Agent Projektwahrheit ableitet. |
| `scope_declaration` | Explizite Aussage zu Rolle, Ziel, Grenzen, Annahmen und nächster Aktion. |
| `quality_gate_contract` | Pflicht, relevante Checks, Review-Regeln und CI-Readiness nachvollziehbar zu behandeln. |
| `handover_contract` | Pflicht, signifikante Sitzungen mit prüfbarer Übergabe zu beenden. |
| `adapter_prompt` | Tool- oder providerspezifischer Prompt für eine konkrete CLI oder Plattform. |

ADM-konforme Projekte müssen diese Begriffe nicht identisch benennen, aber ihre Entsprechungen müssen dokumentiert und konsistent verwendet werden.

## 2. Minimaler Master-Prompt-Scope

Ein ADM-konformer Master Prompt muss mindestens folgende Bereiche abdecken:

- Rolle und Grundauftrag des Agenten.
- Autoritätsmodell und Repository-backed Truth.
- Pflichtlektüre und Initialisierungsreihenfolge.
- Scope-, Rollen-, Annahmen- und Plan-Deklaration vor Umsetzung.
- Betriebsregeln gegen erfundene Fakten, Checks, Rollen, Commits, Review-Votes oder CI-Ergebnisse.
- Entscheidungskriterien für ADRs.
- PR-Ready-Checks und Review-Validierung.
- Handover-Pflichten und Handover-Grenzen.
- SaaS-Foundation-Trigger.
- AI-Foundation-Trigger.
- Verbot von Provider-, Tool-, Runtime-, Workflow- oder Validator-Scope-Creep ohne explizites GO.

## 3. Autoritätsmodell

Der Master Prompt muss Agenten zwingen, Projektzustand aus versionierten oder explizit zulässigen Repository-Artefakten abzuleiten.

Rangfolge:

1. `spec/ADM_v1_DRAFT.md`, `docs/CONSTITUTION.md`, Roadmap, Governance-Dokumente und accepted ADRs.
2. Versionierte Runtime-Artefakte wie `.ai/reviews/`, `.ai/handover/`, `.ai/decisions/`, `.ai/agents/`.
3. Kuratierte Projektkontexte wie `.ai/memory/`, `.ai/knowledge/`, `.ai/tasks/`.
4. Lokale transiente Dateien nur als nicht-kanonische Arbeitshilfe.
5. Chatverlauf, hidden model memory und Tool-Cache niemals als Projektwahrheit.

Der Prompt darf den Agenten nicht auffordern, fehlende Repository-Wahrheit aus Erinnerung zu rekonstruieren.

## 4. Pflichtstruktur

Ein ADM Master Prompt sollte diese Abschnitte enthalten:

1. Role.
2. Required initialization.
3. Operating rules.
4. Quality checks.
5. PR hygiene.
6. Decision rules.
7. Foundation-specific rules.
8. Handover rules.
9. Output expectation.

Projektindividuelle Ergänzungen sind erlaubt, wenn sie die kanonischen ADM-Regeln nicht abschwächen.

## 5. Initialisierung

Vor Änderungen muss ein Agent mindestens prüfen:

- README und Status des Repositories.
- Constitution, Operating System, Governance und Release-Regeln.
- ADM-Spezifikation.
- Multi-Agent Parliament oder gleichwertige Rollenbeschreibung.
- Relevante Foundation-Standards.
- Agent Registry, wenn vorhanden und relevant.
- Aktive Tasks, letzter Handover, kuratierte Memory und accepted Decisions, wenn vorhanden und relevant.

Die Initialisierung darf nicht als mechanisches Abhaken ohne Relevanzprüfung verstanden werden. Der Agent muss daraus Scope, Annahmen und Risiken ableiten.

## 6. Scope-Deklaration

Vor Implementierung muss ein Agent seine Arbeitsgrenze nennen:

- aktive Rolle oder Rollenfamilie,
- Ziel der Sitzung,
- betroffene Dokumente oder Codebereiche,
- ausdrücklich ausgeschlossene Bereiche,
- Annahmen und Unsicherheiten,
- nächster geplanter Schritt.

Bei unklarem Scope muss der Agent erst lesen, prüfen und planen. Implementierung ohne Scope-Verständnis ist nicht ADM-konform.

## 7. Decision Rules

Der Master Prompt muss eine ADR-Pflicht auslösen, wenn eine Änderung:

- Architektur oder Modulgrenzen verändert,
- Governance, Review, Release oder Handover-Semantik verändert,
- SaaS Foundation oder AI Foundation Semantik verändert,
- Security, Tenant Isolation, Billing, Cost, Data Lifecycle oder Provider-Verhalten betrifft,
- eine Qualitätsregel ausnimmt,
- erforderliche Checks bewusst überspringt.

Der Prompt darf kleinere Textkorrekturen nicht unnötig zu ADR-pflichtigen Architekturentscheidungen aufblasen.

## 8. Quality Gate Contract

Der Master Prompt muss den Agenten verpflichten, vor Merge- oder PR-Ready-Aussagen belegbare Checks zu nennen.

Mindest-Checks im ADM-Repository:

```bash
python3 scripts/check_limits.py --path . --max-lines 300
python3 scripts/test_validate_reviews.py
python3 scripts/validate_reviews.py --path . --mode existing-strict
```

Für Governance-Änderungen, Roadmap-Phasenübergänge oder Releases ist zusätzlich ein vollständiges Review-Set mit `complete-set`-Validierung erforderlich.

Nicht ausgeführte Checks müssen als `NOT RUN` oder gleichwertig markiert werden. Ein Agent darf sie nicht als bestanden melden.

## 9. Review Contract

Der Master Prompt muss Review-Artefakte als versionierte Runtime-Historie behandeln, nicht als informelle Chat-Bewertung.

Ein vollständiges Review-Set umfasst:

- Architect Review.
- Security Review.
- Performance Review.
- Cost Review.
- Simplifier Review.
- Documentation Review.

Review-Artefakte müssen auf denselben `review_set_id`, `target_ref` und stabilen `target_commit` gebunden sein.

## 10. Foundation Trigger

Der Prompt muss Aufgaben erkennen, die zusätzliche Foundation-Dokumente relevant machen.

SaaS-bezogene Aufgaben müssen den SaaS Foundation Standard beachten, wenn sie User, Tenant, Permissions, Billing, Quotas, Jobs, Observability, Admin, Data Lifecycle, Tests oder Performance Budgets betreffen.

AI-bezogene Aufgaben müssen den AI Foundation Standard beachten, wenn sie Provider, Prompts, Tools, Evaluation, Routing, Fallback, Caching, Safety, AI Cost Tracking, AI Observability, Audit oder AI Artifacts betreffen.

## 11. Handover Contract

Der Master Prompt muss signifikante Sitzungen mit einem strukturierten Handover abschließen.

Der Handover muss mindestens dokumentieren:

- Session identity und aktive Rolle.
- Erledigte, offene und blockierte Tasks.
- Geänderte repository-relative Pfade.
- Ausgeführte Checks und Evidenz.
- Review-Status und CI-Readiness.
- Risiken, Annahmen und Mitigation.
- Nächste Schritte und empfohlene Rolle.

Handover darf keine Checks, Commits, CI-Ergebnisse, Review-Votes, Freigaben oder erledigte Arbeit erfinden.

## 12. Adapter-Grenze

Roadmap Phase 4 definiert den kanonischen Master Prompt.

Nicht Teil von Roadmap Phase 4:

- Claude-spezifische Adapter-Prompts,
- Codex-spezifische Adapter-Prompts,
- Gemini-, Antigravity- oder IDE-spezifische Profile,
- lokale Tool-Konfiguration,
- MCP- oder Provider-Integration,
- Runtime-Code,
- neue Validator- oder Workflow-Erzwingung ohne gesondertes GO.

Diese Themen gehören in spätere Roadmap-Phasen, tool-spezifische Adapter oder explizit freigegebene Implementierungs-PRs.

## 13. Roadmap-Phase-4-Grenze

Roadmap Phase 4 definiert die Master-Prompt-Semantik. Sie ersetzt weder die ADM-Spezifikation noch Roadmap Phase 2 SaaS Foundation oder Roadmap Phase 3 AI Foundation.

Der Master Prompt muss diese Standards operationalisieren, nicht neu erfinden.

## 14. Final Audit

Vor einer Master-Prompt-Standard-Freigabe wird objektiv geprüft:

- Modellneutralität.
- Repository-backed Truth.
- Vollständige Initialisierung.
- Scope-Deklaration vor Umsetzung.
- ADR- und Review-Regeln.
- Quality-Gate-Evidenz.
- Handover-Pflichten.
- SaaS- und AI-Foundation-Anbindung.
- Adapter-Grenze.
- Dokumentationskonsistenz mit README, ROADMAP, Spezifikation und Operating System.
