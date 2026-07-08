# ADM — SaaS Foundation Standard (v0.19 Draft)

Der SaaS Foundation Standard definiert die Mindestarchitektur für neue SaaS-Produkte, bevor produktbezogene Features gebaut werden.

Er ist der kanonische **Roadmap-Phase-2-Standard**. Diese Roadmap-Phase ist nicht identisch mit **Lifecycle Phase 2 — Architecture Competition** aus `spec/ADM_v1_DRAFT.md`.

Ziel ist kein großes Enterprise-System am ersten Tag. Ziel ist eine kleine, klare Foundation, die später nicht gegen Auth, Mandanten, Rechte, Abrechnung, Kostenkontrolle, Jobs oder Observability umgebaut werden muss.

## Architektur-Philosophie

ADM startet mit einem Modular Monolith.

Das System bleibt zunächst in einem Repository und einem deploybaren System, aber Fachbereiche und Infrastruktur werden sauber getrennt. Eine Auslagerung in Services erfolgt erst, wenn reale Last, Teamgrenzen oder Betriebsanforderungen das rechtfertigen.

Pflichtprinzipien:

1. Domänen klar schneiden, aber Deployment einfach halten.
2. Provider-Adapter vorbereiten, aber keinen Anbieter erzwingen.
3. Tenant-, Kosten- und Audit-Grenzen von Anfang an sichtbar machen.
4. Langläufer aus dem Request-Pfad herauslösen.
5. Lokale Entwicklung reproduzierbar halten.

## 1. Kernbegriffe

| Begriff | Bedeutung |
| --- | --- |
| `user` | Eine reale Person oder technische Identität, die sich authentifiziert. |
| `organization` | Rechtliche oder kaufmännische Einheit, die Verträge, Abrechnung oder Besitz repräsentiert. |
| `tenant` | Isolationsgrenze für Daten, Konfiguration, Limits und Audit. |
| `workspace` | Arbeitsbereich innerhalb eines Tenants oder einer Organisation. |
| `member` | Verbindung zwischen User und Organization, Tenant oder Workspace. |
| `role` | Benannte Verantwortung wie owner, admin, member, viewer oder support. |
| `permission` | Konkrete erlaubte Aktion, zum Beispiel `workspace.read` oder `billing.manage`. |
| `entitlement` | Produkt- oder Plan-bedingte Berechtigung, ein Feature zu nutzen. |
| `quota` | Messbare Nutzungsgrenze, zum Beispiel Jobs, Exporte, Speicher oder KI-Aufrufe. |

ADM-konforme SaaS-Systeme müssen diese Begriffe nicht identisch benennen, aber ihre Entsprechungen müssen dokumentiert und konsistent verwendet werden.

## 2. Minimaler Foundation-Scope

Ein SaaS-Foundation-Entwurf muss mindestens folgende Bereiche erklären:

- Identity und User-Modell.
- Organization-, Tenant- oder Workspace-Modell.
- Memberships, Rollen und Berechtigungen.
- Billing Readiness ohne Provider-Lock-in.
- Entitlements und Quotas.
- Usage Tracking und Kostenaggregation.
- Jobs, Worker und Queue-Verhalten.
- Observability, Audit Logs und Admin-Diagnose.
- Data Lifecycle für Uploads, Exporte, Logs, KI-Artefakte und temporäre Dateien.
- Lokale Developer Experience und Teststrategie.

## 3. Multi-Tenancy und Isolation

Tenant-Grenzen müssen im Datenmodell, in Queries, Jobs, Storage-Pfaden und Logs sichtbar sein.

Vorbereiten:

- Tenant-ID oder gleichwertige Isolationskennung in relevanten Datenmodellen.
- Tenant-spezifische Limits, Konfiguration und Feature-Schalter.
- Tenant-bezogene Audit-Logs.
- Tenant-sichere Storage-Pfade oder Buckets, wenn Dateien gespeichert werden.
- Explizite Regeln für Cross-Tenant-Admin-Zugriffe.
- Tests oder Review-Checks gegen Tenant Escape.

Ein System darf mit nur einem Tenant starten, wenn der Codepfad trotzdem nicht auf globale Annahmen festgenagelt wird.

## 4. Organizations, Workspaces und Memberships

ADM erzwingt kein einziges SaaS-Modell. Der Entwurf muss aber entscheiden, welche Ebene Besitz, Abrechnung und Zusammenarbeit trägt.

Zulässige Grundmodelle:

| Modell | Einsatz |
| --- | --- |
| User-only | Sehr kleine Tools ohne Teamfunktion. Muss später sauber erweiterbar bleiben. |
| Organization-first | B2B-SaaS mit Vertrag, Abrechnung und Teamverwaltung. |
| Workspace-first | Produktivitätstools mit mehreren Arbeitsbereichen pro Organisation. |
| Tenant-first | Systeme, bei denen Isolation wichtiger ist als kaufmännische Struktur. |

Die Entscheidung muss dokumentieren:

- Wer besitzt Daten?
- Wer verwaltet Mitglieder?
- Wo hängen Billing, Quotas und Audit?
- Wie werden Einladungen, Deaktivierung und Besitzwechsel behandelt?

## 5. Rollen und Berechtigungen

ADM empfiehlt ein einfaches RBAC-Modell mit klaren Permissions.

Mindestrollen:

- `owner`: Besitz, Abrechnung, kritische Administration.
- `admin`: Verwaltung ohne vollständigen Besitz.
- `member`: normale produktive Nutzung.
- `viewer`: lesender Zugriff.
- `support`: eng begrenzter interner Diagnosezugriff, wenn benötigt.

Regeln:

1. UI-Sichtbarkeit ersetzt keine serverseitige Autorisierung.
2. Kritische Aktionen brauchen explizite Permissions.
3. Support-Zugriffe müssen auditierbar und begrenzt sein.
4. Rollen dürfen Entitlements nicht ersetzen. Rolle heißt: darf. Entitlement heißt: Produktplan erlaubt es.

## 6. Billing Readiness

Die Foundation muss Abrechnung vorbereiten, ohne einen Zahlungsanbieter fest einzubauen.

Vorbereiten:

- Plan-Modell: Free, Starter, Pro, Enterprise oder projektspezifische Entsprechung.
- Subscription-Zustände: trial, active, past_due, canceled, paused.
- Upgrade, Downgrade, Kündigung und Reaktivierung.
- Provider-Adapter für spätere Integration.
- Billing-relevante Audit-Ereignisse.
- Entitlements, die aus Plan und Sonderfreigaben berechnet werden.

Nicht erforderlich in der Foundation:

- echter Zahlungsanbieter,
- echte Rechnungsstellung,
- Steuerlogik,
- komplexe Revenue-Recognition.

## 7. Entitlements, Quotas und Usage

Features und Nutzung müssen steuerbar sein.

Typische Entitlements:

- Teamgröße.
- Projekt- oder Workspace-Anzahl.
- Export- oder Importfunktionen.
- KI-Funktionen.
- API-Zugriff.
- Admin- oder Audit-Funktionen.

Typische Quotas:

- API-Requests.
- Jobs.
- Worker-Laufzeit.
- Speicher.
- Exporte.
- KI-Tokens oder KI-Aufrufe.
- externe Provider-Kosten.

Usage Tracking muss Kosten pro User, Workspace, Tenant, Feature, Request, Worker-Zeit und KI-Aufruf aggregieren können.

Usage Tracking ohne Kostenmodell reicht nicht aus.

## 8. Jobs, Queues und Worker

Langlaufende oder fehleranfällige Aufgaben gehören nicht in den Webserver-Request-Pfad.

Worker übernehmen zum Beispiel:

- PDF-Erzeugung.
- Bildgenerierung.
- Datenimporte.
- KI-Analysen.
- E-Mail-Versand.
- Webhook-Verarbeitung.
- Batch-Exporte.

Mindestanforderungen:

- Idempotenzschlüssel.
- Retries mit Backoff.
- Timeouts.
- Dead-Letter-Queue oder dokumentierte Fehlerablage.
- Job-Status für Nutzer oder Admin.
- Tenant-, User- und Correlation-Kontext.
- Kosten- und Laufzeitmessung.

## 9. Observability, Audit und Admin

Jede SaaS-Foundation braucht Diagnosefähigkeit, bevor echte Kundenlast entsteht.

Mindeststandard:

- strukturierte Logs,
- Request IDs,
- Correlation IDs,
- Metrics,
- Fehlerklassifikation,
- Audit Logs für sicherheits- und billingrelevante Aktionen,
- Admin-Diagnose für Tenants, Jobs, Quotas, Usage und Integrationen.

Logs dürfen keine Secrets, Tokens, privaten URLs, unnötigen personenbezogenen Daten oder rohen KI-Prompts enthalten.

## 10. Security und Abuse Controls

SaaS-Foundation-Sicherheit umfasst mehr als Login.

Mindestprüfung:

- Tenant Escape.
- Broken Access Control.
- unsichere Einladungen.
- unsichere Admin- oder Support-Zugriffe.
- API-Missbrauch.
- Quota-Umgehung.
- Webhook-Fälschung.
- unklare Lösch- und Exportrechte.
- sensible Daten in Logs oder Jobs.

KI-spezifische Risiken werden in Roadmap Phase 3 durch `docs/AI_FOUNDATION_STANDARD.md` vertieft. Roadmap Phase 2 muss sicherstellen, dass Kosten-, Tenant-, Permission-, Job- und Daten-Grenzen für spätere KI-Funktionen anschlussfähig sind.

## 11. Data Lifecycle

Jede relevante Datenklasse braucht einen definierten Lebenszyklus:

1. Upload oder Import.
2. Verarbeitung.
3. Speicherung.
4. Export.
5. Archivierung.
6. Löschung.
7. Backup.
8. Restore.

Der Lifecycle gilt besonders für Uploads, Exporte, Logs, KI-Artefakte, temporäre Dateien, Caches und Worker-Zwischenstände.

Ziel: keine Datenmüllhalden, keine ungeplanten Speicherkosten, keine unklare Löschlogik.

## 12. Developer Experience

ADM priorisiert schnelle lokale Produktivität.

Mindeststandard:

- One Command Setup oder dokumentierter lokaler Startpfad.
- lokale Mocks für externe Provider.
- Fake Billing.
- Fake AI, wenn KI-Funktionen später erwartet werden.
- Seed-Daten.
- lokale Queue oder Queue-Ersatz.
- lokale Storage-Option.
- schnelle Tests.

## 13. Testing Strategy

Eine SaaS-Foundation braucht Tests für die Grenzen, die später teuer zu reparieren wären.

Pflichtbereiche:

- Unit-Tests für Berechtigungs- und Entitlement-Logik.
- Integrationstests für Tenant- und Workspace-Kontext.
- Contract-Tests für Provider-Adapter, wenn Adapter existieren.
- Job-Tests für Idempotenz, Retry und Fehlerzustände.
- E2E-Smoke-Tests für kritische Nutzerflüsse.
- Regressionstests für bekannte Sicherheits- oder Kostenrisiken.

Optional folgen Performance-, Security-, Mutation- und Chaos-Tests.

## 14. Performance Budgets

Default-Grenzwerte verhindern unkontrolliertes Latenzwachstum. Abweichungen sind erlaubt, müssen aber in einem Decision Record begründet werden.

- Standard-API-Requests: unter 150 ms.
- Frontend-Ladezeit: unter 2 s.
- Cold Starts: unter 500 ms.
- Worker-Jobs: maximal 5 Minuten pro Ausführung, wenn kein längeres Budget dokumentiert ist.
- KI- oder Drittanbieter-Requests: eigenes Budget, typischerweise 1500 ms bis 5000 ms.
- Interaktive Langläufer brauchen Streaming, Polling oder Fortschrittsanzeige.

## 15. Roadmap-Phase-2-Grenze

Roadmap Phase 2 definiert die SaaS-Foundation. Sie implementiert keine konkrete Produktlogik und erzwingt keinen Anbieter.

Nicht Teil von Roadmap Phase 2:

- tiefe AI Provider Architecture,
- Prompt Registry,
- Evaluation Framework,
- Modellrouting,
- echte Payment-Provider-Integration,
- produktindividuelle Feature-Implementierung,
- Microservice-Zerlegung ohne belegten Bedarf.

AI Provider Architecture, Prompt Registry, Evaluation Framework, Modellrouting, Fallback, Caching und Safety Rules sind durch Roadmap Phase 3 in `docs/AI_FOUNDATION_STANDARD.md` definiert. Sie bauen auf den SaaS-Grenzen auf und ersetzen sie nicht.

## 16. Final Audit

Vor einer Foundation-Freigabe wird objektiv geprüft: Architektur, Tenant-Isolation, Berechtigungen, Sicherheit, Performance, Kosten, Jobs und Worker, Observability, Data Lifecycle, Testabdeckung, Dokumentation und technische Schulden.
