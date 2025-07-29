from fastapi import Response
from fastapi.testclient import TestClient
from decimal import Decimal

BASE_URL = "/variation_objet"

def test_get_all_variation_objets(client: TestClient):
    result: Response = client.get(f"{BASE_URL}/")
    assert result.status_code == 200
    data = result.json()
    assert isinstance(data, list)

def test_get_variation_objet_by_id(client: TestClient):
    result: Response = client.get(f"{BASE_URL}/1")
    assert result.status_code == 200
    data = result.json()
    assert "variation_objet_id" in data
    assert "variation_objet_poids" in data

def test_get_variation_objet_by_id_404(client: TestClient):
    result: Response = client.get(f"{BASE_URL}/9999")
    assert result.status_code == 404

def test_create_variation_objet(client: TestClient):
    new_variation = {
        "variation_objet_taille": "Grande",
        "variation_objet_poids": "1.25",
        "fk_variation_objet_objet_id": 1
    }
    result: Response = client.post(BASE_URL + "/", json=new_variation)
    assert result.status_code == 201
    created = result.json()
    assert created["variation_objet_taille"] == "Grande"
    assert Decimal(created["variation_objet_poids"]) == Decimal("1.25")
    assert created["fk_variation_objet_objet_id"] == 1

def test_create_variation_objet_default_taille(client: TestClient):
    new_variation = {
        "variation_objet_poids": "0.500",
        "fk_variation_objet_objet_id": 1
    }
    result: Response = client.post(BASE_URL + "/", json=new_variation)
    assert result.status_code == 201
    data = result.json()
    assert data["variation_objet_taille"] is None
    assert Decimal(data["variation_objet_poids"]) == Decimal("0.500")

def test_patch_variation_objet(client: TestClient):
    update_data = {
        "variation_objet_poids": "3.000"
    }
    result: Response = client.patch(f"{BASE_URL}/1", json=update_data)
    assert result.status_code == 200
    updated = result.json()
    assert Decimal(updated["variation_objet_poids"]) == Decimal("3.000")

def test_patch_variation_objet_404(client: TestClient):
    update_data = {
        "variation_objet_taille": "Fantôme"
    }
    result: Response = client.patch(f"{BASE_URL}/9999", json=update_data)
    assert result.status_code == 404

def test_delete_variation_objet(client: TestClient):
    result = client.delete(f"{BASE_URL}/1")
    assert result.status_code == 204

    result = client.get(f"{BASE_URL}/1")
    assert result.status_code == 404

def test_delete_variation_objet_404(client: TestClient):
    result = client.delete(f"{BASE_URL}/9999")
    assert result.status_code == 404
