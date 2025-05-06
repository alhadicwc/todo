# app/crud.py
from sqlmodel import Session, select
from app.models import Todo
from app.database import engine

def get_todos():
    with Session(engine) as session:
        return session.exec(select(Todo)).all()

def create_todo(todo: Todo):
    with Session(engine) as session:
        session.add(todo)
        session.commit()
        session.refresh(todo)
        return todo
    
def update_todo_status(todo_id: int, completed: bool):
    with Session(engine) as session:
        todo = session.get(Todo, todo_id)
        if not todo:
            return None
        todo.completed = completed
        session.add(todo)
        session.commit()
        session.refresh(todo)
        return todo

def delete_todo(todo_id: int):
    with Session(engine) as session:
        todo = session.get(Todo, todo_id)
        if not todo:
            return False
        session.delete(todo)
        session.commit()
        return True
