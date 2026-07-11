# Backend API of the Developer Platform.
# Handles projects, receives JSON data and returns API responses.
from fastapi import FastAPI
from pydantic import BaseModel
from database import engine, SessionLocal, Base
from models import Project 

app = FastAPI()


# Creates database tables if they do not exist
Base.metadata.create_all(bind=engine)


# Temporary project data used before database integration
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
    
    # Creates a new database session for interacting with the database
    db = SessionLocal()

    projects = db.query(Project).all()

    db.close()

    return projects

    



# Defines the structure of project data received from API requests.
# This model validates incoming JSON data before it is processed.
class ProjectCreate(BaseModel):
    name: str
    language: str
    status: str

# Returns a single project by ID
@app.get("/projects/{project_id}")
def get_project(project_id: int):

   # Creates a new database session for interacting with the database
    db = SessionLocal()

    # Searches the database for a project with the matching ID.
    # .filter() defines the condition, .first() returns only one result (or None)
    project = db.query(Project).filter(Project.id == project_id).first()

    db.close()

    if project is None:
        return {
            "message": "Projekt nicht gefunden"
        }

    return project

# Creates a new project
@app.post("/projects")
def create_project(project: ProjectCreate):

# Creates a new database session for interacting with the database
    db= SessionLocal()

# Builds a new Project object (matches the database table structure)
    # using the validated data from the incoming request
    new_project = Project (
        name=project.name,
        language=project.language,
        status=project.status
    )

    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    db.close()


    return {
        "message": "Projekt erfolgreich erstellt!",
        "project": new_project
    }


# Updates an existing project
@app.put("/projects/{project_id}")
def update_project(project_id: int, updated_project: ProjectCreate):

    db = SessionLocal()

    # Searches the database for a project with the matching ID
    project = db.query(Project).filter(Project.id == project_id).first()

    if project is None:
        db.close()
        return {
            "message": "Projekt nicht gefunden"
        }

    # Updates the fields of the existing database object with the new values
    project.name = updated_project.name
    project.language = updated_project.language
    project.status = updated_project.status

    db.commit()
    db.refresh(project)
    db.close()

    return {
        "message": "Projekt erfolgreich aktualisiert!",
        "project": project
    }



# Deletes a project by its ID
@app.delete("/projects/{project_id}")
def delete_project(project_id: int):

    db = SessionLocal() 

    project = db.query(Project).filter(Project.id == project_id).first()
    
    if project is None:
         db.close()


         return { 
        "message": "Projekt nicht gefunden"
             
        }
    
    db.delete(project)
    db.commit()
    db.close()

    return {
        "message": "Projekt erfolgreich gelöscht!"
    }

       
       
