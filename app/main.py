# app/main.py
from fastapi import FastAPI, HTTPException
from app.models import Todo
from app.database import create_db_and_tables
from app.crud import get_todos, create_todo, update_todo_status, delete_todo

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/todos")
def read_todos():
    return get_todos()

@app.post("/todos")
def add_todo(todo: Todo):
    return create_todo(todo)

@app.put("/todos/{todo_id}/status")
def change_status(todo_id: int, completed: bool):
    updated = update_todo_status(todo_id, completed)
    if updated is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return updated

@app.delete("/todos/{todo_id}")
def remove_todo(todo_id: int):
    success = delete_todo(todo_id)
    if not success:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"detail": f"Todo with ID {todo_id} deleted successfully"}
