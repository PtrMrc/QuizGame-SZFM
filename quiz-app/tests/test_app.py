# RUN: python -m pytest -vv

import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_index_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"<html" in response.data

def test_quiz_page(client):
    response = client.get("/quiz")
    assert response.status_code == 200
    assert b"quiz" in response.data.lower()
def test_end_page(client):
    response = client.get("/end")
    assert response.status_code == 200

def test_review_page(client):
    response = client.get("/review")
    assert response.status_code == 200

def test_questions_json(client):
    response = client.get("/questions.json")
    assert response.status_code == 200
    assert response.is_json
    data = response.get_json()
    assert isinstance(data, list) or isinstance(data, dict)