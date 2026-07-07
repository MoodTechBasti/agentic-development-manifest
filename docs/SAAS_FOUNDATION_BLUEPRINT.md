# ADM — SaaS Foundation Blueprint (v0.2 Draft)

Der SaaS Foundation Blueprint beschreibt die technologischen Mindestbereiche für ein neues, skalierbares und wartbares SaaS-System.

## Architektur-Philosophie: Modular Monolith First

ADM startet mit einem Modular Monolith. Das System bleibt in einem Repository, aber Fachdomänen und Infrastruktur werden klar getrennt.

Beispiele für Module:

- Users
- Organizations
- Billing
- AI
- Analytics
- Queue
- Notifications
- Admin

Ein Modul wird erst ausgelagert, wenn reale Last, Teamgrenzen oder Betriebsanforderungen das rechtfertigen.

## 1. Multi-Tenancy & Isolation

Tenant-Grenzen müssen von Anfang an sichtbar sein. Datenzugriffe dürfen nicht versehentlich tenantübergreifend funktionieren.

Vorbereiten:

- Tenant-ID in relevanten Datenmodellen
- Tenant-spezifische Limits
- Tenant-Konfiguration
- Tenant-Branding
- getrennte Storage-Pfade oder Buckets, wenn nötig
- Datenbankseitige Isolation, wenn der Stack sie unterstützt

## 2. Entitlements & Quotas

Features und APIs werden über Berechtigungen und Limits gesteuert.

Typische Pläne:

- Free
- Starter
- Pro
- Enterprise

Quotas können Requests, KI-Aufrufe, Speicher, Exporte, Worker-Jobs oder Teammitglieder begrenzen.

## 3. Subscription & Billing Readiness

Die Foundation muss Abos vorbereiten, ohne sofort an einen Zahlungsanbieter gebunden zu sein.

Vorbereiten:

- Monatsabo
- Jahresabo
- Testphase
- Upgrade
- Downgrade
- Kündigung
- Provider-Adapter für spätere Integration

## 4. Usage Tracking & Cost Engineering

Kostenintensive Aktivitäten werden gemessen:

- API-Requests
- KI-Tokens
- Worker-Laufzeit
- Speicher
- Exporte
- externe Provider-Kosten

Das Kostenmodell muss Kosten pro User, Workspace, Tenant, Feature, API-Request, Worker-Sekunde und KI-Aufruf aggregieren können.

Usage Tracking ohne Kostenmodell reicht nicht aus.

## 5. Queue & Workers

Langlaufende oder fehleranfällige Aufgaben gehören nicht in den Webserver-Thread.

Worker übernehmen zum Beispiel:

- PDF-Erzeugung
- Bildgenerierung
- Datenimporte
- KI-Analysen
- E-Mail-Versand

Zuverlässigkeit erfordert Retries, Backoff, Idempotenz, Timeouts und Dead-Letter-Queues.

## 6. AI Layer

Moderne SaaS-Produkte brauchen eine isolierte KI-Schicht.

Bausteine:

- Provider-Abstraktion
- Prompt Registry
- Prompt-Versionierung
- strukturierte Ausgaben
- Evaluation
- Caching
- Kosten- und Latenztracking
- Fallback-Modelle

## 7. Observability & Security

Mindeststandard:

- strukturierte Logs
- Request IDs
- Correlation IDs
- Metrics
- Audit Logs
- Admin-Diagnose
- Threat Modeling
- Schutz gegen API-Missbrauch
- Tenant-Isolation-Checks

KI-spezifische Risiken müssen explizit geprüft werden:

- Prompt Injection
- Token Leakage
- Cost Explosion durch Endlosschleifen oder Rekursion
- API-Missbrauch
- Tenant Escape
- ungewollte Weitergabe sensibler Daten an externe Provider

## 8. Developer Experience

ADM priorisiert schnelle lokale Produktivität.

Mindeststandard:

- One Command Setup
- lokale Mocks
- Fake Billing
- Fake AI
- Seed-Daten
- lokale Queue
- lokale Storage-Option
- schnelle Tests

## 9. Testing Strategy

Die Foundation braucht Unit-, Integrations-, Contract- und E2E-Tests. Optional folgen Performance-, Security-, Mutation- und Chaos-Tests.

## 10. Performance Budget

Default-Grenzwerte verhindern unkontrolliertes Latenzwachstum. Abweichungen sind erlaubt, müssen aber im Decision Record begründet werden.

- Standard-API-Requests: unter 150 ms
- Frontend-Ladezeit: unter 2 s
- Cold Starts: unter 500 ms
- Worker-Jobs: maximal 5 Minuten pro Ausführung
- KI- oder Drittanbieter-Requests: eigenes Budget, typischerweise 1500 ms bis 5000 ms; interaktive Langläufer müssen Streaming oder Fortschrittsanzeige nutzen

## 11. Data Lifecycle

Jede relevante Datenklasse braucht einen definierten Lebenszyklus:

1. Upload oder Import
2. Processing
3. Archive
4. Delete
5. Backup
6. Restore

Der Lifecycle gilt besonders für Uploads, Exporte, Logs, KI-Artefakte, temporäre Dateien und Caches.

Ziel: keine Datenmüllhalden, keine ungeplanten Speicherkosten, keine unklare Löschlogik.

## 12. Final Audit

Vor Release wird objektiv geprüft:

- Architektur
- Sicherheit
- Performance
- Kosten
- Codequalität
- Testabdeckung
- AI Readiness
- Dokumentation
- technische Schulden
