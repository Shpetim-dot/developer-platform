from sqlalchemy import Column, Integer, String
from database import Base

# Defines the database table used to store projects.
class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    language = Column(String)
    status = Column(String)





