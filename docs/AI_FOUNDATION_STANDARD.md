# ADM — AI Foundation Standard (v0.20 Draft)

Der AI Foundation Standard definiert die Mindestarchitektur für KI-Funktionen, bevor produktbezogene KI-Features, Provider-Integrationen oder Tool-Ausführungen gebaut werden.

Er ist der kanonische **Roadmap-Phase-3-Standard**. Diese Roadmap-Phase ist nicht identisch mit den ADM Lifecycle-Phasen aus `spec/ADM_v1_DRAFT.md`.

Ziel ist kein KI-Runtime-Framework. Ziel ist eine kleine, klare Foundation, die spätere KI-Nutzung kontrollierbar, messbar, austauschbar, sicher und bezahlbar macht.

## Architektur-Philosophie

ADM behandelt KI als kontrollierte Systemgrenze, nicht als frei eingebetteten Helfer im Produktcode.

Pflichtprinzipien:

1. Provider austauschbar halten, aber keinen Anbieter integrieren.
2. Prompts versionieren, aber keine Produktprompts erzwingen.
3. Tools registrieren, aber keine Tool-Ausführung implementieren.
4. Evaluation und Kosten sichtbar machen, bevor KI produktkritisch wird.
5. Routing, Fallback und Caching bewusst entscheiden, nicht implizit im Code verstecken.
6. Safety-Regeln an Daten-, Tenant-, Tool- und Kosten-Grenzen binden.

## 1. Kernbegriffe

| Begriff | Bedeutung |
| --- | --- |
| `ai_provider` | Austauschbarer Anbieter oder lokales Modellziel für KI-Aufrufe. |
| `model_capability` | Fähigkeit eines Modells, zum Beispiel Text, Bild, Audio, Embedding, Tool-Use oder strukturierte Ausgabe. |
| `prompt_registry` | Versionierte Sammlung erlaubter Prompt-Artefakte und ihrer Metadaten. |
| `prompt_version` | Stabile Version eines Prompts mit Zweck, Inputs, Outputs und Safety-Erwartung. |
| `tool_registry` | Versionierte Sammlung erlaubter Tools, Scopes, Risiken und Ausführungsgrenzen. |
| `evaluation` | Messung von Qualität, Sicherheit, Kosten und Regressionen für KI-Verhalten. |
| `routing_policy` | Regel, welcher Provider, welches Modell oder welcher Fallback für einen Task genutzt werden darf. |
| `fallback_policy` | Verhalten bei Fehlern, Kostenlimits, Timeouts, Provider-Ausfall oder Qualitätsproblemen. |
| `ai_cache` | Bewusst begrenzter Cache für KI-Ergebnisse, Embeddings oder Zwischenartefakte. |
| `safety_rule` | Explizite Regel, die KI-Nutzung, Datenzugriff, Tool-Nutzung oder Ausgabe begrenzt. |

ADM-konforme Systeme müssen diese Begriffe nicht exakt benennen, aber ihre Entsprechungen müssen dokumentiert und konsistent verwendet werden.

## 2. Minimaler Foundation-Scope

Ein AI-Foundation-Entwurf muss mindestens folgende Bereiche erklären:

- Provider-Abstraktion und Modellfähigkeiten.
- Prompt Registry und Prompt-Versionierung.
- Tool Registry und Tool-Ausführungsgrenzen.
- Evaluation, Testdaten und Regressionserkennung.
- AI Cost Tracking und Budgetgrenzen.
- Routing, Fallback und Degradation.
- Caching, Wiederverwendung und Invalidierung.
- Safety-Regeln für Daten, Tenant, User, Tools und Ausgaben.
- Observability, Audit und Diagnose für KI-Aufrufe.
- Data Lifecycle für Prompts, Antworten, Embeddings, Evaluationsdaten und KI-Artefakte.

## 3. Provider Abstraction

Provider müssen hinter einem neutralen Vertrag stehen.

Der Standard verlangt keine konkrete Integration, aber ein Entwurf muss erklären:

- Welche Fähigkeiten benötigt werden: Text, strukturierte Ausgabe, Embeddings, Bild, Audio, Tool-Use oder Batch.
- Welche Provider- oder Modellentscheidung später austauschbar bleiben muss.
- Welche Inputs und Outputs normalisiert werden.
- Welche Fehlerklassen, Timeouts und Rate Limits erwartet werden.
- Welche Kosten- und Latenzmetadaten pro Aufruf erfasst werden.
- Welche Provider-spezifischen Features nicht in Produktlogik leaken dürfen.

Nicht erlaubt im Foundation-Standard:

- Anbieterbindung ohne ADR.
- Secrets oder API Keys in Dokumentation, Tests oder Logs.
- Produktlogik, die direkt auf einen Provider-SDK-Vertrag angewiesen ist.

## 4. Prompt Registry

Prompts sind versionierte Architekturartefakte, nicht lose Strings.

Eine Prompt Registry muss mindestens beschreiben:

- Prompt-ID und Version.
- Zweck und erlaubte Einsatzbereiche.
- erwartete Inputs und Outputs.
- Owner oder verantwortliche Rolle.
- Safety-Annahmen und verbotene Datenklassen.
- Evaluationsstatus und bekannte Risiken.
- Änderungsregeln für produktkritische Prompts.

Prompts dürfen später in Dateien, Datenbanken oder Konfiguration liegen. v0.20 erzwingt keine konkrete Ablageform.

## 5. Tool Registry

Tools erweitern die Wirkung eines Modells und brauchen stärkere Grenzen als normale Prompts.

Eine Tool Registry muss mindestens beschreiben:

- Tool-ID und Zweck.
- erlaubte Eingaben und Ausgaben.
- erforderliche User-, Tenant- oder System-Permissions.
- Side-Effect-Klasse: read-only, write, external call, billing-relevant oder destructive.
- Rate Limits, Timeouts und Retry-Regeln.
- Audit-Anforderungen.
- Human-Approval-Punkte für riskante Aktionen.

Kein Modell darf implizit beliebige Funktionen, Shell-Befehle, Provider-APIs oder externe Systeme auslösen.

## 6. Evaluation

Evaluation verhindert, dass KI-Verhalten nur nach Gefühl bewertet wird.

Mindeststandard:

- Golden Cases für kritische Prompts oder Tools.
- Negative Cases für unerlaubte Daten, unsichere Tool-Nutzung und falsche Tenant-Kontexte.
- Qualitätskriterien für Richtigkeit, Format, Vollständigkeit und Ablehnung.
- Kosten- und Latenzmessung pro Fall.
- Regressionserkennung bei Prompt-, Modell-, Provider- oder Routing-Änderungen.
- Dokumentierte Toleranzen für nicht-deterministisches Verhalten.

Evaluation ist kein Ersatz für Security Review. Sie ist ein Frühwarnsystem.

## 7. AI Cost Tracking

KI-Kosten müssen einer verantwortlichen Grenze zugeordnet werden können.

Ein Entwurf muss Kosten mindestens aggregierbar machen nach:

- User.
- Organization, Tenant oder Workspace.
- Feature.
- Prompt-ID und Prompt-Version.
- Tool-ID.
- Provider oder Modellklasse.
- Request, Job oder Worker-Ausführung.
- Cache Hit oder Cache Miss.

KI-Aufrufe ohne Kostenmodell sind nicht ADM-konform, sobald sie produktiv, wiederholbar oder kundenbezogen sind.

## 8. Routing und Fallback

Routing entscheidet, welches Modell oder welcher Provider einen Task bearbeiten darf.

Mindestentscheidungen:

- Welche Aufgaben brauchen hohe Qualität, niedrige Kosten, niedrige Latenz oder lokale Ausführung?
- Welche Aufgaben dürfen Fallbacks nutzen?
- Wann wird degraded statt erneut versucht?
- Wann muss ein Nutzer informiert werden?
- Wann wird ein Job abgebrochen?
- Wann ist Human Review nötig?

Fallbacks dürfen keine Safety-Regeln umgehen. Ein billigeres oder schnelleres Modell darf nicht automatisch mehr Daten oder stärkere Tools bekommen.

## 9. Caching

Caching kann Kosten senken, erzeugt aber Datenschutz-, Tenant- und Korrektheitsrisiken.

Ein AI Cache muss entscheiden:

- Welche Datenklassen überhaupt cachebar sind.
- Ob Cache Keys Tenant-, User-, Permission- und Prompt-Version-Kontext enthalten müssen.
- Wie lange Einträge leben.
- Wann Einträge invalidiert werden.
- Ob Rohprompts, Antworten, Embeddings oder strukturierte Artefakte gespeichert werden.
- Wie Löschung, Export und Audit mit Cache-Einträgen umgehen.

Caching ohne Data-Lifecycle-Regel ist nicht zulässig.

## 10. Safety Rules

Safety-Regeln begrenzen KI-Nutzung vor, während und nach dem Aufruf.

Mindestprüfungen:

- erlaubte Datenklassen pro Prompt oder Tool.
- Tenant- und Permission-Kontext vor Tool-Nutzung.
- Schutz vor Prompt Injection bei externen oder nutzergelieferten Inhalten.
- Schutz vor unsicheren Tool-Parametern.
- Regeln für PII, Secrets, private URLs und interne Systemdaten.
- Regeln für Logging, Caching und Evaluation mit sensiblen Daten.
- Regeln für menschliche Freigabe bei riskanten Aktionen.

Safety muss als Architekturgrenze dokumentiert sein, nicht nur als Prompt-Hinweis.

## 11. Observability, Audit und Admin

KI-Aufrufe brauchen Diagnosefähigkeit ohne Datenleck.

Mindeststandard:

- Request ID und Correlation ID.
- Provider-, Modell-, Prompt- und Tool-Metadaten.
- Kosten-, Token-, Latenz- und Cache-Metriken.
- Fehlerklassifikation und Fallback-Grund.
- Audit Logs für tool-, billing-, tenant- oder sicherheitsrelevante Aktionen.
- Admin-Diagnose ohne Rohprompt-Leak.

Logs dürfen keine Secrets, Tokens, private URLs, unnötige personenbezogene Daten oder unredigierte Rohprompts enthalten.

## 12. Data Lifecycle für KI-Artefakte

Jede KI-Datenklasse braucht einen Lebenszyklus:

1. Erzeugung oder Import.
2. Verarbeitung.
3. Speicherung oder Nicht-Speicherung.
4. Nutzung für Evaluation oder Caching.
5. Export.
6. Archivierung.
7. Löschung.
8. Backup und Restore, falls gespeichert.

Der Lifecycle gilt besonders für Prompts, Antworten, Tool-Inputs, Tool-Outputs, Embeddings, Evaluationsdaten, Cache-Einträge, Moderationsartefakte und Worker-Zwischenstände.

## 13. Boundary zum SaaS Foundation Standard

Roadmap Phase 2 definiert die SaaS-Grenzen: User, Organization, Tenant, Workspace, Membership, Permissions, Billing Readiness, Quotas, Jobs, Observability und Data Lifecycle.

Roadmap Phase 3 nutzt diese Grenzen und ergänzt KI-spezifische Architekturregeln.

Ein AI-Foundation-Entwurf darf SaaS-Grenzen nicht neu erfinden oder umgehen. KI-Kosten, KI-Jobs, KI-Artefakte, KI-Logs und KI-Tools müssen an User-, Tenant-, Permission-, Quota-, Billing- und Data-Lifecycle-Entscheidungen anschließen.

## 14. Roadmap-Phase-3-Grenze

Roadmap Phase 3 definiert die AI Foundation. Sie implementiert keine konkrete KI-Funktion und erzwingt keinen Anbieter.

Nicht Teil von Roadmap Phase 3:

- Runtime-Code,
- Provider-SDK-Integration,
- echte Modellaufrufe,
- echte Tool-Ausführung,
- echte Prompt-Datenbank,
- produktspezifische KI-Features,
- neue Validator- oder Workflow-Erzwingung ohne gesondertes GO,
- automatische Modellranglisten oder Provider-Empfehlungen.

Diese Themen folgen in späteren Roadmap-Phasen, produktbezogenen ADRs oder explizit freigegebenen Implementierungs-PRs.

## 15. Final Audit

Vor einer AI-Foundation-Freigabe wird objektiv geprüft: Provider-Neutralität, Prompt- und Tool-Governance, Evaluation, Kosten, Routing, Fallback, Caching, Safety, Tenant-Anbindung, Observability, Data Lifecycle, Dokumentation und technische Schulden.
