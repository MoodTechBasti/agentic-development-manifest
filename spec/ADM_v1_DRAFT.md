# ADM — Spezifikation (v0.9 Draft)

Dieses Dokument spezifiziert den aktuellen Draft-Zustand des Agentic Development Manifest.

## Status

- Version: v0.9 Draft
- Zustand: Advisory Review Validation
- Ziel: modellneutraler Standard für CLI-basierte Softwareentwicklung mit verbindlichen Qualitätsleitplanken, automatisierter Durchsetzung, Agenten-Onboarding, lokaler Workspace-Initialisierung, standardisierten Review-Protokollen und advisory Review-Validierung

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

Jedes ausgefüllte Review muss einen Status, betroffene Dateien, Befunde, erforderliche Aktionen, finales Vote und CI-readiness enthalten.

## Review Validation

`scripts/validate_reviews.py` prüft ausgefüllte Review-Artefakte unter `.ai/reviews/`.

Der Validator ist ohne externe Python-Pakete implementiert und prüft:

- YAML-Frontmatter am Dateianfang
- Pflichtfelder wie `template_id`, `review_type`, `review_id`, `review_status`, `runtime_target` und `ci_ready`
- gültige Review-Typen und Review-ID-Präfixe
- gültige Statuswerte
- Konsistenz zwischen `review_status: PASSED` und `ci_ready: true`
- optionalen Confidence Score zwischen 1 und 10

Lokale strenge Ausführung:

```bash
python scripts/validate_reviews.py --path .
```

CI-Ausführung im Advisory-Modus:

```bash
python scripts/validate_reviews.py --path . --advisory
```

Ein hartes Review-Merge-Gate darf erst ergänzt werden, wenn klar definiert ist, welche Phasen, Branches oder Release-Typen vollständige Review-Sets verlangen.

## Automatisiertes CI Quality Gate

ADM-konforme Repositories sollen Qualitätsregeln nicht nur dokumentieren, sondern automatisiert prüfen.

Das erste verpflichtende Gate ist der Line-Limit-Check:

- Workflow: `.github/workflows/adm-quality-gate.yml`
- Skript: `scripts/check_limits.py`
- Standardlimit: 300 Zeilen pro Quellcodedatei
- Ausführung: `push`, `pull_request` und manuell über `workflow_dispatch`

Der Review-Validator läuft im gleichen Workflow zunächst nur im Advisory-Modus.

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
