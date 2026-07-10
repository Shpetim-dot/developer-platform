# Backend API of the Developer Platform.
# Handles projects, receives JSON data and returns API responses.
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


## Temporary storage for projects.
# Will be replaced by a database in the future.
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

# API homepage
@app.get("/")
def home():
    return {
        "message": "Developer Platform API läuft"
    }


# Returns all projects
@app.get("/projects")
def get_projects():
    return projects


# Defines the structure of a project
class Project(BaseModel):
    id: int
    name: str
    language: str
    status: str

# Returns a single project by ID
@app.get("/projects/{project_id}")
def get_project(project_id: int):

    for project in projects:
        if project["id"] == project_id:
            return project

    return {
        "message": "Projekt nicht gefunden"
    }

# Creates a new project
@app.post("/projects")
def create_project(project: Project):

    projects.append(project.model_dump())

    return {
        "message": "Projekt erfolgreich erstellt!",
        "project": project
    }


# Updates an existing project
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

# Deletes a project by its ID
@app.delete("/projects/{project_id}")
def delete_project(project_id: int):

# Searches the project list for the matching project
 for project in projects:
     if project["id"] == project_id:       # Prüft, ob die ID mit der gesuchten ID übereinstimmt
         projects.remove(project)

         return { 
        "message": "Projekt erfolgreich gelöscht!"
             
        }
       
       
# Returns an error if no matching project was found.
         return {
        "message": "Projekt nicht gefunden"
        }