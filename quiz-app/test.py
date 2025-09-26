import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

'''HTML oldalakat és a JSON fájl meglétét teszteljük'''
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

'''questions.json tartalmának ellenőrzése'''
def test_questions_json_valid_structure(client):
    response = client.get("/questions.json")
    data = response.get_json()
    
    assert isinstance(data, list), "JSON should be a list of questions"
    for i, q in enumerate(data):
        assert "question" in q, f"Question {i} missing 'question' key"
        assert "answers" in q, f"Question {i} missing 'answers' key"
        assert "correct" in q, f"Question {i} missing 'correct' key"
        
        answers = q["answers"]
        assert isinstance(answers, list), f"Question {i} answers should be a list"
        assert len(answers) == 4, f"Question {i} should have exactly 4 answers"

        correct = q["correct"]
        assert isinstance(correct, int), f"Question {i} correct index should be an int"
        assert 0 <= correct < 4, f"Question {i} correct index out of range"

def test_questions_non_empty_text(client):
    response = client.get("/questions.json")
    data = response.get_json()
    
    for i, q in enumerate(data):
        assert q["question"].strip(), f"Question {i} text is empty"
        for j, ans in enumerate(q["answers"]):
            assert ans.strip(), f"Question {i}, answer {j} is empty"