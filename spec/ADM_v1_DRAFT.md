# ADM — Spezifikation (v0.20 Draft)

Das Agentic Development Manifest (ADM) ist ein modellneutraler, dateibasierter Standard für die Softwareentwicklung mit KI-Agenten. Dieses Dokument dient als kanonische Spezifikation des Regelwerks.

## 1. Status / Version

- **Version**: v0.20 Draft
- **Zustand**: AI Foundation Standard Accepted
- **Letztes Update**: 2026-07-08

## 2. ADM Prinzipien

ADM basiert auf drei Grundpfeilern, die eine langfristige Wartbarkeit und Modellunabhängigkeit garantieren:

1. **Modell-Neutralität**: Der Standard setzt keine spezifischen LLM-Provider oder proprietären Features voraus. Alle Logik ist lokal ausführbar.
2. **CLI-First**: Die Interaktion und Validierung erfolgt primär über Terminal-Tools. Das Repository ist für Agenten ohne grafische Oberfläche optimiert.
3. **Repository-Backed Truth**: Das Repository ist die einzige Quelle der Wahrheit. Projektgedächtnis, Entscheidungen, Rollen, Reviews, Handovers, SaaS Foundation Standards und AI Foundation Standards müssen als Dateien versioniert oder bewusst als lokal/transient ausgeschlossen sein.

## 3. Entwicklungs-Lifecycle

ADM definiert einen strukturierten Prozess für architekturrelevante Änderungen. Jede Phase endet mit einem expliziten Quality Gate:

- **Phase 0 — Mission & Standards**: Definition von Zielen, Risiken und Qualitätsleitplanken.
- **Phase 1 — Research Engine**: Recherche kritischer Informationen für Architektur, Sicherheit und Kosten.
- **Phase 2 — Architecture Competition**: Vergleich von Varianten (z.B. DDD, Hexagonal, Event-Driven).
- **Phase 3 — Devil's Advocate**: Aggressive Prüfung auf Schwächen, Kosten und technische Schulden.
- **Phase 4 — Simplification**: Entfernung unnötiger Komplexität vor der Umsetzung.
- **Phase 5 — Roadmap & Plan**: Zerlegung in überprüfbare Arbeitspakete.
- **Phase 6 — Foundation Build**: Aufbau der SaaS- und AI-Foundation vor den Produktfeatures.

Diese Lifecycle-Phasen beschreiben den Ablauf einer architekturrelevanten Änderung. Sie sind nicht identisch mit den Roadmap-Phasen in `ROADMAP.md`.

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

- **Versioniert**: `.ai/reviews/`, `.ai/decisions/`, `.ai/handover/`, `.ai/memory/`, `.ai/knowledge/`, `.ai/tasks/`, `.ai/agents/`, `.ai/README.md`.
- **Ignoriert oder lokal behandelt**: `.ai/tmp/`, `.ai/logs/`, `.ai/cache/`, `.ai/scratch/`, `.ai/local/`, `.ai/sessions/`.
- **Regel**: Keine temporären Chat-Marker, Rohlogs, Secrets, privaten lokalen Pfade oder flüchtigen Notizen im Repository.

## 9. Project-owned Memory

Project-owned memory ist dauerhaftes Projektwissen, das dem Repository gehört und nicht einem Modell, Chatfenster oder lokalen Tool-Profil.

### Autoritätshierarchie

1. Kanonische Repository-Dokumente: Spezifikation, Constitution, Governance, Foundation Standards, ADRs, Runbooks.
2. Versionierte Runtime-Artefakte: Reviews, Handovers, akzeptierte Projektentscheidungen, kuratierte Memory-Notizen.
3. Working-Artefakte: Tasks, Planung, offene Fragen, geprüfte Research-Zusammenfassungen.
4. Lokale transiente Artefakte: Scratch, Logs, Cache, Experimente.
5. Hidden model memory und Chatverlauf: nie autoritative Projektwahrheit.

Memory-Dateien müssen knapp, quellenbewusst, nicht-sensitiv und für zukünftige Agenten prüfbar sein.

## 10. Agent Registry

Die Agent Registry beschreibt repository-owned Agentenrollen. Sie definiert Zuständigkeiten, Lese-Reihenfolge, erwartete Schreibbereiche und Handover-Routing.

Die kanonische Laufzeitposition ist `.ai/agents/`.

### Minimalfelder

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

## 12. SaaS Foundation Standard

Der SaaS Foundation Standard ist der kanonische **Roadmap-Phase-2-Block** für neue SaaS-Systeme. Das ist bewusst von **Lifecycle Phase 2 — Architecture Competition** aus Abschnitt 3 getrennt.

Ziel ist eine kleine, explizite Foundation vor Produktfeatures. ADM erzwingt keinen bestimmten Anbieter und keine Microservice-Architektur. Der Default ist Modular Monolith First.

### Pflichtbereiche

Ein SaaS-Foundation-Entwurf muss mindestens folgende Bereiche entscheiden oder bewusst als nicht anwendbar markieren:

| Bereich | Mindestentscheidung |
| --- | --- |
| Identity | User, Authentifizierung und technische Identitäten |
| Organization | Besitz, Vertrag, Abrechnung und Teamverwaltung |
| Tenant | Daten-, Konfigurations-, Limit-, Job-, Storage- und Audit-Isolation |
| Workspace | Arbeitsbereiche unterhalb von Organization oder Tenant |
| Membership | Einladungen, Rollen, Deaktivierung und Besitzwechsel |
| Roles and Permissions | serverseitige Autorisierung und kritische Aktionen |
| Billing Readiness | Plan-, Subscription- und Provider-Adapter-Modell ohne Lock-in |
| Entitlements and Quotas | Feature-Gates, Nutzungslimits und Planlogik |
| Usage and Cost | Kostenaggregation pro User, Workspace, Tenant, Feature, Request, Worker-Zeit und Provider |
| Jobs and Workers | Idempotenz, Retries, Backoff, Timeouts, Dead-Letter und Status |
| Observability and Admin | Logs, Metrics, Request IDs, Audit Logs und Support-Diagnose |
| Data Lifecycle | Upload, Processing, Export, Archive, Delete, Backup und Restore |
| DX and Testing | lokaler Startpfad, Mocks, Fake Billing, Seed-Daten und Foundation-Tests |

### Grenzen

Roadmap Phase 2 implementiert keine konkrete Produktlogik, keine echte Payment-Integration, keine AI Provider Architecture, kein Modellrouting und keine Prompt Registry. Diese Themen folgen in Roadmap Phase 3 oder produktspezifischen ADRs.

## 13. AI Foundation Standard

Der AI Foundation Standard ist der kanonische **Roadmap-Phase-3-Block** für KI-Funktionen. Das ist bewusst von **Lifecycle Phase 3 — Devil's Advocate** aus Abschnitt 3 getrennt.

Ziel ist eine kleine, explizite KI-Foundation vor produktbezogenen KI-Features. ADM erzwingt keinen LLM-Provider, kein Runtime-Framework, keine Prompt-Datenbank und keine Tool-Ausführungsengine.

### Pflichtbereiche

Ein AI-Foundation-Entwurf muss mindestens folgende Bereiche entscheiden oder bewusst als nicht anwendbar markieren:

| Bereich | Mindestentscheidung |
| --- | --- |
| Provider Abstraction | Austauschbare Provider- und Modellfähigkeiten ohne SDK-Lock-in |
| Prompt Registry | Prompt-IDs, Versionen, Owner, Inputs, Outputs, Safety-Annahmen und Änderungsregeln |
| Tool Registry | erlaubte Tools, Permissions, Side Effects, Audit, Rate Limits und Human-Approval-Punkte |
| Evaluation | Golden Cases, Negative Cases, Qualitätskriterien, Kosten, Latenz und Regressionserkennung |
| AI Cost Tracking | Kostenaggregation pro User, Tenant, Feature, Prompt, Tool, Provider, Request, Job und Cache-Verhalten |
| Routing | Auswahlregeln für Provider, Modellklasse, Qualität, Kosten, Latenz oder lokale Ausführung |
| Fallback | Verhalten bei Fehlern, Timeouts, Kostenlimits, Safety-Blocks oder Qualitätsproblemen |
| Caching | Cachebarkeit, Tenant-Kontext, Prompt-Version, TTL, Invalidierung und Data Lifecycle |
| Safety Rules | Grenzen für Datenklassen, Prompt Injection, Tools, PII, Secrets, Logs, Cache und Evaluation |
| Observability and Audit | Request IDs, Provider-, Modell-, Prompt-, Tool-, Kosten-, Token-, Latenz- und Fallback-Metadaten |
| AI Artifact Lifecycle | Prompts, Antworten, Tool-Inputs, Tool-Outputs, Embeddings, Evaluation, Cache und Worker-Zwischenstände |

### Grenzen

Roadmap Phase 3 implementiert keine konkrete KI-Funktion, keine Provider-SDK-Integration, keine echten Modellaufrufe, keine echte Tool-Ausführung, keine Prompt-Datenbank, keine neue Validator- oder Workflow-Erzwingung und keine Provider-Secrets.

Roadmap Phase 3 baut auf Roadmap Phase 2 auf. KI-Kosten, KI-Jobs, KI-Artefakte, KI-Logs und KI-Tools müssen an User-, Tenant-, Permission-, Quota-, Billing- und Data-Lifecycle-Entscheidungen anschließen.

## 14. PR Hygiene Policy

Pull Requests müssen die Selbsterklärung des Agenten widerspiegeln.

- **Inhalt**: PR-Bodies dürfen keine ungelösten Platzhalter, leere Pflichtfelder oder ungeprüfte Checkboxen enthalten.
- **Vorlage**: Die Nutzung von `.github/pull_request_template.md` ist verpflichtend.
- **Qualität**: Ein PR ohne inhaltlich wertvolle Summary und Validierung ist ein Governance-Fehler.

## 15. Agent Onboarding Contract

Jeder Agent muss seine Arbeit mit dem `prompts/master_prompt.md` beginnen. Dieser Prompt definiert:

- Die notwendige Initialisierung (Lese-Reihenfolge der Doku und Agent Registry).
- Die verpflichtenden Qualitäts-Checks (`check_limits.py`, `validate_reviews.py`).
- Die Regeln für Handover und Decision Records.
- Die Pflicht, `docs/SAAS_FOUNDATION_BLUEPRINT.md` zu lesen, wenn eine Aufgabe SaaS-Architektur, Mandanten, Billing, Jobs, Observability, Admin, Data Lifecycle oder Foundation-Standards betrifft.
- Die Pflicht, `docs/AI_FOUNDATION_STANDARD.md` zu lesen, wenn eine Aufgabe KI-Provider, Prompts, Tools, Evaluation, Routing, Fallback, Caching, Safety, AI Cost Tracking, KI-Artefakte oder AI Foundation Standards betrifft.

## 16. Quality Gates / Definition of Done

- **Line-Limit**: Quellcodedateien dürfen 300 Zeilen nicht überschreiten (automatisch geprüft durch `scripts/check_limits.py`).
- **Exemptions**: Ausnahmen erfordern ein ACCEPTED ADR mit dem Tag `ADM-Exemption: path/to/file (Max: lines)`.
- **Testing**: Neue Logik muss durch Tests abgedeckt sein.
- **SaaS Foundation**: Produktfeatures dürfen Foundation-Grenzen wie Tenant, Permissions, Billing Readiness, Quotas, Jobs, Observability und Data Lifecycle nicht implizit oder undokumentiert umgehen.
- **AI Foundation**: KI-Features dürfen Provider, Prompts, Tools, Evaluation, Kosten, Routing, Fallback, Caching, Safety, Observability und KI-Artefakt-Lifecycle nicht implizit oder undokumentiert umgehen.
- **Handover**: Jede signifikante Sitzung endet mit einem strukturierten Handover, das Checks, Risiken, geänderte Dateien, Review-Status, aktive Rolle und nächste Schritte nachvollziehbar dokumentiert.
