# ADM — Spezifikation (v0.26 Draft)

Das Agentic Development Manifest (ADM) ist ein modellneutraler, dateibasierter Standard für die Softwareentwicklung mit KI-Agenten. Dieses Dokument dient als kanonische Spezifikation des Regelwerks.

## 1. Status / Version

- **Version**: v0.26 Draft
- **Zustand**: Review Archive Policy Accepted
- **Letztes Update**: 2026-07-08

## 2. ADM Prinzipien

ADM basiert auf drei Grundpfeilern, die eine langfristige Wartbarkeit und Modellunabhängigkeit garantieren:

1. **Modell-Neutralität**: Der Standard setzt keine spezifischen LLM-Provider oder proprietären Features voraus. Alle Logik ist lokal ausführbar oder klar als extern markiert.
2. **CLI-First**: Die Interaktion und Validierung erfolgt primär über Terminal-Tools. Das Repository ist für Agenten ohne grafische Oberfläche optimiert.
3. **Repository-Backed Truth**: Das Repository ist die einzige Quelle der Wahrheit. Projektgedächtnis, Entscheidungen, Rollen, Reviews, Review Archive Policy, Handovers, SaaS Foundation Standards, AI Foundation Standards, Master Prompt Standards, Adapter Prompt Standards, Roadmap Continuation, v1-Readiness-Kriterien, Review and Validation Hardening sowie Foundation Consistency and Release Hygiene müssen als Dateien versioniert oder bewusst als lokal/transient ausgeschlossen sein.

## 3. Entwicklungs-Lifecycle

ADM definiert einen strukturierten Prozess für architekturrelevante Änderungen. Jede Phase endet mit einem expliziten Quality Gate:

- **Phase 0 — Mission & Standards**: Definition von Zielen, Risiken und Qualitätsleitplanken.
- **Phase 1 — Research Engine**: Recherche kritischer Informationen für Architektur, Sicherheit und Kosten.
- **Phase 2 — Architecture Competition**: Vergleich von Varianten, zum Beispiel DDD, Hexagonal oder Event-Driven.
- **Phase 3 — Devil's Advocate**: Aggressive Prüfung auf Schwächen, Kosten und technische Schulden.
- **Phase 4 — Simplification**: Entfernung unnötiger Komplexität vor der Umsetzung.
- **Phase 5 — Roadmap & Plan**: Zerlegung in überprüfbare Arbeitspakete.
- **Phase 6 — Foundation Build**: Aufbau der SaaS- und AI-Foundation vor den Produktfeatures.

Diese Lifecycle-Phasen beschreiben den Ablauf einer architekturrelevanten Änderung. Sie sind nicht identisch mit den Roadmap-Phasen in `ROADMAP.md`.

## 4. Repository Governance

ADM-konforme Repositories unterliegen strengen Sicherheits- und Prozessregeln:

- **Branch Protection**: Der Default-Branch, meistens `main`, ist geschützt. Direkte Pushes sind verboten.
- **Rulesets**: Ein aktives GitHub-Ruleset, zum Beispiel `main-protection`, muss PRs, Konversations-Auflösung und erfolgreiche Status-Checks erzwingen.
- **Merge-Pfad**: Änderungen fließen ausnahmslos über Feature-Branches und Pull Requests nach `main`.
- **No-Bypass**: Es gibt keine Ausnahmen von der Governance-Regel für einzelne Benutzer oder Agenten, solange kein ADR oder gleichwertiger Governance-Beschluss das ausdrücklich erlaubt.

GitHub-Rulesets sind externe Repository-Einstellungen. Source-Dateien dokumentieren die erwartete Einstellung, beweisen aber nicht den aktiven GitHub-Zustand. Governance-relevante Releases erfordern eine manuelle Ruleset-Prüfung.

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
- Ausgefüllte aktive Berichte liegen direkt unter `.ai/reviews/`.
- Archivierte historische Review-Sets dürfen später unter `.ai/reviews/archive/<review_set_id>/` liegen.
- Dateinamen müssen der `review_id` entsprechen, zum Beispiel `REV-ARCH-YYYYMMDD-slug.md`.

Archivierung ist keine Fehlerverbergung. Aktuelle fehlerhafte Reviews müssen repariert werden; sie dürfen nicht verschoben werden, nur um den normalen Validatorpfad grün zu machen.

## 6. Review-Validierungsmodi

Der Validator `scripts/validate_reviews.py` unterstützt drei Modi:

| Modus | Beschreibung | Einsatzbereich |
| --- | --- | --- |
| `advisory` | Meldet Fehler, blockiert aber nicht. | Feature-Branches, frühe Entwicklung. |
| `existing-strict` | Prüft vorhandene Reviews strikt auf Struktur. | Pull Requests, normale Pushes. |
| `complete-set` | Erzwingt alle 6 Rollen, PASSED-Status und Scope-Bindung. | Releases, Phasenübergänge. |

v0.24 akzeptiert diese drei Modi als Review and Validation Hardening Baseline. Normale PRs dürfen dadurch nicht versehentlich complete-set-pflichtig werden.

v0.26 akzeptiert, dass der Standardpfad direkte `.ai/reviews/*.md` Dateien prüft und `.ai/reviews/archive/**` nicht rekursiv in normale Validierung einbezieht.

## 7. Release Gate Policy

Ein Release oder Git-Tag ist nur zulässig, wenn ein vollständiges Review-Set vorliegt und manuell validiert wurde.

- **Manual Release Validation**: Vor dem Tagging muss der Workflow `ADM Quality Gate` manuell auf `main` mit Modus `complete-set` gestartet werden.
- **Parameter**: `review_set_id`, `target_ref` und `reviewed_commit` müssen explizit angegeben werden.
- **Stable reviewed commit**: Der `target_commit` in Review-Artefakten ist der stabile nicht-review Commit, der geprüft wurde.
- **Final tag commit**: Der Release-Tag zeigt auf den finalen `main`-Commit nach Merge der Review-Artefakte und erfolgreicher manueller release-grade Validation.
- **Referenz**: Details siehe `docs/RELEASE_RUNBOOK.md`.

## 8. Runtime Artifact Policy (`.ai/`)

Das `.ai/` Verzeichnis dient als persistente Memory Layer für Agenten.

- **Versioniert**: `.ai/reviews/`, `.ai/reviews/archive/`, `.ai/decisions/`, `.ai/handover/`, `.ai/memory/`, `.ai/knowledge/`, `.ai/tasks/`, `.ai/agents/`, `.ai/README.md`.
- **Ignoriert oder lokal behandelt**: `.ai/tmp/`, `.ai/logs/`, `.ai/cache/`, `.ai/scratch/`, `.ai/local/`, `.ai/sessions/`.
- **Regel**: Keine temporären Chat-Marker, Rohlogs, Secrets, privaten lokalen Pfade oder flüchtigen Notizen im Repository.

Aktive Review-Artefakte liegen direkt unter `.ai/reviews/`. Archivierte Review-Artefakte sind historische Evidenz unter `.ai/reviews/archive/<review_set_id>/` und werden vom Standard-Validatorpfad nicht rekursiv geprüft.

## 9. Project-owned Memory

Project-owned memory ist dauerhaftes Projektwissen, das dem Repository gehört und nicht einem Modell, Chatfenster oder lokalen Tool-Profil.

Autoritätshierarchie:

1. Kanonische Repository-Dokumente: Spezifikation, Constitution, Governance, Foundation Standards, Master Prompt Standard, Adapter Prompt Standard, ADRs, Runbooks.
2. Versionierte Runtime-Artefakte: Reviews, Review-Archive, Handovers, akzeptierte Projektentscheidungen, kuratierte Memory-Notizen.
3. Working-Artefakte: Tasks, Planung, offene Fragen, geprüfte Research-Zusammenfassungen.
4. Lokale transiente Artefakte: Scratch, Logs, Cache, Experimente.
5. Hidden model memory und Chatverlauf: nie autoritative Projektwahrheit.

Memory-Dateien müssen knapp, quellenbewusst, nicht-sensitiv und für zukünftige Agenten prüfbar sein.

## 10. Agent Registry

Die Agent Registry beschreibt repository-owned Agentenrollen. Sie definiert Zuständigkeiten, Lese-Reihenfolge, erwartete Schreibbereiche und Handover-Routing.

Die kanonische Laufzeitposition ist `.ai/agents/`.

Minimalfelder:

| Feld | Zweck |
| --- | --- |
| `agent_id` | Stabiler repository-lokaler Rollen-Identifier |
| `role` | Menschlich lesbarer Rollenname |
| `mission` | Hauptverantwortung |
| `reads` | Pflichtkontext vor Arbeitsbeginn |
| `writes` | Erwartete Schreibbereiche im Scope |
| `forbidden` | Bereiche, die ohne explizite Freigabe tabu sind |
| `handover_to` | Empfohlene nächste Rolle oder Rollenfamilie |
| `review_scope` | Review-Verantwortung, falls vorhanden |

Die Agent Registry ist keine technische Rechteverwaltung. GitHub Rulesets, CI, Code Review und lokale Sandbox-Regeln bleiben die Durchsetzungsmechanismen.

## 11. Handover Automation

Handover Automation definiert strukturierte, repository-owned Übergaben, die später sicher vorbefüllt, gelintet oder validiert werden können.

Die kanonischen Positionen sind:

- `.ai/handover/` für konkrete Session-Handovers.
- `templates/HANDOVER_TEMPLATE.md` für die wiederverwendbare Vorlage.

Handover Automation darf keine Checks, Commits, Review-Votes, Rollen, CI-Ergebnisse oder Freigaben erfinden.

Sie darf nicht mergen, taggen, Branch Protection ändern oder hidden model memory, Chatverlauf, Scratch-Dateien, Rohlogs, private Pfade oder Secrets als autoritative Quellen verwenden.

v0.26 implementiert keine Roadmap Phase 7, keinen Handover-Linter und keine Handover-Automation.

## 12. Foundation Standards

SaaS Foundation Standard, AI Foundation Standard, Master Prompt Standard und Adapter Prompt Standard bleiben gültige Roadmap-Standards. v0.26 verändert deren technische Semantik nicht.

## 13. Review Archive Policy

Die Review Archive Policy ist ein Governance-Hygiene-Block nach v0.25 und vor Roadmap Phase 7.

Sie definiert:

- direkte `.ai/reviews/*.md` Dateien als aktive Review-Fläche,
- `.ai/reviews/archive/<review_set_id>/` als spätere historische Ablage,
- keine historische Migration innerhalb von v0.26,
- keine Änderung an `scripts/validate_reviews.py`,
- einen gezielten Regressionstest für den nicht-rekursiven Standardpfad.

Roadmap Phase 7 bleibt offen, bis diese Archivierungssemantik akzeptiert und überprüft ist.
