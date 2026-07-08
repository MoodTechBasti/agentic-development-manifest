# ADM — Operating System

> Status: v0.30 synchronized draft
> Last updated: 2026-07-08
> Scope: file-based ADM project operating model, not runtime implementation

Dieses Dokument beschreibt das dateibasierte Kontrollzentrum eines ADM-konformen Projekts. Es speichert Projektzustand, Rollen, Tasks, Entscheidungen, Reviews, Review-Archive, Memory, Standards, Tool Verification und Übergaben so, dass verschiedene CLI-Tools und Modelle weiterarbeiten können.

Der Projektzustand muss aus dem Repository lesbar sein. Ein Agent darf ihn nicht aus Chat-Erinnerung, hidden model memory, Tool-Cache oder lokalen Scratch-Dateien rekonstruieren müssen.

## 1. Struktur

```text
.ai/
├── manifest/
├── knowledge/
├── agents/
├── research/
├── planning/
├── reviews/
├── decisions/
├── memory/
├── tasks/
├── protocols/
├── audit/
├── quality/
├── handover/
├── roadmap/
├── experiments/
├── benchmarks/
├── standards/
└── playbooks/
```

Tool-specific adapter prompts are stored under `prompts/adapters/`, not inside `.ai/`, because they are reusable prompt artifacts rather than runtime state.

## 2. Authority Order

| Rang | Quelle | Bedeutung |
| --- | --- | --- |
| 1 | `spec/`, `docs/`, `ROADMAP.md`, accepted ADRs | Kanonische Projektwahrheit |
| 2 | `prompts/master_prompt.md`, `prompts/adapters/` | Kanonische und abgeleitete Agenten-Startanweisungen |
| 3 | `.ai/reviews/`, `.ai/reviews/archive/`, `.ai/handover/`, `.ai/decisions/` | Versionierte Runtime-Historie |
| 4 | `.ai/memory/`, `.ai/knowledge/`, `.ai/tasks/`, `.ai/agents/` | Kuratierter Kontext, Rollen und Arbeitszustand |
| 5 | `.ai/tmp/`, `.ai/logs/`, `.ai/cache/`, `.ai/scratch/` | Lokale transiente Daten |
| 6 | Chatverlauf, hidden model memory, Tool-State | Nicht autoritativ |

## 3. Agent Registry

Die Agent Registry unter `.ai/agents/` beschreibt repository-owned Agentenrollen. Sie ist keine lokale Tool-Konfiguration und keine versteckte Modell-Memory.

Die Registry macht explizit:

- welche Rolle ein Agent ausführt,
- welchen Kontext er vor Arbeitsbeginn lesen muss,
- welche Bereiche er im Task-Scope ändern darf,
- welche Bereiche ohne explizite Freigabe tabu sind,
- an welche Rolle sinnvoll übergeben werden soll.

Minimalfelder:

| Feld | Bedeutung |
| --- | --- |
| `agent_id` | stabiler repository-lokaler Rollen-Identifier |
| `role` | menschlich lesbarer Rollenname |
| `mission` | Hauptverantwortung |
| `reads` | Pflichtkontext vor Arbeitsbeginn |
| `writes` | erwartete Schreibbereiche im Scope |
| `forbidden` | Bereiche ohne explizite Freigabe tabu |
| `handover_to` | empfohlene nächste Rolle oder Rollenfamilie |
| `review_scope` | Review-Verantwortung, falls vorhanden |

Die Agent Registry ersetzt nicht GitHub Rulesets, Branch Protection, CI-Checks, Code Review oder lokale Sandbox- und Tool-Permissions.

## 4. Project-owned Memory

Project-owned memory ist kuratiertes Projektwissen, das dem Repository gehört. Es darf nicht mit versteckter Modell-Memory, Chatverlauf, Tool-Cache oder lokalen Scratch-Dateien verwechselt werden.

Versioniert werden darf nur, was zukünftige Agenten oder Maintainer brauchen, um Entscheidungen, Zustand, Rollen, Risiken oder nächste Schritte zu rekonstruieren.

Nicht versioniert werden dürfen:

- Secrets, Tokens, Credentials oder private URLs,
- private lokale Pfade und maschinenspezifische Tool-Profile,
- Rohlogs, Chat-Marker, NotebookLM-Quellenmarker oder Prompt-Experimente,
- ungeprüfte Recherche-Rohdaten,
- kurzlebige Scratch-Notizen.

Kuratierte Memory-Dateien unter `.ai/memory/` müssen einen klaren Zweck haben, Unsicherheiten nennen, repository-relative Pfade verwenden, nicht-sensitiv und reviewbar sein.

## 5. Template- und Laufzeit-Trennung

ADM trennt wiederverwendbare Vorlagen von ausgefüllten Laufzeit-Artefakten.

- Wiederverwendbare Review-Vorlagen liegen unter `templates/reviews/`.
- Ausgefüllte, konkrete Review-Berichte liegen unter `.ai/reviews/`.
- Archivierte historische Review-Sets dürfen später unter `.ai/reviews/archive/<review_set_id>/` liegen.
- Wiederverwendbare Handover-Vorlagen liegen unter `templates/HANDOVER_TEMPLATE.md`.
- Ausgefüllte, konkrete Handovers liegen unter `.ai/handover/`.
- Die Handover-Discovery- und Continuity-Policy liegt unter `.ai/handover/README.md`.
- Wiederverwendbare Adapter-Prompts liegen unter `prompts/adapters/`.
- Leere Templates dürfen nicht in `.ai/reviews/` oder `.ai/handover/` abgelegt werden.
- Ausgefüllte Reviews nutzen ihren `review_id` als Dateiname, nicht statische Rollennamen.

Diese Trennung verhindert, dass Projektgedächtnis, Review-Historie, Handover-Historie, Adapter-Prompts und wiederverwendbare Schablonen vermischt werden.

## 6. Review-Vorlagen und Review-Set-Scoping

Die Standard-Reviews des Multi-Agenten-Parlaments sind:

| Template | Rolle | Runtime Prefix |
| --- | --- | --- |
| `templates/reviews/architect.md` | Principal Architect | `REV-ARCH` |
| `templates/reviews/security.md` | Security Engineer | `REV-SEC` |
| `templates/reviews/performance.md` | SRE and Performance Lead | `REV-PERF` |
| `templates/reviews/cost.md` | Cost Engineer | `REV-COST` |
| `templates/reviews/simplifier.md` | Simplifier | `REV-SIMP` |
| `templates/reviews/documentation.md` | Documentation Reviewer | `REV-DOC` |

Ein Review-Set ist eine zusammengehörige Freigabe-Einheit aus sechs Rollen-Reviews.

Jedes ausgefüllte Review-Artefakt muss die folgenden Scope-Felder enthalten:

- `review_set_id`: gemeinsame Set-ID, zum Beispiel `RSV-20260708-session-continuity-baseline`,
- `target_ref`: Zielreferenz, zum Beispiel `adm-v028-session-continuity-baseline`,
- `target_commit`: Git-Commit-SHA des geprüften Codes oder der geprüften Dokumentation.

`target_commit` bezeichnet den geprüften Stand. Es ist nicht zwingend der Workflow-Commit, der die Review-Artefakte enthält.

Ein Release-Gate darf nur grün werden, wenn alle sechs Rollen dieselbe `review_set_id`, dieselbe `target_ref` und denselben stabilen `target_commit` verwenden.

Archivierte Review-Sets bleiben historische Evidenz und dürfen nicht benutzt werden, um aktuelle Validatorfehler zu verstecken.

## 7. Review-Validierung

Ausgefüllte Review-Artefakte unter `.ai/reviews/` können lokal geprüft werden.

```bash
python3 scripts/validate_reviews.py --path . --mode advisory
python3 scripts/validate_reviews.py --path . --mode existing-strict
python3 scripts/validate_reviews.py --path . --mode complete-set --review-set-id <set-id> --target-ref <ref> --target-commit <git-sha>
```

Der Validator prüft das YAML-Frontmatter, Pflichtfelder, Review-ID-Präfixe, Review-Set-Scope, Review-Status, `runtime_target: .ai/reviews/`, `ci_ready` und optional den Confidence Score.

`complete-set` geht weiter: alle sechs Standard-Review-Typen müssen vorhanden, `PASSED`, `ci_ready: true` und auf denselben Scope gebunden sein.

Der Standardpfad validiert direkte `.ai/reviews/*.md` Dateien und ignoriert `.ai/reviews/archive/**` nicht-rekursiv.

v0.27 migriert abgeschlossene historische Review-Sets bis v0.25 in `.ai/reviews/archive/<review_set_id>/`. v0.30 migriert abgeschlossene Review-Sets von v0.26 bis v0.28 in das Archiv, während v0.29 als aktive Release-Evidenz direkt unter `.ai/reviews/` bleibt. Diese Migrationen ändern keine Review-Metadaten und ändern keine Produktionsvalidatorlogik.

## 8. Release Hygiene

Release-Hygiene ist Teil des Operating Systems, aber keine Release-Automation.

Vor einem Release müssen Agenten und Maintainer unterscheiden:

- stabiler geprüfter Commit: der nicht-review Commit, auf den Reviews zeigen,
- Review-Artefakt-Commit: der spätere Commit mit `.ai/reviews/`,
- finaler Tag-Commit: der `main`-Commit nach Merge der Reviews und erfolgreicher manueller `complete-set`-Validierung.

GitHub-Rulesets sind externe Repository-Einstellungen. Sie müssen manuell auditiert werden, wenn Governance-, Review-, Release- oder Branch-Protection-Reife behauptet wird. Source-Dateien allein beweisen diesen Audit nicht.

## 9. Handover Automation

Handover Automation beschreibt, welche Übergabeinformationen später sicher vorbefüllt, gelintet oder validiert werden dürfen.

Maschinenprüfbare Feldgruppen:

| Feldgruppe | Beispiele | Automationsgrenze |
| --- | --- | --- |
| Identität | `session_id`, `timestamp`, `outgoing_agent`, `active_role` | Format und Vorhandensein prüfbar |
| Scope | `changed_files`, `target_ref`, `target_commit`, `review_set_id` | Pfade und Git-/Review-Referenzen prüfbar |
| Qualität | Checks, Review-Status, CI-readiness | Statuswerte prüfbar, Wahrheitsgehalt nur mit Evidenz |
| Routing | nächster Registry-Agent, Routing-Grund | Role-ID prüfbar, Begründung human-review |
| Zustand | erledigte, offene und blockierte Tasks | Struktur prüfbar, Inhalt human-review |

Spätere Tools dürfen Handovers aus Git-Status, Branch-Informationen, Review-Dateien, aktiven Tasks und Agent Registry vorbefüllen oder prüfen.

Handover Automation darf keine Checks, Commits, CI-Ergebnisse, Review-Votes, Rollen, Freigaben oder abgeschlossene Arbeit erfinden. Sie darf keine PRs mergen, Tags setzen, Branch Protection ändern oder Chatverlauf, hidden model memory, Scratch-Dateien, Rohlogs, private Pfade oder Secrets als autoritative Quellen verwenden.

v0.28 implementiert keinen Handover-Linter, keine Runtime und keine Handover-Automation-Erweiterung.

## 10. Session Continuity

Session Continuity beschreibt, wie zukünftige Agenten eine Sitzung aus repository-owned evidence fortsetzen.

Ein Agent muss vor Umsetzung prüfen:

1. den aktuellen Git-Zustand,
2. die kanonischen ADM-Dokumente und akzeptierten ADRs,
3. relevante Reviews und Review-Archive,
4. `.ai/handover/` und `.ai/handover/README.md`, wenn vorherige Sitzungsevidenz relevant ist,
5. `.ai/tasks/`, `.ai/memory/`, `.ai/knowledge/`, `.ai/decisions/` und `.ai/agents/`, wenn sie für den Scope relevant sind.

Latest-Handover-Discovery:

1. Explizite `Timestamp:` Felder im Handover haben Vorrang.
2. Dateiname `Handoff-YYYYMMDD-HHMM-<scope>.md` ist Fallback.
3. Bei widersprüchlichen, fehlenden oder mehreren plausiblen neuesten Handovers muss der Agent `AMBIGUOUS` melden.
4. Wenn kein relevanter Handover existiert, ist der Continuity-Zustand `UNKNOWN`.
5. Chatverlauf, hidden model memory, Tool-State, lokale Profile, Scratch-Dateien und Rohlogs dürfen keine fehlende Repository-Evidenz ersetzen.

Continuity status values:

| Status | Bedeutung |
| --- | --- |
| `READY` | Genug Repository-Evidenz für den nächsten Arbeitsschritt vorhanden; keine Freigabe. |
| `PARTIAL` | Fortsetzung möglich, aber fehlende Checks, Scope-Fragen oder Risiken müssen zuerst geprüft werden. |
| `BLOCKED` | Ein benannter Blocker verhindert Fortsetzung. |
| `UNKNOWN` | Der Fortsetzungszustand ist aus Repository-Evidenz nicht belastbar. |

`READY` ist keine CI-, Review-, Merge-, Release- oder Tag-Freigabe.

## 11. Foundation Standards

### SaaS Foundation Standard

Der SaaS Foundation Standard ist der Roadmap-Phase-2-Architekturblock für neue SaaS-Systeme. Die kanonische Beschreibung liegt in `docs/SAAS_FOUNDATION_BLUEPRINT.md`; die Architekturentscheidung liegt in `docs/decisions/ADR-20260708-saas-foundation-standard.md`.

Das ist bewusst von Lifecycle Phase 2 — Architecture Competition aus `spec/ADM_v1_DRAFT.md` getrennt.

Ein SaaS-bezogener Agent muss prüfen, ob sein Task User, Organization, Tenant, Workspace, Membership, Rollen, Permissions, Billing Readiness, Entitlements, Quotas, Jobs, Workers, Observability, Admin-Diagnose, Data Lifecycle, lokale DX, Tests oder Performance Budgets betrifft.

Roadmap Phase 2 ist kein Implementierungsauftrag für Microservices, Payment-Provider, AI Provider Architecture, Prompt Registry oder Produktfeatures.

### AI Foundation Standard

Der AI Foundation Standard ist der Roadmap-Phase-3-Architekturblock für KI-Funktionen. Die kanonische Beschreibung liegt in `docs/AI_FOUNDATION_STANDARD.md`; die Architekturentscheidung liegt in `docs/decisions/ADR-20260708-ai-foundation-standard.md`.

Das ist bewusst von Lifecycle Phase 3 — Devil's Advocate aus `spec/ADM_v1_DRAFT.md` getrennt.

Ein AI-bezogener Agent muss prüfen, ob sein Task Provider-Abstraktion, Modellfähigkeiten, Prompt Registry, Tool Registry, Evaluation, AI Cost Tracking, Routing, Fallback, Caching, Safety-Regeln, Observability, Audit oder AI Artifact Lifecycle betrifft.

Roadmap Phase 3 ist kein Implementierungsauftrag für Provider-SDKs, Modellaufrufe, Tool-Ausführung, Prompt-Datenbanken, Validatoren, Workflows oder produktspezifische KI-Features.

## 12. Prompt Standards

### Master Prompt Standard

Der Master Prompt Standard ist der Roadmap-Phase-4-Architekturblock für modellneutrales CLI-Agenten-Onboarding. Die kanonische Beschreibung liegt in `docs/MASTER_PROMPT_STANDARD.md`; die Architekturentscheidung liegt in `docs/decisions/ADR-20260708-master-prompt-standard.md`.

Ein Master-Prompt-bezogener Agent muss Autoritätsmodell, Required Initialization, Scope Declaration, Operating Rules, Decision Rules, Quality Gate Contract, Review Contract, Foundation Trigger, Handover Contract, Session Continuity Contract und Adapter Boundary beachten.

Roadmap Phase 4 ist kein Implementierungsauftrag für Runtime-Code, Provider- oder Tool-Integration, CLI-spezifische Adapter-Prompts, lokale Tool-Profile, MCP-Integration, Schemas, Validatoren oder Workflows.

### Adapter Prompt Standard

Der Adapter Prompt Standard ist der Roadmap-Phase-5-Architekturblock für tool-spezifische CLI-Agenten-Prompts. Die kanonische Beschreibung liegt in `docs/ADAPTER_PROMPT_STANDARD.md`; die Architekturentscheidung liegt in `docs/decisions/ADR-20260708-adapter-prompt-standard.md`.

Adapter Prompts verhindern, dass tool-spezifische Bedienhinweise in den kanonischen Master Prompt zurücklecken oder ADM-Governance umgehen.

Roadmap Phase 5 ist kein Implementierungsauftrag für Runtime-Code, Provider-SDKs, echte Tool-Integration, lokale Tool-Profile, MCP-Integration, Schemas, Validatoren, Workflows, Release-Automation oder Provider-Secrets.

## 13. Tool Verification

Tool Verification ist der Roadmap-Phase-8-Discovery- und Governance-Block für deferred oder future CLI-Tool-Adapter. Die kanonische Beschreibung liegt in `docs/TOOL_VERIFICATION.md`; die Architekturentscheidung liegt in `docs/decisions/ADR-20260708-tool-verification-discovery-baseline.md`.

Ein Tool-Verification-bezogener Agent muss prüfen, ob sein Task deferred Adapter, future Adapter, Gemini CLI, Antigravity CLI, Tool-Verhalten, CLI-Fähigkeiten, Tool-State-Grenzen, lokale Profile, Cache, hidden memory, Review-Verhalten oder Adapter-Eignung betrifft.

Tool Verification ist kein Implementierungsauftrag für Gemini CLI Adapter, Antigravity CLI Adapter, neue Adapter, Runtime-Code, Provider-SDKs, MCP-Integration, lokale Tool-Profile, Validatoren, Workflows oder Release-Automation.

Gemini CLI und Antigravity CLI bleiben deferred candidates, bis aktuelles Tool-Verhalten dokumentiert, reviewed und explizit in einem späteren Adapter-PR freigegeben wurde.

## 14. Sitzungs-Lifecycle

1. Initialisierung: Manifest, Agent Registry, Tasks, Memory, Entscheidungen, Master-Prompt-Dokumente, Adapter-Prompt-Dokumente, SaaS-Foundation-Dokumente, AI-Foundation-Dokumente und letzten Handover lesen, wenn relevant.
2. Tool-Verification-Prüfung: `docs/TOOL_VERIFICATION.md` lesen, wenn deferred oder future Adapter, Tool-Verhalten, CLI-Fähigkeiten oder Tool-State-Grenzen betroffen sind.
3. Continuity-Prüfung: neuesten relevanten Handover, Repository-Evidenz, offene Risiken und Ambiguitäten prüfen.
4. Registrierung: Rolle, Mission und Arbeitsumfang eintragen.
5. Task-Übernahme: Aufgabe als aktiv markieren.
6. Ausführung: lokal arbeiten, testen und dokumentieren.
7. Review: Self-Review und Spezialreviews ausführen.
7. Review-Validierung: ausgefüllte Reviews mit `scripts/validate_reviews.py` prüfen, falls Review-Artefakte erstellt wurden.
8. Übergabe: Tasks, Memory, Metriken und Handover aktualisieren.
9. Commit: Änderungen versionieren.

## 14. Erweitertes Handover-Protokoll

Jeder Handover unter `.ai/handover/` muss mindestens enthalten:

1. Session identity: `session_id`, Timestamp, outgoing agent, aktive Registry-Rolle und Ziel-Empfänger.
2. Continuity state: `READY`, `PARTIAL`, `BLOCKED` oder `UNKNOWN`, plus latest repo evidence checked.
3. Task State: abgeschlossene, offene und blockierte Tasks sowie relevante Task-Dateien.
4. Changed Files: neue, geänderte und gelöschte repository-relative Pfade.
5. Checks Run: ausgeführte Befehle, Resultate und Evidenz. Nicht gelaufene Checks müssen `NOT RUN` bleiben.
6. Performance und Budgets: Messwerte, Nicht-Anwendbarkeit oder Decision Record für Verstöße.
7. Review-Status: Review-Dateien, Validator-Modus, `review_set_id`, `target_ref`, stabiler `target_commit`, blockierende Votes und CI-readiness.
8. Agent Routing: aktive Rolle, empfohlene nächste Registry-Rolle und Routing-Grund.
9. Risikoanalyse: neu erkannte Risiken, offene Fragen und blockierende Annahmen.
10. Nächste Schritte: konkrete nächste Aufgabe und empfohlene Rolle.
11. Notes for next agent: knappe, nicht-sensitive Hinweise für die nächste Sitzung.

Kein Agent darf eine größere Arbeit als abgeschlossen markieren, wenn der Handover nicht nachvollziehbar erklärt, was getan wurde, was geprüft wurde und was als Nächstes passieren muss.
