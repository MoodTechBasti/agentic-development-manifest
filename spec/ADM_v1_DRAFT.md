# ADM — Spezifikation (v0.16 Draft)

Das Agentic Development Manifest (ADM) ist ein modellneutraler, dateibasierter Standard für die Softwareentwicklung mit KI-Agenten. Dieses Dokument dient als kanonische Spezifikation des Regelwerks.

## 1. Status / Version

- **Version**: v0.16 Draft
- **Zustand**: Project-owned Memory Architecture Proposed
- **Letztes Update**: 2026-07-08

## 2. ADM Prinzipien

ADM basiert auf drei Grundpfeilern, die eine langfristige Wartbarkeit und Modellunabhängigkeit garantieren:

1. **Modell-Neutralität**: Der Standard setzt keine spezifischen LLM-Provider oder proprietären Features voraus. Alle Logik ist lokal ausführbar.
2. **CLI-First**: Die Interaktion und Validierung erfolgt primär über Terminal-Tools. Das Repository ist für Agenten ohne grafische Oberfläche optimiert.
3. **Repository-Backed Truth**: Das Repository ist die einzige Quelle der Wahrheit. Projektgedächtnis, Entscheidungen und Reviews müssen als Dateien versioniert oder bewusst als lokal/transient ausgeschlossen sein.

## 3. Entwicklungs-Lifecycle

ADM definiert einen strukturierten Prozess für architekturrelevante Änderungen. Jede Phase endet mit einem expliziten Quality Gate:

- **Phase 0 — Mission & Standards**: Definition von Zielen, Risiken und Qualitätsleitplanken.
- **Phase 1 — Research Engine**: Recherche kritischer Informationen für Architektur, Sicherheit und Kosten.
- **Phase 2 — Architecture Competition**: Vergleich von Varianten (z.B. DDD, Hexagonal, Event-Driven).
- **Phase 3 — Devil's Advocate**: Aggressive Prüfung auf Schwächen, Kosten und technische Schulden.
- **Phase 4 — Simplification**: Entfernung unnötiger Komplexität vor der Umsetzung.
- **Phase 5 — Roadmap & Plan**: Zerlegung in überprüfbare Arbeitspakete.
- **Phase 6 — Foundation Build**: Aufbau der SaaS-Foundation vor den Produktfeatures.

## 4. Repository Governance

ADM-konforme Repositories unterliegen strengen Sicherheits- und Prozessregeln:

- **Branch Protection**: Der Default-Branch (meist `main`) ist geschützt. Direkte Pushes sind verboten.
- **Rulesets**: Ein aktives GitHub-Ruleset (z.B. `main-protection`) muss PRs, Konversations-Auflösung und erfolgreiche Status-Checks erzwingen.
- **Merge-Pfad**: Änderungen fließen ausnahmslos über Feature-Branches und Pull Requests nach `main`.
- **No-Bypass**: Es gibt keine Ausnahmen von der Governance-Regel für einzelne Benutzer oder Agenten.

## 5. Review Governance

Jede wesentliche Änderung erfordert ein strukturiertes Review-Set.

### Review-Rollen

Ein vollständiges Review-Set besteht aus sechs Rollen:

- **Architect Review**: Architektur, Wartbarkeit, Skalierbarkeit.
- **Security Review**: Bedrohungsmodelle, Datensicherheit, Tenant-Isolation.
- **Performance Review**: Latenzen, Ressourcen-Effizienz, Budgets.
- **Cost Review**: Token-Verbrauch, API-Kosten, Infrastruktur-Ausgaben.
- **Simplifier Review**: Komplexitätsreduktion, Abhängigkeitsprüfung.
- **Documentation Review**: Vollständigkeit der Doku, Runbooks, ADRs.

### Review-Artefakte

- Templates liegen unter `templates/reviews/`.
- Ausgefüllte Berichte liegen unter `.ai/reviews/`.
- Dateinamen müssen der `review_id` entsprechen (z.B. `REV-ARCH-YYYYMMDD-slug.md`).

## 6. Review-Validierungsmodi

Der Validator `scripts/validate_reviews.py` unterstützt drei Modi:

| Modus | Beschreibung | Einsatzbereich |
| --- | --- | --- |
| `advisory` | Meldet Fehler, blockiert aber nicht. | Feature-Branches, frühe Entwicklung. |
| `existing-strict` | Prüft vorhandene Reviews strikt auf Struktur. | Pull Requests, normale Pushes. |
| `complete-set` | Erzwingt alle 6 Rollen, PASSED-Status und Scope-Bindung. | Releases, Phasenübergänge. |

## 7. Release Gate Policy

Ein Release (Git Tag) ist nur zulässig, wenn ein vollständiges Review-Set vorliegt und manuell validiert wurde.

- **Manual Release Validation**: Vor dem Tagging muss der Workflow `ADM Quality Gate` manuell auf `main` mit Modus `complete-set` gestartet werden.
- **Parameter**: `review_set_id`, `target_ref` (Override) und `reviewed_commit` (SHA) müssen explizit angegeben werden.
- **Referenz**: Details siehe `docs/RELEASE_RUNBOOK.md`.

## 8. Runtime Artifact Policy (`.ai/`)

Das `.ai/` Verzeichnis dient als persistente Memory Layer für Agenten.

- **Versioniert**: `.ai/reviews/`, `.ai/decisions/`, `.ai/handover/`, `.ai/memory/`, `.ai/knowledge/`, `.ai/tasks/`, `.ai/README.md`.
- **Ignoriert oder lokal behandelt**: `.ai/tmp/`, `.ai/logs/`, `.ai/cache/`, `.ai/scratch/`, `.ai/local/`, `.ai/sessions/`.
- **Regel**: Keine temporären Chat-Marker, Rohlogs, Secrets, privaten lokalen Pfade oder flüchtigen Notizen im Repository.

## 9. Project-owned Memory

Project-owned memory ist dauerhaftes Projektwissen, das dem Repository gehört und nicht einem Modell, Chatfenster oder lokalen Tool-Profil.

### Autoritätshierarchie

1. Kanonische Repository-Dokumente: Spezifikation, Constitution, Governance, ADRs, Runbooks.
2. Versionierte Runtime-Artefakte: Reviews, Handovers, akzeptierte Projektentscheidungen, kuratierte Memory-Notizen.
3. Working-Artefakte: Tasks, Planung, offene Fragen, geprüfte Research-Zusammenfassungen.
4. Lokale transiente Artefakte: Scratch, Logs, Cache, Experimente.
5. Hidden model memory und Chatverlauf: nie autoritative Projektwahrheit.

### Speicherklassen

| Klasse | Zweck | Beispiel |
| --- | --- | --- |
| `canonical` | Normative Projektwahrheit | `spec/`, `docs/decisions/`, `docs/REPOSITORY_GOVERNANCE.md` |
| `runtime` | Ausgeführte Agentenarbeit | `.ai/reviews/`, `.ai/handover/`, `.ai/decisions/` |
| `working` | Koordination kommender Arbeit | `.ai/tasks/`, `.ai/planning/` |
| `knowledge` | Kuratierte Recherche und Projektkontext | `.ai/knowledge/`, `.ai/memory/` |
| `transient` | Lokale Tool-Ausgaben | `.ai/tmp/`, `.ai/cache/`, `.ai/logs/` |

Memory-Dateien müssen knapp, quellenbewusst, nicht-sensitiv und für zukünftige Agenten prüfbar sein.

## 10. PR Hygiene Policy

Pull Requests müssen die Selbsterklärung des Agenten widerspiegeln.

- **Inhalt**: PR-Bodies dürfen keine ungelösten Platzhalter, leere Pflichtfelder oder ungeprüfte Checkboxen enthalten.
- **Vorlage**: Die Nutzung von `.github/pull_request_template.md` ist verpflichtend.
- **Qualität**: Ein PR ohne inhaltlich wertvolle Summary und Validierung ist ein Governance-Fehler.

## 11. Agent Onboarding Contract

Jeder Agent muss seine Arbeit mit dem `prompts/master_prompt.md` beginnen. Dieser Prompt definiert:

- Die notwendige Initialisierung (Lese-Reihenfolge der Doku).
- Die verpflichtenden Qualitäts-Checks (`check_limits.py`, `validate_reviews.py`).
- Die Regeln für Handover und Decision Records.

## 12. Quality Gates / Definition of Done

- **Line-Limit**: Quellcodedateien dürfen 300 Zeilen nicht überschreiten (automatisch geprüft durch `scripts/check_limits.py`).
- **Exemptions**: Ausnahmen erfordern ein ACCEPTED ADR mit dem Tag `ADM-Exemption: path/to/file (Max: lines)`.
- **Testing**: Neue Logik muss durch Tests abgedeckt sein.
- **Handover**: Jede Sitzung endet mit einem strukturierten Handover.