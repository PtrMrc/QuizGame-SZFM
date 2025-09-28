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
    
    assert isinstance(data, list), "Listának kell lennie"
    for i, q in enumerate(data):
        assert "question" in q, f"Hiányzik a 'question' kulcs a {i}. kérdésnél"
        assert "answers" in q, f"Hiányzik az 'answers' kulcs a {i}. kérdésnél"
        assert "correct" in q, f"Hiányzik a 'correct' kulcs a {i}. kérdésnél"
        
        answers = q["answers"]
        assert isinstance(answers, list), f"Listának kell lennie az answers kulcsnak a {i}. kérdésnél"
        assert len(answers) == 4, f"Pontosan 4 válasznak kell lennie a {i}. kérdésnél"

        correct = q["correct"]
        assert isinstance(correct, int), f"Integernek kell lennie a correct kulcsnak a {i}. kérdésnél"
        assert 0 <= correct < 4, f"Nincs érvényes index a correct kulcsnál a {i}. kérdésnél"

def test_questions_non_empty_text(client):
    response = client.get("/questions.json")
    data = response.get_json()
    
    for i, q in enumerate(data):
        assert q["question"].strip(), f"Hiányzik a kérdés szövege a {i}. kérdésnél"
        for j, ans in enumerate(q["answers"]):
            assert ans.strip(), f"Hiányzik a válasz szövege a {i}. kérdésnél, {j}. válasznál"

'''Leaderboard meglétének ellenőrzése'''
def test_end_page_has_leaderboard(client):
    response = client.get("/end")
    html = response.data.decode("utf-8")
    assert "leaderboard" in html