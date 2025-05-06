# app/database.py
from sqlmodel import SQLModel, create_engine

DATABASE_URL = "postgresql://postgres:8287@localhost:5432/todo_db"
engine = create_engine(DATABASE_URL, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
