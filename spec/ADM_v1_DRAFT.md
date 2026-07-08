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
| Authority Order | Repository-Dokumente, `.ai/`-Artefakte und kuratierter Kontext vor Chat, hidden memory oder Tool-Cache |
| Required Initialization | Pflichtlektüre und relevante `.ai/`-Prüfung vor Umsetzung |
| Scope Declaration | Rolle, Ziel, betroffene Bereiche, ausgeschlossene Bereiche, Annahmen, Risiken und nächste Aktion |
| Operating Rules | Verbot erfundener Dateien, Commits, Checks, Rollen, CI-Ergebnisse, Review-Votes oder Freigaben |
| Decision Rules | ADR-Auslöser und proportionale Governance für kleine Änderungen |
| Quality Gate Contract | Lokale Checks, Review-Validatoren und vollständige Review-Sets für Governance-Änderungen |
| Review Contract | Sechs Rollen, gemeinsamer `review_set_id`, `target_ref` und stabiler `target_commit` |
| Release Hygiene Contract | stabile reviewed commits, finaler tag commit und manuelle release-grade Validation |
| Foundation Triggers | Pflichtkontext für SaaS Foundation und AI Foundation bei betroffenen Aufgaben |
| Handover Contract | Strukturierte Übergabe mit Checks, Risiken, geänderten Dateien, Review-Status und nächsten Schritten |
| Adapter Boundary | Trennung zwischen kanonischem Master Prompt und späteren tool-spezifischen Adapter-Prompts |

Roadmap Phase 4 implementiert keine Runtime, keine Provider- oder Tool-Integration, keine CLI-spezifischen Adapter-Prompts, keine lokalen Tool-Profile, keine MCP-Integration, keine Schemas, keine Validatoren und keine Workflow-Änderungen ohne gesondertes GO.

## 15. Adapter Prompt Standard

Der Adapter Prompt Standard ist der kanonische **Roadmap-Phase-5-Block** für tool-spezifische CLI-Agenten-Prompts. Das ist bewusst von **Lifecycle Phase 5 — Roadmap & Plan** aus Abschnitt 3 getrennt.

Ziel ist eine dünne Adapter-Schicht unterhalb des kanonischen Master Prompts. Adapter Prompts helfen konkreten CLI-Tools beim Arbeiten, ersetzen aber weder die ADM-Spezifikation noch `prompts/master_prompt.md`.

Pflichtbereiche:

| Bereich | Mindestentscheidung |
| --- | --- |
| Canonical Dependency | Verweis auf `prompts/master_prompt.md` als autoritativen Startpunkt |
| Supported Tool | Konkrete CLI oder generische Tool-Familie |
| Tool Capabilities | Welche Tool-Funktionen als Arbeitshilfe genutzt werden dürfen |
| Tool State Boundary | Hidden memory, Chatverlauf, Tool-Cache und lokale Profile sind nie Projektwahrheit |
| Forbidden Overrides | Keine Abschwächung von ADM-Regeln, Checks, Reviews, ADRs, PR-Hygiene, Release Hygiene oder Handover |
| Quality Gate Handling | Checks müssen mit Evidenz berichtet werden; unrun checks bleiben `NOT RUN` |
| Handover Handling | Handover bleibt repository-owned und evidenzbasiert |
| Deferred Candidates | Nicht akzeptierte Adapter dürfen nicht als implementiert gelten |

Roadmap Phase 5 implementiert keine Runtime, keine Provider-SDKs, keine echte Tool-Integration, keine lokalen Tool-Profile, keine MCP-Integration, keine Schemas, keine Validatoren, keine Workflows, keine Release-Automation und keine Provider-Secrets.

Initial akzeptierte Adapter sind Claude Code CLI, Codex CLI und Generic CLI Agent. Gemini CLI und Antigravity CLI bleiben deferred candidates bis zu späterer expliziter Freigabe.

## 16. Roadmap Continuation, Review Hardening, and Foundation Hygiene

Roadmap Continuation ist der kanonische v0.23-Planungsblock nach Roadmap Phase 5. Er definiert Roadmap Phase 6 bis Roadmap Phase 9 und v1-Readiness-Kriterien, ohne die späteren Mechanismen zu implementieren.

Review and Validation Hardening Baseline ist der kanonische v0.24-Roadmap-Phase-6-Block. Er akzeptiert die bestehenden Review-Validation-Modi und Review-Set-Scoping-Semantik, korrigiert ADR-Status-Drift und ergänzt gezielte Scope-Regressionstests.

Foundation Consistency and Release Hygiene Baseline ist der kanonische v0.25-Konsolidierungsblock. Er synchronisiert Status- und Versionssprache, modernisiert Release-Hygiene, präzisiert manuelle Ruleset-Audits und hält Roadmap Phase 7 bewusst offen.

Das ist bewusst von Lifecycle Phase 5 — Roadmap & Plan und Lifecycle Phase 6 — Foundation Build aus Abschnitt 3 getrennt.

v1-Readiness verlangt mindestens synchronisierte Roadmap-Phasen, Spezifikation, README, Changelog, akzeptierte ADRs, vollständige sechs Rollen Review-Evidenz, manuelle Ruleset-Audit-Evidenz für governance-relevante Releases und release-grade `complete-set`-Validierung für den Zielzustand.

Deferred Adapter wie Gemini CLI und Antigravity CLI dürfen nicht als akzeptiert gelten, bevor ihr aktuelles Tool-Verhalten verifiziert und explizit freigegeben wurde.

v0.25 implementiert keine Roadmap Phase 7, Handover-Automation, Workflow-Härtung, Release-Automation, Runtime, Provider-SDKs, MCP-Integration, lokale Tool-Profile, Gemini CLI Adapter, Antigravity CLI Adapter oder Provider-Secrets.

## 17. PR Hygiene Policy

Pull Requests müssen die Selbsterklärung des Agenten widerspiegeln.

- **Inhalt**: PR-Bodies dürfen keine ungelösten Platzhalter, leere Pflichtfelder oder ungeprüfte Checkboxen enthalten.
- **Vorlage**: Die Nutzung von `.github/pull_request_template.md` ist verpflichtend.
- **Qualität**: Ein PR ohne inhaltlich wertvolle Summary und Validierung ist ein Governance-Fehler.

## 18. Agent Onboarding Contract

Jeder Agent muss seine Arbeit mit dem `prompts/master_prompt.md` beginnen. Dieser Prompt definiert:

- Die notwendige Initialisierung.
- Die verpflichtenden Qualitäts-Checks (`check_limits.py`, `validate_reviews.py`).
- Die Regeln für Handover und Decision Records.
- Die Pflicht, `docs/MASTER_PROMPT_STANDARD.md` zu lesen, wenn eine Aufgabe Agenten-Onboarding, Prompt-Verhalten, Autoritätsmodell, Scope-Deklaration, Checks, Review-Routing, Handover-Regeln oder Adapter-Grenzen betrifft.
- Die Pflicht, `docs/ADAPTER_PROMPT_STANDARD.md` und relevante Dateien unter `prompts/adapters/` zu lesen, wenn eine Aufgabe tool-spezifische Adapter-Prompts, CLI-Agenten-Verhalten, Tool-State-Grenzen oder Adapter-Grenzen betrifft.
- Die Pflicht, `docs/SAAS_FOUNDATION_BLUEPRINT.md` zu lesen, wenn eine Aufgabe SaaS-Architektur, Mandanten, Billing, Jobs, Observability, Admin, Data Lifecycle oder Foundation-Standards betrifft.
- Die Pflicht, `docs/AI_FOUNDATION_STANDARD.md` zu lesen, wenn eine Aufgabe KI-Provider, Prompts, Tools, Evaluation, Routing, Fallback, Caching, Safety, AI Cost Tracking, KI-Artefakte oder AI Foundation Standards betrifft.
- Die Pflicht, `docs/RELEASE_RUNBOOK.md` zu lesen, wenn eine Aufgabe Release-Hygiene, Review-Tagging, stable target commits oder release-grade Validation betrifft.

## 19. Quality Gates / Definition of Done

- **Line-Limit**: Quellcodedateien dürfen 300 Zeilen nicht überschreiten (automatisch geprüft durch `scripts/check_limits.py`).
- **Exemptions**: Ausnahmen erfordern ein ACCEPTED ADR mit dem Tag `ADM-Exemption: path/to/file (Max: lines)`.
- **Testing**: Neue Logik muss durch Tests abgedeckt sein.
- **SaaS Foundation**: Produktfeatures dürfen Foundation-Grenzen wie Tenant, Permissions, Billing Readiness, Quotas, Jobs, Observability und Data Lifecycle nicht implizit oder undokumentiert umgehen.
- **AI Foundation**: KI-Features dürfen Provider, Prompts, Tools, Evaluation, Kosten, Routing, Fallback, Caching, Safety, Observability und KI-Artefakt-Lifecycle nicht implizit oder undokumentiert umgehen.
- **Master Prompt**: Agenten dürfen Autoritätsmodell, Scope-Deklaration, Quality-Gate-Evidenz, Review-Scope, Handover-Pflichten oder Adapter-Grenzen nicht implizit umgehen.
- **Adapter Prompt**: Adapter dürfen den kanonischen Master Prompt nicht ersetzen, Tool-State nicht als Wahrheit nutzen und keine ADM-Governance umgehen.
- **Roadmap and Review Validation**: Roadmap-Phasen müssen von Lifecycle-Phasen getrennt bleiben; v1-Readiness-Kriterien dürfen keine deferred oder nicht akzeptierten Mechanismen als umgesetzt behandeln; normale PR-Gates dürfen nicht versehentlich zu release-grade `complete-set`-Gates werden.
- **Release Hygiene**: Reviews müssen auf den stabilen geprüften Commit zeigen; der Release-Tag darf erst nach Merge der Reviews und manueller release-grade Validation auf dem finalen `main`-Commit gesetzt werden.
- **Repository Ruleset Audit**: Governance-relevante Releases brauchen manuelle externe Ruleset-Prüfung; Source-Dateien allein sind kein Beweis.
- **Handover**: Jede signifikante Sitzung endet mit einem strukturierten Handover, das Checks, Risiken, geänderte Dateien, Review-Status, aktive Rolle und nächste Schritte nachvollziehbar dokumentiert.
