from fastapi.testclient import TestClient
from app.app import app

client = TestClient(app)


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_create_task():
    response = client.post(
        "/tasks",
        json={"title": "Learn pytest"}
    )

    assert response.status_code == 200
    assert response.json()["title"] == "Learn pytest"
    assert response.json()["status"] == "pending"

def test_get_tasks():
    client.post(
        "/tasks",
        json={"title": "Test retrieval"}
    )

    response = client.get("/tasks")

    assert response.status_code == 200

    tasks = response.json()

    assert isinstance(tasks, list)
    assert len(tasks) > 0
    assert tasks[-1]["title"] == "Test retrieval"

def test_task_not_found():
    response = client.get("/tasks/99999")

    assert response.status_code == 404
    assert response.json() == {"detail": "Task not found"}