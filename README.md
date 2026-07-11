# Developer Platform API

A backend REST API for managing software projects.

This project was created to gain practical experience in backend development, REST APIs, data validation, database integration, containerization, and modern software development workflows.

## Overview

The Developer Platform API provides a simple backend system for managing project information.

The API allows users to create, read, update, and delete projects through REST endpoints.

Project data is persisted in a SQLite database using SQLAlchemy as the ORM (Object-Relational Mapper), so data remains available after restarting the server.

## Features

- REST API built with FastAPI
- CRUD operations for project management:
  - Create projects
  - Read project data
  - Update existing projects
  - Delete projects
- Persistent data storage using SQLite and SQLAlchemy
- Automatic API documentation with Swagger UI
- Data validation using Pydantic
- Containerized application using Docker
- Dependency management using requirements.txt
- Version control using Git and GitHub

## Technologies

| Technology | Purpose |
|---|---|
| Python | Programming language |
| FastAPI | Backend REST API framework |
| Pydantic | Data validation and data models |
| SQLAlchemy | ORM for database interaction |
| SQLite | Lightweight relational database |
| Uvicorn | Server for running the API |
| Docker | Containerization and consistent environments |
| Git/GitHub | Version control and project management |

## Project Structure
developer-platform/
│
├── main.py # FastAPI backend application (API routes)
├── database.py # Database connection and session setup
├── models.py # SQLAlchemy database models
├── requirements.txt # Python dependencies
├── Dockerfile # Docker container configuration
├── README.md # Project documentation
├── LICENSE
└── .gitignore

## Installation

### Clone the repository

```bash
git clone <repository-url>
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Start the API

```bash
uvicorn main:app --reload
```

The database table is created automatically on startup if it doesn't already exist.

The API is available at:

http://127.0.0.1:8000

Interactive API documentation:

http://127.0.0.1:8000/docs

## Run with Docker

### Build Docker image

```bash
docker build -t developer-platform .
```

### Start container

```bash
docker run -p 8000:8000 developer-platform
```

The API will then be available at:

http://localhost:8000

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | / | Check API status |
| GET | /projects | Get all projects |
| GET | /projects/{id} | Get a specific project |
| POST | /projects | Create a new project |
| PUT | /projects/{id} | Update a project |
| DELETE | /projects/{id} | Delete a project |

## Example Project Data

Request body for creating or updating a project (the `id` is generated automatically by the database):

```json
{
  "name": "DevHub",
  "language": "Python",
  "status": "Running"
}
```

## Future Improvements

- Add PostgreSQL database integration for production use
- Add user authentication and authorization
- Improve API security
- Add automated testing
- Deploy the application to a cloud environment

## Learning Goals

This project was created to improve practical skills in:

- Backend development
- REST API design
- Database integration with SQLAlchemy
- Python programming
- Docker containerization
- Software development workflows

## Author

Created as a personal learning project to develop practical experience in modern software development.