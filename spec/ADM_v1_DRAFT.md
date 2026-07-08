# ADM — Spezifikation (v0.11 Draft)

Dieses Dokument spezifiziert den aktuellen Draft-Zustand des Agentic Development Manifest.

## Status

- Version: v0.11 Draft
- Zustand: Review Set Scoping and Target Binding
- Ziel: modellneutraler Standard für CLI-basierte Softwareentwicklung mit verbindlichen Qualitätsleitplanken, automatisierter Durchsetzung, Agenten-Onboarding, lokaler Workspace-Initialisierung, standardisierten Review-Protokollen und commit-gebundener Review-Validierung

## Entwicklungs-Lifecycle

ADM arbeitet sequenziell. Jede Phase endet mit Review und Quality Gate.

1. Phase 0 — Mission & Standards
2. Phase 1 — Research Engine
3. Phase 2 — Architecture Competition
4. Phase 3 — Devil's Advocate
5. Phase 4 — Simplification
6. Phase 5 — Roadmap & Plan
7. Phase 6 — Foundation Build

## Phase 0 — Mission & Standards

Ziele, Nicht-Ziele, Zielgruppen, Risiken, Einschränkungen und Qualitätsstandards werden definiert.

## Phase 1 — Research Engine

Aktuelle Informationen werden recherchiert, wenn sie für Architektur, Sicherheit, Frameworks, Standards oder Kosten relevant sind.

## Phase 2 — Architecture Competition

Mehrere Architekturvarianten werden verglichen, bevor eine Richtung gewählt wird.

Beispiele:

- Modular Monolith
- DDD Lite
- Hexagonal Architecture
- Vertical Slice
- Event-Driven Architecture

## Phase 3 — Devil's Advocate

Die gewählte Richtung wird aggressiv auf Schwächen, Kosten, Risiken und spätere technische Schulden geprüft.

## Phase 4 — Simplification

Unnötige Module, Abstraktionen und Abhängigkeiten werden entfernt, bevor gebaut wird.

## Phase 5 — Roadmap & Plan

Die Umsetzung wird in Abhängigkeiten, Meilensteine und überprüfbare Arbeitspakete zerlegt.

## Phase 6 — Foundation Build

Zuerst entsteht die SaaS-Foundation. Produktfeatures folgen erst danach.

## Definition of Done für Code-Änderungen

Keine größere Code-Änderung gilt als abgeschlossen, bevor folgende Punkte erfüllt oder begründet abgewichen sind:

- neue oder geänderte Quellcodedateien bleiben unter 300 Zeilen
- Ausnahmen sind in einem Decision Record begründet
- exportierte Schnittstellen sind typisiert und dokumentiert
- neue Codepfade sind durch passende Tests abgedeckt
- Foundation-Code strebt mindestens 80 Prozent Testabdeckung an
- vertrauliche Zugangsdaten werden nicht im Repository abgelegt
- neue Abhängigkeiten sind begründet
- Duplikate und unnötige Abstraktionen wurden geprüft

## Quality Gates bei Phasenübergängen

Ein Phasenübergang ist nur freigegeben, wenn passende Review-Artefakte vorliegen:

1. Architect Review
2. Security Review
3. Performance Review
4. Cost Review
5. Simplification Review
6. Documentation Review

Kritische Einwände blockieren den Übergang, bis sie gelöst oder bewusst akzeptiert und dokumentiert wurden.

## Review Template Governance

Wiederverwendbare Review-Vorlagen liegen unter `templates/reviews/`.

Ausgefüllte Review-Artefakte liegen unter `.ai/reviews/` und müssen aus einer passenden Vorlage abgeleitet werden.

Standardrollen:

- `templates/reviews/architect.md`
- `templates/reviews/security.md`
- `templates/reviews/performance.md`
- `templates/reviews/cost.md`
- `templates/reviews/simplifier.md`
- `templates/reviews/documentation.md`

Jedes ausgefüllte Review muss einen Status, betroffene Dateien, Befunde, erforderliche Aktionen, finales Vote, CI-readiness und Review-Set-Scope enthalten.

## Review Set Scoping

Ein Review-Set ist die logische Einheit aus sechs zusammengehörigen Rollen-Reviews für denselben Zielstand.

Jedes ausgefüllte Review-Artefakt muss diese Scope-Felder enthalten:

- `review_set_id`: gemeinsame Set-ID im Format `RSV-YYYYMMDD-feature-slug`
- `target_ref`: Zielreferenz wie `PR-2`, Branch-Name oder Release-Ref
- `target_commit`: Git-Commit-SHA des geprüften Codes

Ausgefüllte Review-Dateien sollen nicht unter statischen Rollennamen wie `.ai/reviews/architect.md` gespeichert werden. Stattdessen soll der `review_id` als Dateiname genutzt werden, zum Beispiel `.ai/reviews/REV-ARCH-20260708-review-set-scoping.md`.

## Review Validation

`scripts/validate_reviews.py` prüft ausgefüllte Review-Artefakte unter `.ai/reviews/`.

Der Validator ist ohne externe Python-Pakete implementiert und prüft:

- YAML-Frontmatter am Dateianfang
- Pflichtfelder wie `template_id`, `review_type`, `review_id`, `review_set_id`, `target_ref`, `target_commit`, `review_status`, `runtime_target` und `ci_ready`
- gültige Review-Typen und Review-ID-Präfixe
- gültige Review-Set-ID-Struktur
- gültige Statuswerte
- Konsistenz zwischen `review_status: PASSED` und `ci_ready: true`
- optionalen Confidence Score zwischen 1 und 10

ADM definiert drei Review-Validierungsmodi:

| Modus | Bedeutung | Blocking |
| --- | --- | --- |
| `advisory` | Vorhandene Review-Artefakte prüfen, Fehler melden, Entwicklung nicht blockieren | Nein |
| `existing-strict` | Vorhandene Review-Artefakte strikt prüfen, aber kein vollständiges Set verlangen | Ja, bei fehlerhaften vorhandenen Reviews |
| `complete-set` | Alle sechs Standardreviews müssen vorhanden, `PASSED`, `ci_ready: true` und identisch gescoped sein | Ja |

Lokale advisory Ausführung:

```bash
python scripts/validate_reviews.py --path . --mode advisory
```

Lokale strenge Ausführung für vorhandene Reviews:

```bash
python scripts/validate_reviews.py --path . --mode existing-strict
```

Vollständiges Release-Gate mit Scope-Bindung:

```bash
python scripts/validate_reviews.py --path . --mode complete-set --review-set-id RSV-20260708-review-set-scoping --target-ref PR-2 --target-commit <git-sha>
```

Der ältere Befehl `--advisory` bleibt als Alias für `--mode advisory` gültig. `--strict`, `--set-id` und `--dir` bleiben als Kompatibilitätsformen für ältere Review-Skripte verfügbar.

Das harte vollständige Review-Gate ist an `complete-set` gebunden und darf nur für Release-Kontexte, manuelle Release-Readiness-Prüfungen oder explizit definierte Phasenübergänge verwendet werden.

## Automatisiertes CI Quality Gate

ADM-konforme Repositories sollen Qualitätsregeln nicht nur dokumentieren, sondern automatisiert prüfen.

Das erste verpflichtende Gate ist der Line-Limit-Check:

- Workflow: `.github/workflows/adm-quality-gate.yml`
- Skript: `scripts/check_limits.py`
- Standardlimit: 300 Zeilen pro Quellcodedatei
- Ausführung: `push`, `pull_request` und manuell über `workflow_dispatch`

Der Review-Validator läuft im gleichen Workflow mit kontextabhängigem Modus:

| Kontext | Modus |
| --- | --- |
| Feature-Branch / `dev` | `advisory` |
| PR nach `main` / `master` | `existing-strict` |
| Push auf `main` / `master` | `existing-strict` |
| `release/**` | `complete-set` mit `target_ref` und `target_commit` |
| Manuell per `workflow_dispatch` | auswählbar, Standard `existing-strict` |

Für Pull Requests nutzt CI `target_ref: PR-<number>` und die PR-Head-SHA. Für Pushes nutzt CI den Branch-Namen und die Workflow-SHA.

## ADM Exemptions

Line-Limit-Ausnahmen werden vom Checker technisch ausgewertet, wenn sie in einem Decision Record stehen.

Eine Ausnahme ist im strikten CI-Modus nur gültig, wenn:

- der Decision Record den Status ACCEPTED oder APPROVED hat
- die Ausnahme dieses Format nutzt: `ADM-Exemption: path/to/file.py (Max: 500)`
- der Pfad repository-relativ ist

Für lokale Feature-Arbeit kann `scripts/check_limits.py --allow-proposed-exemptions` genutzt werden. Dieser Modus akzeptiert zusätzlich PROPOSED, ist aber nicht der Merge-Readiness-Standard.

## Workspace Bootstrap

`scripts/bootstrap.sh` initialisiert die lokale `.ai/`-Struktur und installiert einen lokalen Pre-Commit-Hook. Der lokale Hook nutzt den vorgeschlagenen Exemption-Modus, damit frühe Feature-Arbeit nicht unnötig blockiert wird. Das CI-Gate bleibt streng.

## Agent Onboarding

Frische CLI-Agenten starten mit `prompts/master_prompt.md`. Der Master Prompt definiert Lese-Reihenfolge, Initialisierung, Qualitätsregeln, Decision-Record-Pflicht und Handover-Pflicht.

## Agent Communication Protocol

Wichtige Entscheidungen werden strukturiert dokumentiert.

Format:

```markdown
### Decision: [Titel]

- Reason:
- Evidence:
- Confidence:
- Alternatives:
- Tradeoffs:
- Risks:
- Files:
- Dependencies:
- Owner:
- Status:
```

## Quality Gate

Eine Phase darf erst abgeschlossen werden, wenn Entscheidungen, Risiken, offene Fragen, Tests, Metriken, Review-Status und nächste Schritte dokumentiert sind.
