# ADM — Operating System (v0.17 Draft)

Dieses Dokument beschreibt das dateibasierte Kontrollzentrum eines ADM-konformen Projekts. Es speichert Projektzustand, Rollen, Tasks, Entscheidungen, Reviews, Memory und Übergaben so, dass verschiedene CLI-Tools und Modelle weiterarbeiten können.

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

Die Agent Registry ist Governance-Metadokumentation. Sie ersetzt nicht:

- GitHub Rulesets,
- Branch Protection,
- CI-Checks,
- Code Review,
- lokale Sandbox- oder Tool-Permissions.

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

Kuratierte Memory-Dateien unter `.ai/memory/` müssen:

- einen klaren Zweck haben,
- eine kurze Gültigkeits- oder Kontextbeschreibung enthalten,
- bekannte Unsicherheiten nennen,
- repository-relative Pfade verwenden,
- nicht-sensitiv und reviewbar sein.

## Template- und Laufzeit-Trennung

ADM trennt wiederverwendbare Vorlagen von ausgefüllten Laufzeit-Artefakten.

- Wiederverwendbare Review-Vorlagen liegen unter `templates/reviews/`.
- Ausgefüllte, konkrete Review-Berichte liegen unter `.ai/reviews/`.
- Leere Templates dürfen nicht in `.ai/reviews/` abgelegt werden.
- Ausgefüllte Reviews nutzen ihren `review_id` als Dateiname, nicht statische Rollennamen.

Diese Trennung verhindert, dass Projektgedächtnis, Review-Historie und wiederverwendbare Schablonen vermischt werden.

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

`target_commit` bezeichnet den geprüften Code-Stand. Es ist nicht zwingend der Workflow-Commit, der die Review-Artefakte enthält. Review-Artefakte sollen deshalb nach dem Code-Commit geschrieben werden und weiterhin auf den stabilen geprüften Code-Commit zeigen.

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

Im GitHub-Workflow wird die Review-Validierung kontextabhängig ausgeführt:

| Kontext | Modus |
| --- | --- |
| Feature-Branch / `dev` | `advisory` |
| PR nach `main` / `master` | `existing-strict` |
| Push auf `main` / `master` | `existing-strict` |
| `release/**` | `complete-set` mit `target_ref` und stabilem geprüftem `target_commit` |
| Manuell per `workflow_dispatch` | auswählbar, Standard `existing-strict` |

Die Workflow-Automation ermittelt den stabilen geprüften Commit standardmäßig als letzten Commit außerhalb `.ai/reviews/`. Manuelle Runs können diesen Wert mit `reviewed_commit` explizit setzen.

Diese Trennung verhindert, dass normale Entwicklungsarbeit durch fehlende Review-Instanzen hart blockiert wird, während Release-Zweige ein echtes vollständiges und commit-gebundenes Review-Gate erhalten.

## Sitzungs-Lifecycle

1. Initialisierung: Manifest, Agent Registry, Tasks, Memory, Entscheidungen und letzten Handover lesen.
2. Registrierung: Rolle, Mission und Arbeitsumfang eintragen.
3. Task-Übernahme: Aufgabe als aktiv markieren.
4. Ausführung: lokal arbeiten, testen und dokumentieren.
5. Review: Self-Review und Spezialreviews ausführen.
6. Review-Validierung: ausgefüllte Reviews mit `scripts/validate_reviews.py` prüfen, falls Review-Artefakte erstellt wurden.
7. Übergabe: Tasks, Memory, Metriken und Handover aktualisieren.
8. Commit: Änderungen versionieren.

## Erweitertes Handover-Protokoll

Jeder Handover unter `.ai/handover/` muss mindestens enthalten:

### 1. Task State

- abgeschlossene Tasks
- offene oder blockierte Tasks
- betroffene Dateien

### 2. Technische Metriken

- Linter-Status
- Compiler- oder Typecheck-Status
- Teststatus
- Coverage, falls verfügbar
- Dateien über 300 Zeilen
- Decision Records für begründete Ausnahmen

### 3. Performance und Budgets

- gemessene Latenzen, falls relevant
- Budget-Verstöße
- Begründung oder Decision Record für akzeptierte Abweichungen

### 4. Review-Status

- ausgeführte Review-Vorlagen
- Review-Dateien unter `.ai/reviews/`
- Ergebnis von `scripts/validate_reviews.py`, inklusive Modus und Scope
- `review_set_id`, `target_ref` und stabiler geprüfter `target_commit`
- blockierende Votes
- CI-readiness status

### 5. Agent Routing

- aktive Agentenrolle, falls relevant
- nächster empfohlener Registry-Agent oder Rollenfamilie
- Grund für das empfohlene Handover-Routing

### 6. Risikoanalyse

- neu erkannte Architektur-, Sicherheits-, Kosten- oder Betriebsrisiken
- offene Fragen
- blockierende Annahmen

### 7. Nächste Schritte

- nächste logische Aufgabe
- empfohlene Rolle für die nächste Sitzung
- Hinweise für den nächsten Agenten

## Handover-Regel

Kein Agent darf eine größere Arbeit als abgeschlossen markieren, wenn der Handover nicht nachvollziehbar erklärt, was getan wurde, was geprüft wurde und was als Nächstes passieren muss.