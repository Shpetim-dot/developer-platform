# Backend-API der Developer Platform.
# Verarbeitet Projekte, empfängt JSON-Daten und gibt API-Antworten zurück.

from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


# Temporärer Speicher für Projekte
# Später wird dieser durch eine Datenbank ersetzt.
projects = [
    {
        "id": 1,
        "name": "DevHub",
        "language": "Python",
        "status": "Running"
    },
    {
        "id": 2,
        "name": "Portfolio",
        "language": "JavaScript",  
        "status": "Completed"
    }
]


# Startseite der API
@app.get("/")
def home():
    return {
        "message": "Developer Platform API läuft"
    }


# Gibt alle Projekte zurück
@app.get("/projects")
def get_projects():
    return projects


# Struktur eines Projekts
class Project(BaseModel):
    id: int
    name: str
    language: str
    status: str

@app.get("/projects/{project_id}")
def get_project(project_id: int):

    for project in projects:
        if project["id"] == project_id:
            return project

    return {
        "message": "Projekt nicht gefunden"
    }

# Erstellt ein neues Projekt
@app.post("/projects")
def create_project(project: Project):

    projects.append(project.model_dump())

    return {
        "message": "Projekt erfolgreich erstellt!",
        "project": project
    }


  #Aktualisiert ein bestehendes Projekt
@app.put("/projects/{project_id}")
def update_project(project_id: int, updated_project: Project):

      for index, project in enumerate(projects):
          if project["id"] == project_id:
              projects[index] = updated_project.model_dump()
              return {
                  "message": "Projekt erfolgreich aktualisiert!",
                  "project": updated_project
              }

      return {
          "message": "Projekt nicht gefunden"
      }

# Löscht ein Projekt anhand seiner ID
@app.delete("/projects/{project_id}")
def delete_project(project_id: int):

# Durchsucht die Projektliste nach dem passenden Projekt
 for project in projects:
     if project["id"] == project_id:       # Prüft, ob die ID mit der gesuchten ID übereinstimmt
         projects.remove(project)

         return { 
        "message": "Projekt erfolgreich gelöscht!"
             
        }
       
       
        # Falls kein Projekt mit der angegebenen ID gefunden wurde,
        # gibt die API eine Fehlermeldung zurück. 
         return {
        "message": "Projekt nicht gefunden"
        }