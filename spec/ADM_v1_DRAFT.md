# ADM — Spezifikation (v0.25 Draft)

Das Agentic Development Manifest (ADM) ist ein modellneutraler, dateibasierter Standard für die Softwareentwicklung mit KI-Agenten. Dieses Dokument dient als kanonische Spezifikation des Regelwerks.

## 1. Status / Version

- **Version**: v0.25 Draft
- **Zustand**: Foundation Consistency and Release Hygiene Baseline Accepted
- **Letztes Update**: 2026-07-08

## 2. ADM Prinzipien

ADM basiert auf drei Grundpfeilern, die eine langfristige Wartbarkeit und Modellunabhängigkeit garantieren:

1. **Modell-Neutralität**: Der Standard setzt keine spezifischen LLM-Provider oder proprietären Features voraus. Alle Logik ist lokal ausführbar oder klar als extern markiert.
2. **CLI-First**: Die Interaktion und Validierung erfolgt primär über Terminal-Tools. Das Repository ist für Agenten ohne grafische Oberfläche optimiert.
3. **Repository-Backed Truth**: Das Repository ist die einzige Quelle der Wahrheit. Projektgedächtnis, Entscheidungen, Rollen, Reviews, Handovers, SaaS Foundation Standards, AI Foundation Standards, Master Prompt Standards, Adapter Prompt Standards, Roadmap Continuation, v1-Readiness-Kriterien, Review and Validation Hardening sowie Foundation Consistency and Release Hygiene müssen als Dateien versioniert oder bewusst als lokal/transient ausgeschlossen sein.

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
- Ausgefüllte Berichte liegen unter `.ai/reviews/`.
- Dateinamen müssen der `review_id` entsprechen, zum Beispiel `REV-ARCH-YYYYMMDD-slug.md`.

## 6. Review-Validierungsmodi

Der Validator `scripts/validate_reviews.py` unterstützt drei Modi:

| Modus | Beschreibung | Einsatzbereich |
| --- | --- | --- |
| `advisory` | Meldet Fehler, blockiert aber nicht. | Feature-Branches, frühe Entwicklung. |
| `existing-strict` | Prüft vorhandene Reviews strikt auf Struktur. | Pull Requests, normale Pushes. |
| `complete-set` | Erzwingt alle 6 Rollen, PASSED-Status und Scope-Bindung. | Releases, Phasenübergänge. |

v0.24 akzeptiert diese drei Modi als Review and Validation Hardening Baseline. Normale PRs dürfen dadurch nicht versehentlich complete-set-pflichtig werden.

## 7. Release Gate Policy

Ein Release oder Git-Tag ist nur zulässig, wenn ein vollständiges Review-Set vorliegt und manuell validiert wurde.

- **Manual Release Validation**: Vor dem Tagging muss der Workflow `ADM Quality Gate` manuell auf `main` mit Modus `complete-set` gestartet werden.
- **Parameter**: `review_set_id`, `target_ref` und `reviewed_commit` müssen explizit angegeben werden.
- **Stable reviewed commit**: Der `target_commit` in Review-Artefakten ist der stabile nicht-review Commit, der geprüft wurde.
- **Final tag commit**: Der Release-Tag zeigt auf den finalen `main`-Commit nach Merge der Review-Artefakte und erfolgreicher manueller release-grade Validation.
- **Referenz**: Details siehe `docs/RELEASE_RUNBOOK.md`.

## 8. Runtime Artifact Policy (`.ai/`)

Das `.ai/` Verzeichnis dient als persistente Memory Layer für Agenten.

- **Versioniert**: `.ai/reviews/`, `.ai/decisions/`, `.ai/handover/`, `.ai/memory/`, `.ai/knowledge/`, `.ai/tasks/`, `.ai/agents/`, `.ai/README.md`.
- **Ignoriert oder lokal behandelt**: `.ai/tmp/`, `.ai/logs/`, `.ai/cache/`, `.ai/scratch/`, `.ai/local/`, `.ai/sessions/`.
- **Regel**: Keine temporären Chat-Marker, Rohlogs, Secrets, privaten lokalen Pfade oder flüchtigen Notizen im Repository.

## 9. Project-owned Memory

Project-owned memory ist dauerhaftes Projektwissen, das dem Repository gehört und nicht einem Modell, Chatfenster oder lokalen Tool-Profil.

Autoritätshierarchie:

1. Kanonische Repository-Dokumente: Spezifikation, Constitution, Governance, Foundation Standards, Master Prompt Standard, Adapter Prompt Standard, ADRs, Runbooks.
2. Versionierte Runtime-Artefakte: Reviews, Handovers, akzeptierte Projektentscheidungen, kuratierte Memory-Notizen.
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

v0.25 implementiert keine Roadmap Phase 7, keinen Handover-Linter und keine Handover-Automation.

## 12. SaaS Foundation Standard

Der SaaS Foundation Standard ist der kanonische **Roadmap-Phase-2-Block** für neue SaaS-Systeme. Das ist bewusst von **Lifecycle Phase 2 — Architecture Competition** aus Abschnitt 3 getrennt.

Ziel ist eine kleine, explizite Foundation vor Produktfeatures. ADM erzwingt keinen bestimmten Anbieter und keine Microservice-Architektur. Der Default ist Modular Monolith First.

Pflichtbereiche:

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

Roadmap Phase 2 implementiert keine konkrete Produktlogik, keine echte Payment-Integration, keine AI Provider Architecture, kein Modellrouting und keine Prompt Registry.

## 13. AI Foundation Standard

Der AI Foundation Standard ist der kanonische **Roadmap-Phase-3-Block** für KI-Funktionen. Das ist bewusst von **Lifecycle Phase 3 — Devil's Advocate** aus Abschnitt 3 getrennt.

Ziel ist eine kleine, explizite KI-Foundation vor produktbezogenen KI-Features. ADM erzwingt keinen LLM-Provider, kein Runtime-Framework, keine Prompt-Datenbank und keine Tool-Ausführungsengine.

Pflichtbereiche:

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

Roadmap Phase 3 implementiert keine konkrete KI-Funktion, keine Provider-SDK-Integration, keine echten Modellaufrufe, keine echte Tool-Ausführung, keine Prompt-Datenbank, keine neue Validator- oder Workflow-Erzwingung und keine Provider-Secrets.

## 14. Master Prompt Standard

Der Master Prompt Standard ist der kanonische **Roadmap-Phase-4-Block** für CLI-Agenten-Onboarding. Das ist bewusst von **Lifecycle Phase 4 — Simplification** aus Abschnitt 3 getrennt.

Ziel ist eine modellneutrale Startanweisung, die ADM-Regeln in operative Agentenschritte übersetzt. Der Master Prompt ist kein Tool-Adapter, keine Runtime-Engine, kein Validator und keine Freigabeinstanz.

Pflichtbereiche:

| Bereich | Mindestentscheidung |
| --- | --- |
| Authority Order | Repository-Dokumente, `.ai/`-Artefakte und Chatverlauf werden klar priorisiert |
| Required Initialization | Agenten lesen relevante kanonische Dokumente vor Umsetzung |
| Scope Declaration | Rolle, Ziel, Scope, Non-Scope und Risiken werden vor Umsetzung genannt |
| Operating Rules | Keine erfundenen Fakten, Checks, Commits, Rollen, Reviews oder Freigaben |
| Quality Gate Contract | Checks, Review-Status und CI-Readiness werden belegbar gemeldet |
| Review Contract | Complete-set und Review-Artefakte bleiben versioniert und scoped |
| Foundation Triggers | SaaS- und AI-Foundation werden bei passenden Tasks aktiviert |
| Handover Contract | Signifikante Sitzungen enden mit prüfbarer Übergabe |
| Adapter Boundary | Tool-spezifische Prompts bleiben dünne Schichten unterhalb des Master Prompts |

Roadmap Phase 4 implementiert keinen Tool-Adapter, keine Runtime, keine Provider-Integration, keine Workflow-Änderung und keinen MCP.

## 15. Adapter Prompt Standard

Der Adapter Prompt Standard ist der kanonische **Roadmap-Phase-5-Block** für tool-spezifische CLI-Agenten-Prompts.

Adapter sind dünne, untergeordnete Schichten unter `prompts/master_prompt.md`. Sie dürfen Tool-Bedienung erklären, aber keine ADM-Regel abschwächen.

Pflichtbereiche:

| Bereich | Mindestentscheidung |
| --- | --- |
| Canonical dependency | Adapter verweisen auf `prompts/master_prompt.md` und ersetzen ihn nicht |
| Tool capability boundary | Adapter unterscheiden Tool-Fähigkeit von Tool-Wahrheit |
| Tool state boundary | Hidden memory, Chatverlauf, lokale Profile und Cache bleiben nicht autoritativ |
| Forbidden overrides | Adapter dürfen Governance, Reviews, ADRs, Checks und Handover nicht umgehen |
| Deferred adapters | Nicht geprüfte Tools bleiben explizit zurückgestellt |

Roadmap Phase 5 implementiert keinen Runtime-Code, keine Provider-SDKs, keine MCP-Integration, keine lokale Tool-Profile und keine zusätzlichen Tool-Adapter ohne aktuelle Verifikation.

## 16. Roadmap Continuation and v1 Readiness

Roadmap Phase 6 bis Phase 9 sind dokumentierte künftige Blöcke nach den ersten fünf Roadmap-Phasen.

v1-Readiness erfordert synchronisierte Spezifikation, Roadmap, Changelog, ADRs und Review-Artefakte. Ein v1 Release Candidate braucht ein vollständiges sechs Rollen Review-Set und manuelle release-grade `complete-set` Validierung.

v1 erfordert keine Runtime, Provider-SDKs, MCP-Integration, lokalen Tool-Profile, Workflow-Änderungen oder Release-Automation, solange diese nicht durch spätere explizite Roadmap-Phasen und ADRs akzeptiert werden.
