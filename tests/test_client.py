from fastapi import Response
from fastapi.testclient import TestClient

BASE_URL = "/client"

def test_get_all_clients(client: TestClient):
    result: Response = client.get(f"{BASE_URL}/")
    assert result.status_code == 200
    data = result.json()
    assert isinstance(data, list)
    assert len(data) == 2

def test_get_all_clients_limit(client: TestClient):
    result: Response = client.get(f"{BASE_URL}/?offset=0&limit=1")
    assert result.status_code == 200
    data = result.json()
    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0]["client_prenom"] == "Robin"

def test_get_all_clients_offset(client: TestClient):
    result: Response = client.get(f"{BASE_URL}/?offset=1")
    assert result.status_code == 200
    data = result.json()
    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0]["client_prenom"] == "Daniel"

def test_get_client_by_id(client: TestClient):
    result: Response = client.get(f"{BASE_URL}/1")
    assert result.status_code == 200
    data = result.json()
    assert data["client_prenom"] == "Robin"

def test_get_client_by_id_404(client: TestClient):
    result: Response = client.get(f"{BASE_URL}/10000000")
    assert result.status_code == 404


def test_create_client(client: TestClient):
    new_client = {
        "client_prenom": "john",
        "client_nom": "doe",
        "client_adresse1": "123 Main St",
        "client_newsletter": 1
    }
    result: Response = client.post(f"{BASE_URL}", json=new_client)
    assert result.status_code == 201
    created_client: dict = result.json()
    assert created_client["client_prenom"] == "John"
    assert created_client["client_nom"] == "DOE"
    assert created_client["client_adresse1"] == "123 Main St"
    assert created_client["client_newsletter"] == True

def test_create_client_400_missing_fields(client: TestClient):
    incomplete_client = {
        "client_nom": "Doe"
    }
    result = client.post("/client", json=incomplete_client)
    assert result.status_code == 400


def test_create_client_400_email(client: TestClient):
    new_client = {
        "client_prenom": "john",
        "client_nom": "doe",
        "client_adresse1": "123 Main St",
        "client_email": "error",
        "client_newsletter": 1
    }
    result: Response = client.post(f"{BASE_URL}", json=new_client)
    assert result.status_code == 400

def test_patch_client(client: TestClient):
    update_client = {
        "client_newsletter": 0
    }
    result: Response = client.patch(f"{BASE_URL}/1", json=update_client)
    assert result.status_code == 200
    data = result.json()
    assert data["client_prenom"] == "Robin"
    assert data["client_newsletter"] == 0

def test_patch_client_400_invalid_email(client: TestClient):
    update_data = {
        "client_email": "invalid-email"
    }
    result = client.patch("/client/2", json=update_data)
    assert result.status_code == 400

def test_patch_404(client: TestClient):
    update_data = {
        "client_prenom": "Ghost"
    }
    result = client.patch("/client/9999", json=update_data)
    assert result.status_code == 404



def test_delete_client(client: TestClient):
    result: Response = client.delete(f"{BASE_URL}/1")
    assert result.status_code == 204  

    result = client.get(f"{BASE_URL}/1")
    assert result.status_code == 404  

def test_delete_404(client: TestClient):
    result = client.delete("/client/9999")
    assert result.status_code == 404
