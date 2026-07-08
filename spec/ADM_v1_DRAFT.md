# ADM — Spezifikation (v0.31 Draft)

Das Agentic Development Manifest (ADM) ist ein modellneutraler, dateibasierter Standard für die Softwareentwicklung mit KI-Agenten. Dieses Dokument dient als kanonische Spezifikation des Regelwerks.

## 1. Status / Version

- **Version**: v0.31 Draft
- **Zustand**: Foundation Hygiene Cleanup Accepted
- **Letztes Update**: 2026-07-08

## 2. ADM Prinzipien

ADM basiert auf drei Grundpfeilern, die eine langfristige Wartbarkeit und Modellunabhängigkeit garantieren:

1. **Modell-Neutralität**: Der Standard setzt keine spezifischen LLM-Provider oder proprietären Features voraus. Alle Logik ist lokal ausführbar oder klar als extern markiert.
2. **CLI-First**: Die Interaktion und Validierung erfolgt primär über Terminal-Tools. Das Repository ist für Agenten ohne grafische Oberfläche optimiert.
3. **Repository-Backed Truth**: Das Repository ist die einzige Quelle der Wahrheit. Projektgedächtnis, Entscheidungen, Rollen, Reviews, Review Archive Policy, Review Archive Migration, Handovers, Session Continuity, Tool Verification, SaaS Foundation Standards, AI Foundation Standards, Master Prompt Standards, Adapter Prompt Standards, Roadmap Continuation, v1-Readiness-Kriterien, Review and Validation Hardening, Foundation Consistency and Release Hygiene sowie Foundation Hygiene Cleanup müssen als Dateien versioniert oder bewusst als lokal/transient ausgeschlossen sein.

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
- Ausgefüllte aktive Berichte liegen unter `.ai/reviews/`; archivierte historische Review-Sets dürfen später unter `.ai/reviews/archive/<review_set_id>/` liegen.
- Dateinamen müssen der `review_id` entsprechen, zum Beispiel `REV-ARCH-YYYYMMDD-slug.md`.

## 6. Review-Validierungsmodi

Der Validator `scripts/validate_reviews.py` unterstützt drei Modi:

| Modus | Beschreibung | Einsatzbereich |
| --- | --- | --- |
| `advisory` | Meldet Fehler, blockiert aber nicht. | Feature-Branches, frühe Entwicklung. |
| `existing-strict` | Prüft vorhandene Reviews strikt auf Struktur. | Pull Requests, normale Pushes. |
| `complete-set` | Erzwingt alle 6 Rollen, PASSED-Status und Scope-Bindung. | Releases, Phasenübergänge. |

v0.24 akzeptiert diese drei Modi als Review and Validation Hardening Baseline. Normale PRs dürfen dadurch nicht versehentlich complete-set-pflichtig werden. v0.26 akzeptiert, dass der Standardpfad direkte `.ai/reviews/*.md` Dateien prüft und `.ai/reviews/archive/**` nicht rekursiv einbezieht. v0.27 migriert abgeschlossene historische Review-Sets bis v0.25 in dieses Archivmodell. v0.30 migriert abgeschlossene v0.26-, v0.27- und v0.28-Review-Sets in dasselbe Archivmodell, ohne Review-Metadaten oder Produktionsvalidatorlogik zu ändern. v0.31 verbessert nur die complete-set Ausgabeklarheit; Validierungssemantik, Rollenpflichten, Scope-Bindung und Archivverhalten bleiben unverändert.

## 7. Release Gate Policy

Ein Release oder Git-Tag ist nur zulässig, wenn ein vollständiges Review-Set vorliegt und release-grade validiert wurde.

- **Release-grade Validation**: Vor dem Tagging muss `complete-set` auf dem finalen `main`-Zustand mit dokumentierter Evidenz grün sein.
- **Evidence Paths**: GitHub manual `workflow_dispatch`, lokale Terminalvalidierung und Ruleset-Audit sind getrennte Evidenzarten und dürfen nicht vermischt werden.
- **Parameter**: `review_set_id`, `target_ref` und `reviewed_commit` beziehungsweise `target_commit` müssen explizit angegeben werden.
- **Stable reviewed commit**: Der `target_commit` in Review-Artefakten ist der stabile nicht-review Commit, der geprüft wurde.
- **Final tag commit**: Der Release-Tag zeigt auf den finalen `main`-Commit nach Merge der Review-Artefakte und erfolgreicher release-grade Validation.
- **Referenz**: Details siehe `docs/RELEASE_RUNBOOK.md`.

## 8. Runtime Artifact Policy (`.ai/`)

Das `.ai/` Verzeichnis dient als persistente Memory Layer für Agenten.

- **Versioniert**: `.ai/reviews/`, `.ai/reviews/archive/`, `.ai/decisions/`, `.ai/handover/`, `.ai/memory/`, `.ai/knowledge/`, `.ai/tasks/`, `.ai/agents/`, `.ai/README.md`.
- **Ignoriert oder lokal behandelt**: `.ai/tmp/`, `.ai/logs/`, `.ai/cache/`, `.ai/scratch/`, `.ai/local/`, `.ai/sessions/`.
- **Regel**: Keine temporären Chat-Marker, Rohlogs, Secrets, privaten lokalen Pfade oder flüchtigen Notizen im Repository.

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

v0.28 implementiert keinen Handover-Linter und keine Handover-Automation-Erweiterung.

## 12. Session Continuity Baseline

Session Continuity ist der kanonische Roadmap-Phase-7-Block für zuverlässige Sitzungsfortsetzung durch zukünftige Agenten.

Ziel ist, dass ein neuer Agent Projektzustand aus repository-owned evidence ableitet, bevor er Chatverlauf, hidden model memory, lokale Profile oder Tool-Caches als nicht-autoritative Zusatzinformation betrachtet.

Pflichtbereiche:

| Bereich | Mindestentscheidung |
| --- | --- |
| Handover discovery | Neueste relevante Übergabe aus `.ai/handover/` nach Timestamp und Dateiname bestimmen |
| Continuity status | `READY`, `PARTIAL`, `BLOCKED` oder `UNKNOWN` ohne Freigabe-Semantik verwenden |
| Evidence boundary | Git, kanonische Docs, Reviews, Handovers, Tasks, Memory, Decisions und Agent Registry vor Chat/Memory |
| Ambiguity handling | Fehlende, widersprüchliche oder stale Evidenz als `UNKNOWN` oder `AMBIGUOUS` berichten |
| Check truth | Nicht ausgeführte Checks bleiben `NOT RUN`; unklare Ergebnisse bleiben `UNKNOWN` |
| Review state | `review_set_id`, `target_ref`, `target_commit`, Review-Votes und CI-readiness nicht erfinden |
| Routing | Registry-Rollen nur verwenden, wenn sie existieren; fehlende Rollen als offene Frage dokumentieren |
| Non-goals | Kein Linter, keine Runtime, kein Workflow, keine neue Validator-Semantik, keine Release-Automation |

Die kanonische Handover-Discovery-Policy liegt in `.ai/handover/README.md`.

v0.28 akzeptiert Session Continuity als Dokumentations- und Verhaltensbaseline. Es implementiert keine Automatisierung.

## 13. SaaS Foundation Standard

Der SaaS Foundation Standard ist der kanonische **Roadmap-Phase-2-Block** für neue SaaS-Systeme. Das ist bewusst von **Lifecycle Phase 2 — Architecture Competition** aus Abschnitt 3 getrennt.

Ziel ist eine kleine, explizite Foundation vor Produktfeatures. ADM erzwingt keinen bestimmten Anbieter und keine Microservice-Architektur. Der Default ist Modular Monolith First.

Pflichtbereiche: Identity, Organization, Tenant, Workspace, Membership, Roles and Permissions, Billing Readiness, Entitlements and Quotas, Usage and Cost, Jobs and Workers, Observability and Admin, Data Lifecycle sowie DX and Testing.

Roadmap Phase 2 implementiert keine konkrete Produktlogik, keine echte Payment-Integration, keine AI Provider Architecture, kein Modellrouting und keine Prompt Registry.

## 14. AI Foundation Standard

Der AI Foundation Standard ist der kanonische **Roadmap-Phase-3-Block** für KI-Funktionen. Das ist bewusst von **Lifecycle Phase 3 — Devil's Advocate** aus Abschnitt 3 getrennt.

Ziel ist eine kleine, explizite KI-Foundation vor produktbezogenen KI-Features. ADM erzwingt keinen LLM-Provider, kein Runtime-Framework, keine Prompt-Datenbank und keine Tool-Ausführungsengine.

Pflichtbereiche: Provider Abstraction, Prompt Registry, Tool Registry, Evaluation, AI Cost Tracking, Routing, Fallback, Caching, Safety Rules, Observability and Audit sowie AI Artifact Lifecycle.

Roadmap Phase 3 implementiert keine konkrete KI-Funktion, keine Provider-SDK-Integration, keine echten Modellaufrufe, keine echte Tool-Ausführung, keine Prompt-Datenbank, keine neue Validator- oder Workflow-Erzwingung und keine Provider-Secrets.

## 15. Master Prompt Standard

Der Master Prompt Standard ist der kanonische **Roadmap-Phase-4-Block** für CLI-Agenten-Onboarding. Das ist bewusst von **Lifecycle Phase 4 — Simplification** aus Abschnitt 3 getrennt.

Ziel ist eine modellneutrale Startanweisung, die ADM-Regeln in operative Agentenschritte übersetzt. Der Master Prompt ist kein Tool-Adapter, keine Runtime-Engine, kein Validator und keine Freigabeinstanz.

Pflichtbereiche: Authority Order, Required Initialization, Scope Declaration, Operating Rules, Decision Rules, Quality Gate Contract, Review Contract, Release Hygiene Contract, Foundation Triggers, Handover Contract, Session Continuity Contract und Adapter Boundary.

Roadmap Phase 4 implementiert keine Runtime, keine Provider- oder Tool-Integration, keine CLI-spezifischen Adapter-Prompts, keine lokalen Tool-Profile, keine MCP-Integration, keine Schemas, keine Validatoren und keine Workflow-Änderungen ohne gesondertes GO.

## 16. Adapter Prompt Standard

Der Adapter Prompt Standard ist der kanonische **Roadmap-Phase-5-Block** für tool-spezifische CLI-Agenten-Prompts. Das ist bewusst von **Lifecycle Phase 5 — Roadmap & Plan** aus Abschnitt 3 getrennt.

Ziel ist eine dünne Adapter-Schicht unterhalb des kanonischen Master Prompts. Adapter Prompts helfen konkreten CLI-Tools beim Arbeiten, ersetzen aber weder die ADM-Spezifikation noch `prompts/master_prompt.md`.

Initial akzeptierte Adapter sind Claude Code CLI, Codex CLI und Generic CLI Agent. Gemini CLI und Antigravity CLI bleiben deferred candidates bis zu späterer expliziter Freigabe.

Roadmap Phase 5 implementiert keine Runtime, keine Provider-SDKs, keine echte Tool-Integration, keine lokalen Tool-Profile, keine MCP-Integration, keine Schemas, keine Validatoren, keine Workflows, keine Release-Automation und keine Provider-Secrets.

## 17. Tool Verification Discovery Baseline

Tool Verification ist der kanonische **Roadmap-Phase-8-Discovery- und Governance-Block** für deferred oder future CLI-Tool-Adapter.

Ziel ist nicht Adapter-Implementierung, sondern die vorgelagerte Prüfung, ob ein konkretes Tool aktuelles, reviewbares Verhalten zeigt, das einen dünnen Adapter unterhalb von `prompts/master_prompt.md` rechtfertigt.

Pflichtbereiche: Tool identity, Instruction model, Repository access, Planning behavior, Edit behavior, Command behavior, Review behavior, Tool state boundary, Governance risks und Generic fallback.

Gemini CLI und Antigravity CLI bleiben deferred candidates. Sie dürfen nicht als akzeptierte Adapter gelten, bevor aktuelles Tool-Verhalten dokumentiert, reviewed und explizit in einem späteren Adapter-PR freigegeben wurde.

Roadmap Phase 8 v0.29 implementiert keine neuen Adapter, keine Runtime, keine Provider-SDKs, keine MCP-Integration, keine lokalen Tool-Profile, keine Validatoren, keine Workflows, keine Release-Automation und keine v1-Release-Candidate-Semantik.

Die kanonische Policy liegt in `docs/TOOL_VERIFICATION.md`.

## 18. Roadmap Continuation, Review Hardening, and Foundation Hygiene

Roadmap Continuation ist der kanonische v0.23-Planungsblock nach Roadmap Phase 5. Er definiert Roadmap Phase 6 bis Roadmap Phase 9 und v1-Readiness-Kriterien, ohne die späteren Mechanismen zu implementieren.

Review and Validation Hardening Baseline ist der kanonische v0.24-Roadmap-Phase-6-Block. Er akzeptiert die bestehenden Review-Validation-Modi und Review-Set-Scoping-Semantik, korrigiert ADR-Status-Drift und ergänzt gezielte Scope-Regressionstests.

Foundation Consistency and Release Hygiene Baseline ist der kanonische v0.25-Konsolidierungsblock. Er synchronisiert Status- und Versionssprache, modernisiert Release-Hygiene, präzisiert manuelle Ruleset-Audits und hält Roadmap Phase 7 bewusst offen.

Review Archive Policy ist der kanonische v0.26-Archivierungsregelblock. Er definiert `.ai/reviews/archive/<review_set_id>/` als spätere historische Review-Ablage, ohne alte Reviews zu verschieben oder Produktionsvalidatorlogik zu ändern.

Review Archive Migration Batch 1 ist der kanonische v0.27-Archivierungsmigrationsblock. Er verschiebt abgeschlossene historische Review-Sets bis v0.25 nach `.ai/reviews/archive/<review_set_id>/`, ohne Review-Metadaten umzuschreiben.

Session Continuity Baseline ist der kanonische v0.28-Roadmap-Phase-7-Block. Er definiert repository-owned Sitzungsfortsetzung, Handover-Discovery, Continuity-Status, Ambiguitätsbehandlung und Evidenzgrenzen ohne Linter, Workflow, Runtime oder neue Validator-Semantik.

Tool Verification Discovery Baseline ist der kanonische v0.29-Roadmap-Phase-8-Block. Er definiert Tool-Verifikationskriterien vor deferred oder future Adapter-PRs, ohne Gemini CLI, Antigravity CLI oder andere neue Adapter zu akzeptieren.

Review Archive Migration Batch 2 ist der kanonische v0.30-Archivierungsmigrationsblock. Er verschiebt abgeschlossene Review-Sets von v0.26 bis v0.28 nach `.ai/reviews/archive/<review_set_id>/`, ohne Review-Metadaten umzuschreiben und ohne v0.29 als aktive Release-Evidenz zu archivieren.

Foundation Hygiene Cleanup ist der kanonische v0.31-Pre-Phase-9-Hygieneblock. Er finalisiert stale ADR-Review-Evidenz, schärft Release-Evidence-Semantik, verbessert PR-Validation-Evidence und macht complete-set Validator-Ausgabe klarer, ohne Validierungssemantik oder Workflow-Verhalten zu ändern.

Roadmap Phase 9 ist der kanonische v0.32-Kriterienblock für einen späteren v1 Release Candidate. v0.32 definiert die Kriterien; es deklariert ADM nicht als v1-ready und erzeugt keinen v1- oder v1-RC-Tag.

### v1 Release Candidate Criteria

Ein v1 Release Candidate ist nur zulässig, wenn der konkrete Zielzustand durch folgende Evidenz belegbar ist:

- README, ROADMAP, CHANGELOG, Spezifikation und relevante Governance-Dokumente sind synchron.
- Alle abgeschlossenen Roadmap-Phasen und Governance-Baselines haben akzeptierte ADR-Abdeckung.
- Deferred Adapter wie Gemini CLI und Antigravity CLI gelten nicht als akzeptiert, bevor ihr aktuelles Tool-Verhalten verifiziert und explizit freigegeben wurde.
- Für den v1-RC-Zielzustand existiert ein neues vollständiges sechs Rollen Review-Set.
- Das v1-RC-Review-Set ist mit explizitem `review_set_id`, `target_ref` und `target_commit` an den stabilen geprüften Zustand gebunden.
- Release-grade `complete-set`-Validierung ist vor einem v1-RC-Tag erfolgreich gelaufen.
- Governance-relevante v1-RC-Releases enthalten manuelle GitHub Ruleset-Audit-Evidenz.
- Die direkte aktive `.ai/reviews/`-Zone ist für den v1-RC-Gate nicht mehrdeutig; historische Review-Sets sind entweder archiviert oder ausdrücklich als nicht zum v1-RC-Scope gehörend dokumentiert.

Nicht erforderlich für v1-RC sind Runtime-Code, Provider-SDKs, MCP-Integration, lokale Tool-Profile, Workflow-Änderungen, neue Validator-Modi, Release-Automation, Review Index, zusätzliche Review-Archivmigration, Handover-Linting oder Adapter-Expansion, solange diese nicht durch spätere explizite Roadmap-Phasen und ADRs akzeptiert werden.

v1-Readiness verlangt mindestens synchronisierte Roadmap-Phasen, Spezifikation, README, Changelog, akzeptierte ADRs, vollständige sechs Rollen Review-Evidenz, manuelle Ruleset-Audit-Evidenz für governance-relevante Releases und release-grade `complete-set`-Validierung für den Zielzustand. Deferred Adapter wie Gemini CLI und Antigravity CLI dürfen nicht als akzeptiert gelten, bevor ihr aktuelles Tool-Verhalten verifiziert und explizit freigegeben wurde.

## 19. PR Hygiene Policy

Pull Requests müssen die Selbsterklärung des Agenten widerspiegeln.

- **Inhalt**: PR-Bodies dürfen keine ungelösten Platzhalter, leere Pflichtfelder oder ungeprüfte Checkboxen enthalten.
- **Vorlage**: Die Nutzung von `.github/pull_request_template.md` ist verpflichtend.
- **Qualität**: Ein PR ohne inhaltlich wertvolle Summary und Validierung ist ein Governance-Fehler.
- **Validation Evidence**: PRs müssen lokale Validierung, GitHub Actions PR Gate, manuelle release-grade Workflow-Runs und `NOT RUN`-Gründe klar trennen.

## 20. Agent Onboarding Contract

Jeder Agent muss seine Arbeit mit dem `prompts/master_prompt.md` beginnen. Dieser Prompt definiert:

- Die notwendige Initialisierung.
- Die verpflichtenden Qualitäts-Checks (`check_limits.py`, `validate_reviews.py`).
- Die Regeln für Handover, Session Continuity und Decision Records.
- Die Pflicht, `docs/MASTER_PROMPT_STANDARD.md` zu lesen, wenn eine Aufgabe Agenten-Onboarding, Prompt-Verhalten, Autoritätsmodell, Scope-Deklaration, Checks, Review-Routing, Handover-Regeln, Session-Continuity-Regeln oder Adapter-Grenzen betrifft.
- Die Pflicht, `docs/ADAPTER_PROMPT_STANDARD.md` und relevante Dateien unter `prompts/adapters/` zu lesen, wenn eine Aufgabe tool-spezifische Adapter-Prompts, CLI-Agenten-Verhalten, Tool-State-Grenzen oder Adapter-Grenzen betrifft.
- Die Pflicht, `docs/SAAS_FOUNDATION_BLUEPRINT.md` zu lesen, wenn eine Aufgabe SaaS-Architektur, Mandanten, Billing, Jobs, Observability, Admin, Data Lifecycle oder Foundation-Standards betrifft.
- Die Pflicht, `docs/AI_FOUNDATION_STANDARD.md` zu lesen, wenn eine Aufgabe KI-Provider, Prompts, Tools, Evaluation, Routing, Fallback, Caching, Safety, AI Cost Tracking, KI-Artefakte oder AI Foundation Standards betrifft.
- Die Pflicht, `docs/RELEASE_RUNBOOK.md` zu lesen, wenn eine Aufgabe Release-Hygiene, Review-Tagging, stable target commits oder release-grade Validation betrifft.
- Die Pflicht, `docs/TOOL_VERIFICATION.md` zu lesen, wenn eine Aufgabe deferred Adapter, future Adapter, Tool-Verhalten, CLI-spezifische Fähigkeiten, Tool-State-Grenzen oder Adapter-Eignung betrifft.

## 21. Quality Gates / Definition of Done

- **Line-Limit**: Quellcodedateien dürfen 300 Zeilen nicht überschreiten (automatisch geprüft durch `scripts/check_limits.py`).
- **Exemptions**: Ausnahmen erfordern ein ACCEPTED ADR mit dem Tag `ADM-Exemption: path/to/file (Max: lines)`.
- **Testing**: Neue Logik muss durch Tests abgedeckt sein.
- **SaaS Foundation**: Produktfeatures dürfen Foundation-Grenzen wie Tenant, Permissions, Billing Readiness, Quotas, Jobs, Observability und Data Lifecycle nicht implizit oder undokumentiert umgehen.
- **AI Foundation**: KI-Features dürfen Provider, Prompts, Tools, Evaluation, Kosten, Routing, Fallback, Caching, Safety, Observability und KI-Artefakt-Lifecycle nicht implizit oder undokumentiert umgehen.
- **Master Prompt**: Agenten dürfen Autoritätsmodell, Scope-Deklaration, Quality-Gate-Evidenz, Review-Scope, Handover-Pflichten oder Adapter-Grenzen nicht implizit umgehen.
- **Adapter Prompt**: Adapter dürfen den kanonischen Master Prompt nicht ersetzen, Tool-State nicht als Wahrheit nutzen und keine ADM-Governance umgehen.
- **Tool Verification**: Deferred oder future Adapter dürfen nicht vorgeschlagen, akzeptiert oder als umgesetzt dargestellt werden, bevor aktuelles Tool-Verhalten dokumentiert, reviewed und explizit freigegeben wurde.
- **Session Continuity**: Agenten müssen repository-owned Handover- und Projektzustandsevidenz prüfen, Ambiguität melden und nicht aus Chatverlauf, hidden memory, lokalen Profilen oder Scratch rekonstruieren.
- **Roadmap and Review Validation**: Roadmap-Phasen müssen von Lifecycle-Phasen getrennt bleiben; v1-Readiness-Kriterien dürfen keine deferred oder nicht akzeptierten Mechanismen als umgesetzt behandeln; normale PR-Gates dürfen nicht versehentlich zu release-grade `complete-set`-Gates werden.
- **Review Archive Policy**: Archivierte Review-Sets bleiben historische Evidenz; aktuelle Validatorfehler dürfen nicht durch Archivierung versteckt werden.
- **Release Hygiene**: Reviews müssen auf den stabilen geprüften Commit zeigen; der Release-Tag darf erst nach Merge der Reviews und release-grade Validation auf dem finalen `main`-Commit gesetzt werden; lokale, GitHub-Workflow- und Ruleset-Evidenz müssen eindeutig getrennt dokumentiert werden.
- **Repository Ruleset Audit**: Governance-relevante Releases brauchen manuelle externe Ruleset-Prüfung; Source-Dateien allein sind kein Beweis.
- **Handover**: Jede signifikante Sitzung endet mit einem strukturierten Handover, das Checks, Risiken, geänderte Dateien, Review-Status, aktive Rolle, Continuity Status und nächste Schritte nachvollziehbar dokumentiert.
