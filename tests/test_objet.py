from fastapi import Response
from fastapi.testclient import TestClient

BASE_URL = "/objet"

def test_get_all_objets(client: TestClient):
    result: Response = client.get(f"{BASE_URL}/")
    assert result.status_code == 200
    data = result.json()
    assert isinstance(data, list)

def test_get_objet_by_id(client: TestClient):
    result: Response = client.get(f"{BASE_URL}/1")
    assert result.status_code == 200
    data = result.json()
    assert "objet_id" in data
    assert "objet_libelee" in data

def test_get_objet_by_id_404(client: TestClient):
    result: Response = client.get(f"{BASE_URL}/9999")
    assert result.status_code == 404

def test_create_objet(client: TestClient):
    new_objet = {
        "objet_libelee": "Epée magique",
        "objet_points": 50
    }
    result: Response = client.post(BASE_URL + "/", json=new_objet)
    assert result.status_code == 201
    created_objet = result.json()
    assert created_objet["objet_libelee"] == "Epée magique"
    assert created_objet["objet_points"] == 50

def test_create_objet_default_points(client: TestClient):
    new_objet = {
        "objet_libelee": "Potion"
    }
    result = client.post(BASE_URL + "/", json=new_objet)
    assert result.status_code == 201
    data = result.json()
    assert data["objet_points"] == 0  # Default value

def test_patch_objet(client: TestClient):
    update_data = {
        "objet_points": 100
    }
    result = client.patch(f"{BASE_URL}/1", json=update_data)
    assert result.status_code == 200
    data = result.json()
    assert data["objet_points"] == 100

def test_patch_objet_404(client: TestClient):
    update_data = {
        "objet_libelee": "Fantôme"
    }
    result = client.patch(f"{BASE_URL}/9999", json=update_data)
    assert result.status_code == 404

def test_delete_objet(client: TestClient):
    result = client.delete(f"{BASE_URL}/1")
    assert result.status_code == 204

    result = client.get(f"{BASE_URL}/1")
    assert result.status_code == 404

def test_delete_objet_404(client: TestClient):
    result = client.delete(f"{BASE_URL}/9999")
    assert result.status_code == 404
