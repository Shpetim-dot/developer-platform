# Developer Platform API 🚀

## Projektübersicht

Die **Developer Platform API** ist ein Backend-Projekt, das mit **Python und FastAPI** entwickelt wurde.

Das Ziel des Projekts ist es, eine einfache Plattform zur Verwaltung von Entwicklerprojekten bereitzustellen. Die API kann Projektdaten empfangen, speichern, abrufen, aktualisieren und löschen.

Das Projekt zeigt grundlegende Kenntnisse in der Backend-Entwicklung, REST-APIs und strukturierter Softwareentwicklung.

---

## Funktionen

Die API unterstützt folgende CRUD-Operationen:

| Funktion | Beschreibung                                    |
| -------- | ----------------------------------------------- |
| Create   | Neue Projekte über eine API-Anfrage erstellen   |
| Read     | Projekte anzeigen und einzelne Projekte abrufen |
| Update   | Bestehende Projekte bearbeiten                  |
| Delete   | Projekte anhand ihrer ID löschen                |

---

## Verwendete Technologien

| Technologie  | Verwendung                                     |
| ------------ | ---------------------------------------------- |
| Python       | Programmiersprache                             |
| FastAPI      | Framework für die Erstellung der REST API      |
| Pydantic     | Validierung und Strukturierung von Daten       |
| JSON         | Austausch von Daten zwischen Client und Server |
| Git & GitHub | Versionskontrolle und Projektverwaltung        |

---

## Projektstruktur

```
developer-platform/
│
├── main.py          # Backend API
├── README.md        # Projektdokumentation
├── .gitignore       # Ignorierte Dateien
└── LICENSE          # Projektlizenz
```

---

## API Endpunkte

### Startseite

**GET /**

Überprüft, ob die API aktiv ist.

Antwort:

```json
{
  "message": "Developer Platform API läuft"
}
```

---

### Alle Projekte abrufen

**GET /projects**

Gibt eine Liste aller gespeicherten Projekte zurück.

Beispiel:

```json
[
    {
        "id": 1,
        "name": "DevHub",
        "language": "Python",
        "status": "Running"
    }
]
```

---

### Einzelnes Projekt abrufen

**GET /projects/{project_id}**

Sucht ein Projekt anhand seiner ID.

Beispiel:

```
GET /projects/1
```

---

### Projekt erstellen

**POST /projects**

Erstellt ein neues Projekt.

Beispiel JSON:

```json
{
    "id": 3,
    "name": "Website",
    "language": "Python",
    "status": "Running"
}
```

---

### Projekt aktualisieren

**PUT /projects/{project_id}**

Aktualisiert ein bestehendes Projekt.

---

### Projekt löschen

**DELETE /projects/{project_id}**

Entfernt ein Projekt anhand seiner ID.

---

## Installation

Repository klonen:

```bash
git clone https://github.com/DEIN-NAME/developer-platform.git
```

In den Projektordner wechseln:

```bash
cd developer-platform
```

Benötigte Pakete installieren:

```bash
pip install fastapi uvicorn
```

---

## API starten

Server starten:

```bash
uvicorn main:app --reload
```

Die API läuft danach unter:

```
http://127.0.0.1:8000
```

FastAPI Dokumentation:

```
http://127.0.0.1:8000/docs
```

---

## Aktueller Entwicklungsstand

Dieses Projekt verwendet aktuell einen temporären Speicher im Arbeitsspeicher.

Die nächsten geplanten Erweiterungen:

* Datenbank Integration (SQLite/PostgreSQL)
* Docker Containerisierung
* Benutzerverwaltung und Authentifizierung
* Automatisierte Tests
* Deployment in der Cloud
* CI/CD Pipeline

---

## Lernziele

Mit diesem Projekt wurden folgende Bereiche praktisch umgesetzt:

* Entwicklung einer REST API
* Arbeiten mit Backend-Frameworks
* Datenmodellierung mit Pydantic
* Umgang mit Git und GitHub
* Strukturierung und Dokumentation eines Softwareprojekts

---

## Autor

Erstellt als persönliches Lernprojekt im Bereich Backend- und Plattformentwicklung.
