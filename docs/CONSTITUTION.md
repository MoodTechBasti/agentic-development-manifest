# ADM — Die Verfassung (v0.2 Draft)

Diese Prinzipien definieren Denkweise, Arbeitsorganisation und Systemgrenzen ADM-konformer Projekte.

## 1. Model Neutral

ADM darf keine anbieterspezifischen Funktionen voraussetzen. Tool-spezifische Fähigkeiten sind erlaubt, aber nur als Adapter, nicht als Grundlage des Standards.

## 2. Multi-Agent First

Komplexe Arbeit wird durch spezialisierte Rollen bearbeitet. Es gilt: so viele Spezialisten wie nötig, so wenige wie möglich.

## 3. Agent Registry

Jede aktive Rolle muss im Projekt registriert sein: Mission, Verantwortung, Abhängigkeiten, Schnittstellen und aktueller Status.

## 4. Shared Knowledge

Wichtige Erkenntnisse, Recherchen, Benchmarks und Entscheidungen fließen in eine gemeinsame, versionierte Wissensbasis zurück.

## 5. Living Documentation

Dokumentation ist Teil der Arbeit, nicht Nacharbeit. Architekturentscheidungen, Schnittstellen, Datenflüsse und Handovers werden während der Umsetzung aktualisiert.

## 6. Project Memory

Der Projektzustand liegt im Repository, nicht im Chatkontext eines einzelnen Modells.

## 7. Agent Handover

Jede Sitzung endet mit einer Übergabe: erledigt, offen, Risiken, geänderte Dateien, Tests, Metriken und nächste logische Aufgabe.

## 8. Artifact-Based Communication

Agenten kommunizieren über Dateien, Entscheidungen, Reviews und Tasks. Unstrukturierte direkte Kommunikation ist keine zuverlässige Quelle.

## 9. Vendor Independence

Die Steuerungsstruktur gehört dem Projekt. Anbieter-CLIs dürfen daraus temporäre Konfigurationen ableiten, aber nicht die Kernstruktur besitzen.

## 10. CLI Friendly

ADM optimiert für Terminal, Git, Tests, Linter, Build-Systeme und reproduzierbare lokale Umgebungen. Eine visuelle IDE darf nie Voraussetzung sein.

## Harte Regeln für AI-Coding-Friendliness

Diese Regeln sind verbindlich, damit Code für Menschen und Agenten leicht lesbar, testbar und änderbar bleibt.

1. Quellcodedateien sollen maximal 300 Zeilen enthalten.
2. Ausnahmen sind erlaubt, müssen aber in einem Decision Record begründet werden.
3. Keine God Classes, God Modules oder Dateien mit vermischten Verantwortlichkeiten.
4. Schnittstellen müssen explizit, typisiert und dokumentiert sein.
5. Implizite Magie, versteckte globale Zustände und schwer verfolgbare Seiteneffekte sind zu vermeiden.
6. Module sollen niedrige Kopplung und hohe Testbarkeit besitzen.
7. Technische Dokumentation gehört möglichst nah an den relevanten Code.

## Quality Bar

Eine Aufgabe ist erst fertig, wenn Entscheidung, Umsetzung, Tests, Risiken, Metriken und nächste Schritte aus dem Repository nachvollziehbar sind.
