import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_create_hero():
    response = client.post("/hero/", params={"name": "Batman"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Batman"

def test_get_hero_by_name():
    response = client.get("/hero/", params={"name": "Batman"})
    assert response.status_code == 200
    assert any(hero["name"] == "Batman" for hero in response.json())

def test_get_hero_by_strength():
    response = client.get("/hero/", params={"strength__gte": 50})
    assert response.status_code == 200
    assert all(hero["strength"] >= 50 for hero in response.json())

def test_hero_not_found():
    response = client.post("/hero/", params={"name": "UnknownHeroXYZ"})
    assert response.status_code == 404
