from fastapi.testclient import TestClient

from src.app.main import app

client = TestClient(app)


def test_home():

    response = client.get("/")

    assert response.status_code == 200


def test_create_user():

    response = client.post(
        "/users/create",
        json={
            "name": "Ana Rita",
            "agency": "0013",
            "account": "56789",
            "current_balance": 1000
        }
    )

    assert response.status_code == 201
    assert response.json()["name"] == "Ana Rita"


def test_get_user():

    client.post(
        "/users/create",
        json={
            "name": "Maria",
            "agency": "0013",
            "account": "11111",
            "current_balance": 500
        }
    )

    response = client.get("/users/11111")

    assert response.status_code == 200
    assert response.json()["account"] == "11111"
    
def test_get_transactions():

    client.post(
        "/users/create",
        json={
            "name": "Ana Rita",
            "agency": "0013",
            "account": "99999",
            "current_balance": 1000
        }
    )

    client.post(
        "/users/deposit",
        json={
            "account": "99999",
            "value": 100
        }
    )

    response = client.get(
        "/users/99999/transactions"
    )

    assert response.status_code == 200
    assert len(response.json()["all_transactions"]) == 1