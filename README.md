# 📝 FastAPI To-Do App

A simple and clean To-Do List API built with **FastAPI**, **SQLModel**, and **PostgreSQL**. This backend project allows you to perform basic CRUD operations on to-do items and explore the API via an interactive Swagger UI.

---

## 🚀 Features

- Add new to-do items with title and description
- Mark tasks as completed or not completed
- View all tasks
- Delete tasks
- Automatically creates database tables on startup
- Interactive API docs via Swagger (`/docs`)

---

## 🧰 Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/) — Web framework
- [SQLModel](https://sqlmodel.tiangolo.com/) — ORM and data models
- [PostgreSQL](https://www.postgresql.org/) — Database
- [Uvicorn](https://www.uvicorn.org/) — ASGI server

---

## 📦 Project Structure
```bash
app/
├── crud.py # CRUD operations
├── database.py # DB engine and table creation
├── main.py # API routes and FastAPI app
├── models.py # SQLModel data model

```

## 🛠️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/alhadicwc/todo.git
```
### 2. Set up a virtual environment

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

### 3. Install dependencies

pip install -r requirements.txt

### 4. Set up PostgreSQL
Make sure PostgreSQL is running, and create a database named todo_db.

You can create it with:

sql

CREATE DATABASE todo_db;
Update the database URL in app/database.py if needed:

python

DATABASE_URL = "postgresql://postgres:<your_password>@localhost:5432/todo_db"
▶️ Run the app
bash

uvicorn app.main:app --reload
Then open your browser and navigate to:

Swagger UI: http://localhost:8000/docs

ReDoc: http://localhost:8000/redoc

🧪 Example API Calls
Create a Todo (POST /todos)
json
Copy
Edit
{
  "title": "Buy groceries",
  "description": "Milk, Bread, Eggs"
}
Update Status (PUT /todos/1/status?completed=true)
