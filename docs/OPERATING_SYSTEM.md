# ADM — Operating System

> Status: v0.26 synchronized draft
> Last updated: 2026-07-08
> Scope: file-based ADM project operating model, not runtime implementation

Dieses Dokument beschreibt das dateibasierte Kontrollzentrum eines ADM-konformen Projekts. Es speichert Projektzustand, Rollen, Tasks, Entscheidungen, Reviews, Review-Archive, Memory, Standards und Übergaben so, dass verschiedene CLI-Tools und Modelle weiterarbeiten können.

Der Projektzustand muss aus dem Repository lesbar sein. Ein Agent darf ihn nicht aus Chat-Erinnerung, hidden model memory, Tool-Cache oder lokalen Scratch-Dateien rekonstruieren müssen.

## 1. Struktur

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

Tool-specific adapter prompts are stored under `prompts/adapters/`, not inside `.ai/`, because they are reusable prompt artifacts rather than runtime state.

## 2. Authority Order

| Rang | Quelle | Bedeutung |
| --- | --- | --- |
| 1 | `spec/`, `docs/`, `ROADMAP.md`, accepted ADRs | Kanonische Projektwahrheit |
| 2 | `prompts/master_prompt.md`, `prompts/adapters/` | Kanonische und abgeleitete Agenten-Startanweisungen |
| 3 | `.ai/reviews/`, `.ai/reviews/archive/`, `.ai/handover/`, `.ai/decisions/` | Versionierte Runtime-Historie |
| 4 | `.ai/memory/`, `.ai/knowledge/`, `.ai/tasks/`, `.ai/agents/` | Kuratierter Kontext, Rollen und Arbeitszustand |
| 5 | `.ai/tmp/`, `.ai/logs/`, `.ai/cache/`, `.ai/scratch/` | Lokale transiente Daten |
| 6 | Chatverlauf, hidden model memory, Tool-State | Nicht autoritativ |

## 3. Template- und Laufzeit-Trennung

ADM trennt wiederverwendbare Vorlagen von ausgefüllten Laufzeit-Artefakten.

- Wiederverwendbare Review-Vorlagen liegen unter `templates/reviews/`.
- Ausgefüllte, aktive Review-Berichte liegen direkt unter `.ai/reviews/`.
- Archivierte historische Review-Sets dürfen später unter `.ai/reviews/archive/<review_set_id>/` liegen.
- Wiederverwendbare Handover-Vorlagen liegen unter `templates/HANDOVER_TEMPLATE.md`.
- Ausgefüllte, konkrete Handovers liegen unter `.ai/handover/`.
- Wiederverwendbare Adapter-Prompts liegen unter `prompts/adapters/`.
- Leere Templates dürfen nicht in `.ai/reviews/` oder `.ai/handover/` abgelegt werden.
- Ausgefüllte Reviews nutzen ihren `review_id` als Dateiname, nicht statische Rollennamen.

Diese Trennung verhindert, dass Projektgedächtnis, Review-Historie, Handover-Historie, Adapter-Prompts und wiederverwendbare Schablonen vermischt werden.

## 4. Review-Vorlagen, Review-Set-Scoping und Archivierung

Die Standard-Reviews des Multi-Agenten-Parlaments sind:

| Template | Rolle | Runtime Prefix |
| --- | --- | --- |
| `templates/reviews/architect.md` | Principal Architect | `REV-ARCH` |
| `templates/reviews/security.md` | Security Engineer | `REV-SEC` |
| `templates/reviews/performance.md` | SRE and Performance Lead | `REV-PERF` |
| `templates/reviews/cost.md` | Cost Engineer | `REV-COST` |
| `templates/reviews/simplifier.md` | Simplifier | `REV-SIMP` |
| `templates/reviews/documentation.md` | Documentation Reviewer | `REV-DOC` |

Ein Review-Set ist eine zusammengehörige Freigabe-Einheit aus sechs Rollen-Reviews.

Jedes ausgefüllte Review-Artefakt muss die folgenden Scope-Felder enthalten:

- `review_set_id`: gemeinsame Set-ID, zum Beispiel `RSV-20260708-review-archive-policy`,
- `target_ref`: Zielreferenz, zum Beispiel `adm-v026-review-archive-policy`,
- `target_commit`: Git-Commit-SHA des geprüften Codes oder der geprüften Dokumentation.

`target_commit` bezeichnet den geprüften Stand. Es ist nicht zwingend der Workflow-Commit, der die Review-Artefakte enthält.

Ein Release-Gate darf nur grün werden, wenn alle sechs Rollen dieselbe `review_set_id`, dieselbe `target_ref` und denselben stabilen `target_commit` verwenden.

Direkte `.ai/reviews/*.md` Dateien sind die aktive Review-Fläche. `.ai/reviews/archive/<review_set_id>/` ist nur historische Ablage nach abgeschlossener Release- oder Governance-Nutzung. Archivierung darf keine aktuellen Validatorfehler verstecken.

## 5. Review-Validierung

Ausgefüllte aktive Review-Artefakte unter `.ai/reviews/` können lokal geprüft werden.

```bash
python3 scripts/validate_reviews.py --path . --mode advisory
python3 scripts/validate_reviews.py --path . --mode existing-strict
python3 scripts/validate_reviews.py --path . --mode complete-set --review-set-id <set-id> --target-ref <ref> --target-commit <git-sha>
```

Der Validator prüft das YAML-Frontmatter, Pflichtfelder, Review-ID-Präfixe, Review-Set-Scope, Review-Status, `runtime_target: .ai/reviews/`, `ci_ready` und optional den Confidence Score.

`complete-set` geht weiter: alle sechs Standard-Review-Typen müssen vorhanden, `PASSED`, `ci_ready: true` und auf denselben Scope gebunden sein.

Der Standardpfad ist nicht rekursiv: Archivierte Review-Dateien unter `.ai/reviews/archive/**` werden bei normalen Läufen gegen `.ai/reviews/` nicht validiert.

## 6. Release Hygiene

Release-Hygiene ist Teil des Operating Systems, aber keine Release-Automation.

Vor einem Release müssen Agenten und Maintainer unterscheiden:

- stabiler geprüfter Commit: der nicht-review Commit, auf den Reviews zeigen,
- Review-Artefakt-Commit: der spätere Commit mit `.ai/reviews/`,
- finaler Tag-Commit: der `main`-Commit nach Merge der Reviews und erfolgreicher manueller `complete-set`-Validierung.

GitHub-Rulesets sind externe Repository-Einstellungen. Sie müssen manuell auditiert werden, wenn Governance-, Review-, Release- oder Branch-Protection-Reife behauptet wird. Source-Dateien allein beweisen diesen Audit nicht.

## 7. Review Archive Policy

Die Review Archive Policy ist ein v0.26 Governance-Hygiene-Baseline vor Roadmap Phase 7.

Sie definiert:

- neue Review-Sets entstehen weiterhin direkt unter `.ai/reviews/`,
- historische Sets dürfen später nach `.ai/reviews/archive/<review_set_id>/` verschoben werden,
- v0.26 verschiebt keine alten Reviews,
- `scripts/validate_reviews.py` wird in v0.26 nicht produktiv verändert,
- `scripts/test_validate_reviews.py` schützt den nicht-rekursiven Standardpfad mit Fixture-Coverage.

## 8. Handover Automation

Handover Automation beschreibt, welche Übergabeinformationen später sicher vorbefüllt, gelintet oder validiert werden dürfen.

Maschinenprüfbare Feldgruppen:

| Feldgruppe | Beispiele | Automationsgrenze |
| --- | --- | --- |
| Identität | `session_id`, `timestamp`, `outgoing_agent`, `active_role` | Format und Vorhandensein prüfbar |
| Scope | `changed_files`, `target_ref`, `target_commit`, `review_set_id` | Pfade und Git-/Review-Referenzen prüfbar |
| Qualität | Checks, Review-Status, CI-readiness | Statuswerte prüfbar, Wahrheitsgehalt nur mit Evidenz |
| Routing | nächster Registry-Agent, Routing-Grund | Role-ID prüfbar, Begründung human-review |
| Zustand | erledigte, offene und blockierte Tasks | Struktur prüfbar, Inhalt human-review |

Spätere Tools dürfen Handovers aus Git-Status, Branch-Informationen, Review-Dateien, aktiven Tasks und Agent Registry vorbefüllen oder prüfen.

Handover Automation darf keine Checks, Commits, CI-Ergebnisse, Review-Votes, Rollen, Freigaben oder abgeschlossene Arbeit erfinden. Sie darf keine PRs mergen, Tags setzen, Branch Protection ändern oder Chatverlauf, hidden model memory, Scratch-Dateien, Rohlogs, private Pfade oder Secrets als autoritative Quellen verwenden.

Roadmap Phase 7 bleibt nach v0.26 offen. v0.26 implementiert keinen Handover-Linter und keine Handover-Automation.

## 9. Foundation Standards

SaaS Foundation Standard, AI Foundation Standard, Master Prompt Standard und Adapter Prompt Standard bleiben gültige Roadmap-Standards. v0.26 verändert deren technische Semantik nicht.
