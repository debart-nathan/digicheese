from fastapi import Response
from fastapi.testclient import TestClient

BASE_URL = "/commune"

def test_get_all_communes(client: TestClient):
    result: Response = client.get(f"{BASE_URL}/")
    assert result.status_code == 200
    data = result.json()
    assert isinstance(data, list)
    assert len(data) > 0

def test_get_all_communes_limit(client: TestClient):
    result: Response = client.get(f"{BASE_URL}/?limit=1")
    assert result.status_code == 200
    data = result.json()
    assert isinstance(data, list)
    assert len(data) > 0

def test_get_all_communes_offset(client: TestClient):
    result: Response = client.get(f"{BASE_URL}/?offset=1")
    assert result.status_code == 200
    data = result.json()
    assert isinstance(data, list)
    assert len(data) == 0

def test_get_commune_by_id(client: TestClient):
    result: Response = client.get(f"{BASE_URL}/1")
    assert result.status_code == 200
    data = result.json()
    assert isinstance(data, dict)
    assert len(data) > 0

def test_get_commune_by_id_404(client: TestClient):
    result: Response = client.get(f"{BASE_URL}/100")
    assert result.status_code == 404


def test_create_commune(client: TestClient):
    new_commune = {
        "fk_commune_departement": "59",
        "commune_ville": "La Salvetat-sur-Agout",
        "commune_codepostal": "34293"
    }

    result: Response = client.post(f"{BASE_URL}/", json=new_commune)
    assert result.status_code == 201
    created_commune: dict = result.json()
    assert created_commune["fk_commune_departement"] == "59"
    assert created_commune["commune_ville"] == "La Salvetat-sur-Agout"
    assert created_commune["commune_codepostal"] == "34293"

def test_create_commune_422(client: TestClient):
    new_commune = {
        "commune_ville": "La Salvetat-sur-Agout",
        "commune_codepostal": "34293"
    }

    result: Response = client.post(f"{BASE_URL}/", json=new_commune)
    assert result.status_code == 422

def test_patch_commune(client: TestClient):
    update_commune = {
        "commune_ville" : "Zuid-Wervik",    
    }
    result: Response = client.patch(f"{BASE_URL}/1", json=update_commune)
    assert result.status_code == 200
    data = result.json()
    assert data["commune_ville"] == "Zuid-Wervik"

def test_patch_commune_404(client: TestClient):
    update_commune = {
        "commune_ville" : "Zuid-Wervik"
    }
    result: Response = client.patch(f"{BASE_URL}/1000000", json=update_commune)
    assert result.status_code == 404

def test_delete_commune(client: TestClient):
    result: Response = client.delete(f"{BASE_URL}/1")
    assert result.status_code == 204

def test_delete_commune_404(client: TestClient):
    result: Response = client.delete(f"{BASE_URL}/1000")
    assert result.status_code == 404