from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import json
import os

from helpers import load_tasks, save_tasks, get_next_id

app = FastAPI(title="Task Manager API", description="My final project for the course!")


# --- Pydantic models ---

class Task(BaseModel):
    id: int
    title: str
    description: str | None = None
    completed: bool = False


class TaskCreate(BaseModel):
    title: str
    description: str | None = None


class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    completed: bool | None = None


# serve the frontend if it exists
if os.path.exists("static"):
    app.mount("/static", StaticFiles(directory="static"), name="static")

    @app.get("/")
    def serve_frontend():
        return FileResponse("static/index.html")
else:
    @app.get("/")
    def root():
        return {"message": "Task Manager API is running!", "docs": "/docs"}


# Helper to find a task by id 

def find_task(task_id: int, tasks: list):
    for t in tasks:
        if t["id"] == task_id:
            return t
    return None


# Endpoints 

@app.get("/tasks")
def get_all_tasks(completed: bool | None = None):
    tasks = load_tasks()

    # filter by completed status if the query param is given
    if completed is not None:
        tasks = [t for t in tasks if t["completed"] == completed]

    return tasks


@app.get("/tasks/stats")
def get_stats():
    tasks = load_tasks()

    total = len(tasks)
    done = len([t for t in tasks if t["completed"] == True])
    pending = total - done

    # avoid dividing by zero
    if total == 0:
        percentage = 0.0
    else:
        percentage = round((done / total) * 100, 2)

    return {
        "total": total,
        "completed": done,
        "pending": pending,
        "completion_percentage": percentage
    }


@app.get("/tasks/{task_id}")
def get_single_task(task_id: int):
    tasks = load_tasks()
    task = find_task(task_id, tasks)

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return task


@app.post("/tasks", status_code=201)
def create_task(new_task: TaskCreate):
    tasks = load_tasks()

    task = {
        "id": get_next_id(tasks),
        "title": new_task.title,
        "description": new_task.description,
        "completed": False
    }

    tasks.append(task)
    save_tasks(tasks)

    return task


@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated: TaskUpdate):
    tasks = load_tasks()
    task = find_task(task_id, tasks)

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    # only update fields that were actually sent
    if updated.title is not None:
        task["title"] = updated.title
    if updated.description is not None:
        task["description"] = updated.description
    if updated.completed is not None:
        task["completed"] = updated.completed

    save_tasks(tasks)
    return task


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    tasks = load_tasks()
    task = find_task(task_id, tasks)

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    tasks.remove(task)
    save_tasks(tasks)

    return {"message": f"Task {task_id} deleted successfully"}


@app.delete("/tasks")
def delete_all_tasks():
    save_tasks([])
    return {"message": "All tasks deleted"}
