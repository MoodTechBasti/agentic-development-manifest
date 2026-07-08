# ADM — Operating System (v0.21 Draft)

Dieses Dokument beschreibt das dateibasierte Kontrollzentrum eines ADM-konformen Projekts. Es speichert Projektzustand, Rollen, Tasks, Entscheidungen, Reviews, Memory, SaaS-Foundation-Standards, AI-Foundation-Standards, Master-Prompt-Standards und Übergaben so, dass verschiedene CLI-Tools und Modelle weiterarbeiten können.

## Zweck

Der Projektzustand muss aus dem Repository lesbar sein. Ein Agent darf ihn nicht aus Chat-Erinnerung rekonstruieren müssen.

## Struktur

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

## Agent Registry

Die Agent Registry unter `.ai/agents/` beschreibt repository-owned Agentenrollen. Sie ist keine lokale Tool-Konfiguration und keine versteckte Modell-Memory.

### Zweck

Die Registry macht explizit:

- welche Rolle ein Agent ausführt,
- welchen Kontext er vor Arbeitsbeginn lesen muss,
- welche Bereiche er im Task-Scope ändern darf,
- welche Bereiche ohne explizite Freigabe tabu sind,
- an welche Rolle sinnvoll übergeben werden soll.

### Minimalfelder

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

### Grenzen

Die Agent Registry ist Governance-Metadokumentation. Sie ersetzt nicht GitHub Rulesets, Branch Protection, CI-Checks, Code Review oder lokale Sandbox- und Tool-Permissions.

Ein Agent muss seine aktive Rolle und seinen Scope vor der Umsetzung nennen, wenn die Registry für den Task relevant ist.

## Project-owned Memory

Project-owned memory ist kuratiertes Projektwissen, das dem Repository gehört. Es darf nicht mit versteckter Modell-Memory, Chatverlauf, Tool-Cache oder lokalen Scratch-Dateien verwechselt werden.

### Autorität

| Rang | Quelle | Bedeutung |
| --- | --- | --- |
| 1 | `spec/`, `docs/`, accepted ADRs | Kanonische Projektwahrheit |
| 2 | `.ai/reviews/`, `.ai/handover/`, `.ai/decisions/` | Versionierte Runtime-Historie |
| 3 | `.ai/memory/`, `.ai/knowledge/`, `.ai/tasks/`, `.ai/agents/` | Kuratierter Kontext, Rollen und Arbeitszustand |
| 4 | `.ai/tmp/`, `.ai/logs/`, `.ai/cache/`, `.ai/scratch/` | Lokale transiente Daten |
| 5 | Chatverlauf oder hidden model memory | Nicht autoritativ |

### Commit-Regeln

Versioniert werden darf nur, was zukünftige Agenten oder Maintainer brauchen, um Entscheidungen, Zustand, Rollen, Risiken oder nächste Schritte zu rekonstruieren.

Nicht versioniert werden dürfen:

- Secrets, Tokens, Credentials oder private URLs.
- Private lokale Pfade und maschinenspezifische Tool-Profile.
- Rohlogs, Chat-Marker, NotebookLM-Quellenmarker oder Prompt-Experimente.
- Ungeprüfte Recherche-Rohdaten.
- Kurzlebige Scratch-Notizen.

### Memory-Dateien

Kuratierte Memory-Dateien unter `.ai/memory/` müssen einen klaren Zweck haben, Unsicherheiten nennen, repository-relative Pfade verwenden, nicht-sensitiv und reviewbar sein.

## Template- und Laufzeit-Trennung

ADM trennt wiederverwendbare Vorlagen von ausgefüllten Laufzeit-Artefakten.

- Wiederverwendbare Review-Vorlagen liegen unter `templates/reviews/`.
- Ausgefüllte, konkrete Review-Berichte liegen unter `.ai/reviews/`.
- Wiederverwendbare Handover-Vorlagen liegen unter `templates/HANDOVER_TEMPLATE.md`.
- Ausgefüllte, konkrete Handovers liegen unter `.ai/handover/`.
- Leere Templates dürfen nicht in `.ai/reviews/` oder `.ai/handover/` abgelegt werden.
- Ausgefüllte Reviews nutzen ihren `review_id` als Dateiname, nicht statische Rollennamen.

Diese Trennung verhindert, dass Projektgedächtnis, Review-Historie, Handover-Historie und wiederverwendbare Schablonen vermischt werden.

## Review-Vorlagen

Die Standard-Reviews des Multi-Agenten-Parlaments sind:

| Template | Rolle | Runtime Prefix |
| --- | --- | --- |
| `templates/reviews/architect.md` | Principal Architect | `REV-ARCH` |
| `templates/reviews/security.md` | Security Engineer | `REV-SEC` |
| `templates/reviews/performance.md` | SRE and Performance Lead | `REV-PERF` |
| `templates/reviews/cost.md` | Cost Engineer | `REV-COST` |
| `templates/reviews/simplifier.md` | Simplifier | `REV-SIMP` |
| `templates/reviews/documentation.md` | Documentation Reviewer | `REV-DOC` |

## Review-Set-Scoping

Ein Review-Set ist eine zusammengehörige Freigabe-Einheit aus sechs Rollen-Reviews.

Jedes ausgefüllte Review-Artefakt muss die folgenden Scope-Felder enthalten:

- `review_set_id`: gemeinsame Set-ID, zum Beispiel `RSV-20260708-review-set-scoping`
- `target_ref`: Zielreferenz, zum Beispiel `PR-2` oder `release/v1`
- `target_commit`: Git-Commit-SHA des geprüften Codes

`target_commit` bezeichnet den geprüften Code-Stand. Es ist nicht zwingend der Workflow-Commit, der die Review-Artefakte enthält.

Ein Release-Gate darf nur grün werden, wenn alle sechs Rollen dieselbe `review_set_id`, dieselbe `target_ref` und denselben stabilen `target_commit` verwenden.

## Review-Validierung

Ausgefüllte Review-Artefakte unter `.ai/reviews/` können lokal geprüft werden.

Advisory-Modus für frühe Entwicklungsarbeit:

```bash
python scripts/validate_reviews.py --path . --mode advisory
```

Strikter Modus für vorhandene Review-Artefakte:

```bash
python scripts/validate_reviews.py --path . --mode existing-strict
```

Vollständiger Review-Set-Modus für Release-Gates:

```bash
python scripts/validate_reviews.py --path . --mode complete-set --review-set-id RSV-20260708-review-set-scoping --target-ref PR-2 --target-commit <git-sha>
```

Der Validator prüft das YAML-Frontmatter, Pflichtfelder, Review-ID-Präfixe, Review-Set-Scope, Review-Status, `runtime_target: .ai/reviews/`, `ci_ready` und optional den Confidence Score.

`complete-set` geht weiter: alle sechs Standard-Review-Typen müssen vorhanden, `PASSED`, `ci_ready: true` und auf denselben Scope gebunden sein.

## Handover Automation

Handover Automation beschreibt, welche Übergabeinformationen später sicher vorbefüllt, gelintet oder validiert werden dürfen.

### Maschinenprüfbare Feldgruppen

| Feldgruppe | Beispiele | Automationsgrenze |
| --- | --- | --- |
| Identität | `session_id`, `timestamp`, `outgoing_agent`, `active_role` | Format und Vorhandensein prüfbar |
| Scope | `changed_files`, `target_ref`, `target_commit`, `review_set_id` | Pfade und Git-/Review-Referenzen prüfbar |
| Qualität | Checks, Review-Status, CI-readiness | Statuswerte prüfbar, Wahrheitsgehalt nur mit Evidenz |
| Routing | nächster Registry-Agent, Routing-Grund | Role-ID prüfbar, Begründung human-review |
| Zustand | erledigte, offene und blockierte Tasks | Struktur prüfbar, Inhalt human-review |

### Zulässige Automatisierung

Spätere Tools dürfen Handovers aus Git-Status, Branch-Informationen, Review-Dateien, aktiven Tasks und Agent Registry vorbefüllen oder prüfen.

Sie dürfen fehlende Pflichtfelder, nicht repository-relative Pfade, inkonsistente Review-Scope-Daten oder fehlende Routing-Rollen melden.

### Verbotene Automatisierung

Handover Automation darf keine Checks, Commits, CI-Ergebnisse, Review-Votes, Rollen, Freigaben oder abgeschlossene Arbeit erfinden. Sie darf keine PRs mergen, Tags setzen, Branch Protection ändern oder Chatverlauf, hidden model memory, Scratch-Dateien, Rohlogs, private Pfade oder Secrets als autoritative Quellen verwenden.

## SaaS Foundation Standard

Der SaaS Foundation Standard ist der Roadmap-Phase-2-Architekturblock für neue SaaS-Systeme. Die kanonische Beschreibung liegt in `docs/SAAS_FOUNDATION_BLUEPRINT.md`; die Architekturentscheidung liegt in `docs/decisions/ADR-20260708-saas-foundation-standard.md`.

Das ist bewusst von Lifecycle Phase 2 — Architecture Competition aus `spec/ADM_v1_DRAFT.md` getrennt.

### Zweck

Die Foundation verhindert, dass Produktfeatures vor den tragenden SaaS-Grenzen entstehen.

Ein SaaS-bezogener Agent muss prüfen, ob sein Task eine der folgenden Grenzen betrifft:

- User, Organization, Tenant, Workspace oder Membership.
- Rollen, Permissions, Support-Zugriff oder Audit.
- Billing Readiness, Entitlements, Quotas, Usage oder Kosten.
- Jobs, Queues, Worker, Retries, Timeouts oder Dead-Letter.
- Observability, Admin-Diagnose, Logs, Metrics oder Request IDs.
- Data Lifecycle für Uploads, Exporte, Logs, Caches, temporäre Dateien oder Backups.
- Lokale DX, Tests oder Performance Budgets.

### Grenzen

Roadmap Phase 2 ist kein Implementierungsauftrag für Microservices, Payment-Provider, AI Provider Architecture, Prompt Registry oder Produktfeatures.

Wenn ein Agent SaaS Foundation Semantik ändert, braucht die Änderung ein ADR und ein vollständiges Review-Set.

## AI Foundation Standard

Der AI Foundation Standard ist der Roadmap-Phase-3-Architekturblock für KI-Funktionen. Die kanonische Beschreibung liegt in `docs/AI_FOUNDATION_STANDARD.md`; die Architekturentscheidung liegt in `docs/decisions/ADR-20260708-ai-foundation-standard.md`.

Das ist bewusst von Lifecycle Phase 3 — Devil's Advocate aus `spec/ADM_v1_DRAFT.md` getrennt.

### Zweck

Die Foundation verhindert, dass produktbezogene KI-Features vor den tragenden KI-Grenzen entstehen.

Ein AI-bezogener Agent muss prüfen, ob sein Task eine der folgenden Grenzen betrifft:

- Provider-Abstraktion, Modellfähigkeiten oder Provider-spezifische Features.
- Prompt Registry, Prompt-Versionen, Prompt-Owner oder Prompt-Änderungsregeln.
- Tool Registry, Tool-Permissions, Side Effects, Human Approval oder Audit.
- Evaluation, Golden Cases, Negative Cases, Qualitätskriterien oder Regressionen.
- AI Cost Tracking, Token, Latenz, Cache Hits, Providerkosten oder Budgetgrenzen.
- Routing, Fallback, Degradation, Timeouts oder lokale Ausführung.
- Caching, Embeddings, KI-Artefakte, Evaluationsdaten oder KI-Data-Lifecycle.
- Safety-Regeln für Datenklassen, Prompt Injection, PII, Secrets, Logs, Cache oder Tool-Nutzung.

### Grenzen

Roadmap Phase 3 ist kein Implementierungsauftrag für Provider-SDKs, Modellaufrufe, Tool-Ausführung, Prompt-Datenbanken, Validatoren, Workflows oder produktspezifische KI-Features.

Wenn ein Agent AI Foundation Semantik ändert, braucht die Änderung ein ADR und ein vollständiges Review-Set.

## Master Prompt Standard

Der Master Prompt Standard ist der Roadmap-Phase-4-Architekturblock für modellneutrales CLI-Agenten-Onboarding. Die kanonische Beschreibung liegt in `docs/MASTER_PROMPT_STANDARD.md`; die Architekturentscheidung liegt in `docs/decisions/ADR-20260708-master-prompt-standard.md`.

Das ist bewusst von Lifecycle Phase 4 — Simplification aus `spec/ADM_v1_DRAFT.md` getrennt.

### Zweck

Der Master Prompt verhindert, dass frische Agenten-Sitzungen Projektzustand aus Chatverlauf, hidden memory oder Tool-Cache ableiten.

Ein Master-Prompt-bezogener Agent muss prüfen, ob sein Task eine der folgenden Grenzen betrifft:

- Autoritätsmodell und repository-backed truth.
- Required Initialization und Pflichtlektüre.
- Rollen-, Scope-, Annahmen- und Risiko-Deklaration vor Umsetzung.
- Operating Rules gegen erfundene Fakten, Checks, Commits, Rollen, Review-Votes, CI-Ergebnisse oder Freigaben.
- Decision Rules, ADR-Auslöser und proportionale Governance.
- Quality Gate Contract, PR-Ready Checks und Complete-Set-Validierung.
- Review Contract und stabile Review-Scope-Bindung.
- Foundation Trigger für SaaS Foundation und AI Foundation.
- Handover Contract und Übergabe-Evidenz.
- Adapter Boundary zwischen kanonischem Master Prompt und tool-spezifischen Prompts.

### Grenzen

Roadmap Phase 4 ist kein Implementierungsauftrag für Runtime-Code, Provider- oder Tool-Integration, CLI-spezifische Adapter-Prompts, lokale Tool-Profile, MCP-Integration, Schemas, Validatoren oder Workflows.

Wenn ein Agent Master Prompt Semantik ändert, braucht die Änderung ein ADR und ein vollständiges Review-Set.

## Sitzungs-Lifecycle

1. Initialisierung: Manifest, Agent Registry, Tasks, Memory, Entscheidungen, Master-Prompt-Dokumente, SaaS-Foundation-Dokumente, AI-Foundation-Dokumente und letzten Handover lesen, wenn relevant.
2. Registrierung: Rolle, Mission und Arbeitsumfang eintragen.
3. Task-Übernahme: Aufgabe als aktiv markieren.
4. Ausführung: lokal arbeiten, testen und dokumentieren.
5. Review: Self-Review und Spezialreviews ausführen.
6. Review-Validierung: ausgefüllte Reviews mit `scripts/validate_reviews.py` prüfen, falls Review-Artefakte erstellt wurden.
7. Übergabe: Tasks, Memory, Metriken und Handover aktualisieren.
8. Commit: Änderungen versionieren.

## Erweitertes Handover-Protokoll

Jeder Handover unter `.ai/handover/` muss mindestens enthalten:

1. Session identity: `session_id`, Timestamp, outgoing agent, aktive Registry-Rolle und Ziel-Empfänger.
2. Task State: abgeschlossene, offene und blockierte Tasks sowie relevante Task-Dateien.
3. Changed Files: neue, geänderte und gelöschte repository-relative Pfade.
4. Checks Run: ausgeführte Befehle, Resultate und Evidenz. Nicht gelaufene Checks müssen `NOT RUN` bleiben.
5. Performance und Budgets: Messwerte, Nicht-Anwendbarkeit oder Decision Record für Verstöße.
6. Review-Status: Review-Dateien, Validator-Modus, `review_set_id`, `target_ref`, stabiler `target_commit`, blockierende Votes und CI-readiness.
7. Agent Routing: aktive Rolle, empfohlene nächste Registry-Rolle und Routing-Grund.
8. Risikoanalyse: neu erkannte Risiken, offene Fragen und blockierende Annahmen.
9. Nächste Schritte: konkrete nächste Aufgabe und empfohlene Rolle.
10. Notes for next agent: knappe, nicht-sensitive Hinweise für die nächste Sitzung.

## Handover-Regel

Kein Agent darf eine größere Arbeit als abgeschlossen markieren, wenn der Handover nicht nachvollziehbar erklärt, was getan wurde, was geprüft wurde und was als Nächstes passieren muss.
