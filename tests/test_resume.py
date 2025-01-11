import pytest
from fastapi.testclient import TestClient

# Mock storage for resumes
resume_storage = {}
resume_id_counter = 1

def test_create_resume(client: TestClient, mocker):
    global resume_id_counter
    
    # Mock the storage operation
    mocker.patch('app.routes.resume.create_resume', 
        return_value={"id": resume_id_counter, "user_id": 1, "title": "Test Resume"})

    response = client.post(
        "/resume",
        json={"user_id": 1, "title": "Test Resume"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Resume"
    assert data["user_id"] == 1
    assert data["id"] == resume_id_counter

def test_get_resume(client: TestClient, mocker):
    # Mock the get operation
    mocker.patch('app.routes.resume.get_resume',
        return_value={"id": 1, "user_id": 1, "title": "Test Resume"})

    response = client.get("/resume/1")
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Resume"
    assert data["id"] == 1

def test_update_resume(client: TestClient, mocker):
    # Mock the update operation
    mocker.patch('app.routes.resume.update_resume',
        return_value={"id": 1, "user_id": 1, "title": "Updated Resume"})

    response = client.put(
        "/resume/1",
        json={"title": "Updated Resume"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Updated Resume"

def test_delete_resume(client: TestClient, mocker):
    # Mock the delete operation
    mocker.patch('app.routes.resume.delete_resume', return_value=True)
    
    # Test successful deletion
    response = client.delete("/resume/1")
    assert response.status_code == 200
    
    # Mock resume not found
    mocker.patch('app.routes.resume.get_resume', return_value=None)
    
    # Verify it's deleted
    get_response = client.get("/resume/1")
    assert get_response.status_code == 404

def test_resume_not_found(client: TestClient, mocker):
    mocker.patch('app.routes.resume.get_resume', return_value=None)
    
    response = client.get("/resume/999")
    assert response.status_code == 404
