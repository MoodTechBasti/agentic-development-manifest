# ADM — Spezifikation (v0.2 Draft)

Dieses Dokument spezifiziert den aktuellen Draft-Zustand des Agentic Development Manifest.

## Status

- Version: v0.2 Draft
- Zustand: Quality Hardening
- Ziel: modellneutraler Standard für CLI-basierte Softwareentwicklung mit verbindlichen Qualitätsleitplanken

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
- keine Secrets oder Credentials sind im Repository hardcodiert
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

Eine Phase darf erst abgeschlossen werden, wenn Entscheidungen, Risiken, offene Fragen, Tests, Metriken und nächste Schritte dokumentiert sind.
