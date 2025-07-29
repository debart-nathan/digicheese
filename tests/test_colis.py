from fastapi import Response
from fastapi.testclient import TestClient

BASE_URL = "/colis"

def test_get_all_colis(client: TestClient):
    result: Response = client.get(f"{BASE_URL}/")
    assert result.status_code == 200
    data = result.json()
    assert isinstance(data, list)
    assert len(data) > 0

def test_get_all_colis_limit(client: TestClient):
    result: Response = client.get(f"{BASE_URL}/?limit=1")
    assert result.status_code == 200
    data = result.json()
    assert isinstance(data, list)
    assert len(data) > 0

def test_get_all_colis_offset(client: TestClient):
    result: Response = client.get(f"{BASE_URL}/?offset=1")
    assert result.status_code == 200
    data = result.json()
    assert isinstance(data, list)
    assert len(data) == 0

def test_get_colis_by_id(client: TestClient):
    result: Response = client.get(f"{BASE_URL}/1")
    assert result.status_code == 200
    data = result.json()
    assert isinstance(data, dict)
    assert len(data) > 0
    assert data["colis_code_suivi"] == "1445"

def test_get_colis_by_id_404(client: TestClient):
    result: Response = client.get(f"{BASE_URL}/100")
    assert result.status_code == 404

def test_create_colis(client: TestClient):
    new_colis = {
        "colis_code_suivi": "5551", 
        "colis_timbre": "5.02", 
        "colis_commentaire": "Colis perdu"}
    result: Response = client.post(f"{BASE_URL}/", json=new_colis)
    assert result.status_code == 201
    created_colis: dict = result.json()
    assert created_colis["colis_code_suivi"] == "5551"
    assert created_colis["colis_timbre"] == 5.02
    assert created_colis["colis_commentaire"] == "Colis perdu"

def test_create_commune_blank(client: TestClient):
    new_colis = {}
    result: Response = client.post(f"{BASE_URL}/", json=new_colis)
    assert result.status_code == 201

def test_patch_colis(client: TestClient):
    update_colis = {
        "colis_commentaire" : "Colis envoyer à la mauvaise adresse",    
    }
    result: Response = client.patch(f"{BASE_URL}/1", json=update_colis)
    assert result.status_code == 200
    data = result.json()
    assert data["colis_commentaire"] == "Colis envoyer à la mauvaise adresse"
    assert data["colis_code_suivi"] == "1445"

def test_patch_colis_404(client: TestClient):
    update_colis = {
        "colis_commentaire" : "Colis envoyer à la mauvaise adresse",    
    }
    result: Response = client.patch(f"{BASE_URL}/1000000", json=update_colis)
    assert result.status_code == 404

def test_delete_colis(client: TestClient):
    result: Response = client.delete(f"{BASE_URL}/1")
    assert result.status_code == 204
    result_alt: Response = client.get(f"{BASE_URL}/1")
    assert result_alt.status_code == 404

def test_delete_colis_404(client: TestClient):
    result: Response = client.delete(f"{BASE_URL}/1000")
    assert result.status_code == 404