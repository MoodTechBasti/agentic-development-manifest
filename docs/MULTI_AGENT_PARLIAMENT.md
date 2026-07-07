# ADM — Multi-Agenten-Parlament

Das Multi-Agenten-Parlament verhindert, dass ein einzelner Agent den ersten plausiblen Weg ungeprüft umsetzt.

## Prinzip

Vor größeren Entscheidungen prüfen spezialisierte Rollen denselben Entwurf aus unterschiedlichen Perspektiven. Gibt es starke Einwände, wird überarbeitet.

## Kernrollen

### Principal Architect

Verantwortlich für Zielarchitektur, Modulgrenzen, Kopplung, Wartbarkeit und Testbarkeit.

### Devil's Advocate

Sucht aktiv nach Schwachstellen, technischen Schulden, Skalierungsrisiken, Single Points of Failure und schlechten Annahmen.

### Simplifier

Reduziert Komplexität. Entfernt unnötige Abstraktionen, Abhängigkeiten und zu große Modulstrukturen.

### Security Engineer

Prüft Threat Modeling, Tenant Isolation, Secrets, Zugriffskontrolle, API-Missbrauch und Prompt-Injection-Risiken.

### SRE & Performance Lead

Prüft Latenzen, Caching, Retry-Strategien, Timeouts, Circuit Breaker, Health Checks und Graceful Shutdown.

### Cost Engineer

Prüft Cloudkosten, Tokenverbrauch, Kosten pro Nutzer, Kosten pro Workspace, Kosten pro Feature und Caching-Effizienz.

### AI Architect

Prüft Provider-Abstraktion, Prompt-Versionierung, strukturierte Ausgaben, Fallback-Modelle, Evaluation und KI-Latenz.

## Entscheidungsprozess

1. Principal Architect legt einen Entwurf vor.
2. Spezialrollen prüfen den Entwurf.
3. Einwände werden dokumentiert.
4. Kritische Vetos müssen aufgelöst werden.
5. Die finale Entscheidung wird als Decision Record gespeichert.
