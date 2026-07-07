# ADM — Operating System (v0.2 Draft)

Dieses Dokument beschreibt das dateibasierte Kontrollzentrum eines ADM-konformen Projekts. Es speichert Projektzustand, Rollen, Tasks, Entscheidungen, Reviews und Übergaben so, dass verschiedene CLI-Tools und Modelle weiterarbeiten können.

## Zweck

Der Projektzustand muss aus dem Repository lesbar sein. Ein Agent darf ihn nicht aus Chat-Erinnerung rekonstruieren müssen.

## Struktur

```text
.ai/
├── manifest/
├── knowledge/
├── agents/
├── research/
├── planning/
├── reviews/
├── decisions/
├── memory/
├── tasks/
├── protocols/
├── audit/
├── quality/
├── handover/
├── roadmap/
├── experiments/
├── benchmarks/
├── standards/
└── playbooks/
```

## Sitzungs-Lifecycle

1. Initialisierung: Manifest, Tasks, Entscheidungen und letzten Handover lesen.
2. Registrierung: Rolle, Mission und Arbeitsumfang eintragen.
3. Task-Übernahme: Aufgabe als aktiv markieren.
4. Ausführung: lokal arbeiten, testen und dokumentieren.
5. Review: Self-Review und Spezialreviews ausführen.
6. Übergabe: Tasks, Memory, Metriken und Handover aktualisieren.
7. Commit: Änderungen versionieren.

## Erweitertes Handover-Protokoll

Jeder Handover unter `.ai/handover/` muss mindestens enthalten:

### 1. Task State

- abgeschlossene Tasks
- offene oder blockierte Tasks
- betroffene Dateien

### 2. Technische Metriken

- Linter-Status
- Compiler- oder Typecheck-Status
- Teststatus
- Coverage, falls verfügbar
- Dateien über 300 Zeilen
- Decision Records für begründete Ausnahmen

### 3. Performance und Budgets

- gemessene Latenzen, falls relevant
- Budget-Verstöße
- Begründung oder Decision Record für akzeptierte Abweichungen

### 4. Risikoanalyse

- neu erkannte Architektur-, Sicherheits-, Kosten- oder Betriebsrisiken
- offene Fragen
- blockierende Annahmen

### 5. Nächste Schritte

- nächste logische Aufgabe
- empfohlene Rolle für die nächste Sitzung
- Hinweise für den nächsten Agenten

## Handover-Regel

Kein Agent darf eine größere Arbeit als abgeschlossen markieren, wenn der Handover nicht nachvollziehbar erklärt, was getan wurde, was geprüft wurde und was als Nächstes passieren muss.
