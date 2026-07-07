# ADM — Vision & Philosophie

Langlebige Softwareprojekte brauchen langlebige Wissensstrukturen. ADM verschiebt die Single Source of Truth weg von flüchtigen Chatfenstern hin zum versionierten Repository.

## Kernvision

KI-gestützte Softwareentwicklung hat ein Kontextproblem: Entscheidungen, Architekturgrenzen und Projektregeln werden oft in einem Chat erklärt, dort vergessen, überschrieben oder bei einem neuen Kontextfenster verloren.

ADM dreht diesen Prozess um. Nicht das Chatfenster speichert den Fortschritt, sondern das Repository selbst.

ADM verbindet moderne CLI-Modelle mit klassischen Software-Engineering-Werkzeugen: Git, Versionierung, Issues, ADRs, Tests, Reviews und strukturierte Dokumentation.

## Git statt Chat-Historie

Der Chat ist nur ein temporärer Arbeitsplatz.

Der ADM-Arbeitsmodus:

1. Ein klar abgegrenzter Schritt wird geplant.
2. Ein Agent arbeitet lokal im Repository.
3. Entscheidungen werden als Dateien dokumentiert.
4. Tests und Reviews werden ausgeführt.
5. Änderungen werden committed.
6. Die Sitzung endet mit einem Handover.
7. Die nächste Sitzung startet aus dem Repository, nicht aus Erinnerung.

## Mensch-Maschine-Kollaboration

Der Mensch bleibt Architekt und Reviewer. Er setzt Ziele, entscheidet Prioritäten, prüft Risiken und genehmigt wichtige Richtungsentscheidungen.

CLI-Agenten arbeiten als ausführende und prüfende Rollen: sie recherchieren, planen, implementieren, testen, dokumentieren und übergeben ihre Arbeit.

## Modellneutralität

Ein Projekt darf nicht von einem einzelnen Modellanbieter abhängig sein. Claude Code, Codex CLI, Antigravity, Gemini CLI, GPT-Modelle oder zukünftige Tools sollen auf derselben dateibasierten Wissensbasis weiterarbeiten können.
