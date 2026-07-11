from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker, declarative_base

# SQLite database file used for storing project data
DATABASE_URL = "sqlite:///./projects.db"

# Database engine used to manage the connection
engine = create_engine(
DATABASE_URL, 
 connect_args={"check_same_thread":False},
)

# Creates database sessions for handling queries
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base class for defining database models
Base = declarative_base()