# ADM — Operating System (v0.10 Draft)

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

## Template- und Laufzeit-Trennung

ADM trennt wiederverwendbare Vorlagen von ausgefüllten Laufzeit-Artefakten.

- Wiederverwendbare Review-Vorlagen liegen unter `templates/reviews/`.
- Ausgefüllte, konkrete Review-Berichte liegen unter `.ai/reviews/`.
- Leere Templates dürfen nicht in `.ai/reviews/` abgelegt werden.

Diese Trennung verhindert, dass Projektgedächtnis, Review-Historie und wiederverwendbare Schablonen vermischt werden.

## Review-Vorlagen

Die Standard-Reviews des Multi-Agenten-Parlaments sind:

| Template | Rolle | Runtime Prefix |
| --- | --- | --- |
| `templates/reviews/architect.md` | Principal Architect | `REV-ARCH` |
| `templates/reviews/security.md` | Security Engineer | `REV-SEC` |
| `templates/reviews/performance.md` | SRE and Performance Lead | `REV-PERF` |
| `templates/reviews/cost.md` | Cost Engineer | `REV-COST` |
| `templates/reviews/simplifier.md` | Simplifier | `REV-SIMP` |
| `templates/reviews/documentation.md` | Documentation Reviewer | `REV-DOC` |

## Review-Validierung

Ausgefüllte Review-Artefakte unter `.ai/reviews/` können lokal geprüft werden.

Advisory-Modus für frühe Entwicklungsarbeit:

```bash
python scripts/validate_reviews.py --path . --mode advisory
```

Strikter Modus für vorhandene Review-Artefakte:

```bash
python scripts/validate_reviews.py --path . --mode existing-strict
```

Vollständiger Review-Set-Modus für Release-Gates:

```bash
python scripts/validate_reviews.py --path . --mode complete-set
```

Der Validator prüft das YAML-Frontmatter, Pflichtfelder, Review-ID-Präfixe, Review-Status, `runtime_target: .ai/reviews/`, `ci_ready` und optional den Confidence Score.

`complete-set` geht weiter: alle sechs Standard-Review-Typen müssen vorhanden, `PASSED` und `ci_ready: true` sein.

Im GitHub-Workflow wird die Review-Validierung kontextabhängig ausgeführt:

| Kontext | Modus |
| --- | --- |
| Feature-Branch / `dev` | `advisory` |
| PR nach `main` / `master` | `existing-strict` |
| Push auf `main` / `master` | `existing-strict` |
| `release/**` | `complete-set` |
| Manuell per `workflow_dispatch` | auswählbar, Standard `existing-strict` |

Diese Trennung verhindert, dass normale Entwicklungsarbeit durch fehlende Review-Instanzen hart blockiert wird, während Release-Zweige ein echtes vollständiges Review-Gate erhalten.

## Sitzungs-Lifecycle

1. Initialisierung: Manifest, Tasks, Entscheidungen und letzten Handover lesen.
2. Registrierung: Rolle, Mission und Arbeitsumfang eintragen.
3. Task-Übernahme: Aufgabe als aktiv markieren.
4. Ausführung: lokal arbeiten, testen und dokumentieren.
5. Review: Self-Review und Spezialreviews ausführen.
6. Review-Validierung: ausgefüllte Reviews mit `scripts/validate_reviews.py` prüfen, falls Review-Artefakte erstellt wurden.
7. Übergabe: Tasks, Memory, Metriken und Handover aktualisieren.
8. Commit: Änderungen versionieren.

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

### 4. Review-Status

- ausgeführte Review-Vorlagen
- Review-Dateien unter `.ai/reviews/`
- Ergebnis von `scripts/validate_reviews.py`, inklusive Modus
- blockierende Votes
- CI-readiness status

### 5. Risikoanalyse

- neu erkannte Architektur-, Sicherheits-, Kosten- oder Betriebsrisiken
- offene Fragen
- blockierende Annahmen

### 6. Nächste Schritte

- nächste logische Aufgabe
- empfohlene Rolle für die nächste Sitzung
- Hinweise für den nächsten Agenten

## Handover-Regel

Kein Agent darf eine größere Arbeit als abgeschlossen markieren, wenn der Handover nicht nachvollziehbar erklärt, was getan wurde, was geprüft wurde und was als Nächstes passieren muss.
