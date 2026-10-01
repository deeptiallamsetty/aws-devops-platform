from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class TaskCreate(BaseModel):
    title: str

tasks = []
next_id = 1

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/tasks")
def create_task(task: TaskCreate):
    global next_id

    new_task = {
        "id": next_id,
        "title": task.title,
        "status": "pending"
    }

    tasks.append(new_task)
    next_id += 1

    return new_task

@app.get("/tasks")
def get_tasks():
    return tasks

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task

    raise HTTPException(status_code=404, detail="Task not found")


