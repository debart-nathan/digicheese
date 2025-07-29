from fastapi import Response
from fastapi.testclient import TestClient

BASE_URL = "/detail_colis"

def test_get_all_detail_colis(client: TestClient):
    result: Response = client.get(f"{BASE_URL}/")
    assert result.status_code == 200
    data = result.json()
    assert isinstance(data, list)
    assert len(data) > 0

def test_get_all_detail_colis_limit(client: TestClient):
    result: Response = client.get(f"{BASE_URL}/?limit=1")
    assert result.status_code == 200
    data = result.json()
    assert isinstance(data, list)
    assert len(data) > 0

def test_get_all_detail_colis_offset(client: TestClient):
    result: Response = client.get(f"{BASE_URL}/?offset=1")
    assert result.status_code == 200
    data = result.json()
    assert isinstance(data, list)
    assert len(data) == 0

def test_get_detail_colis_by_id(client: TestClient):
    result: Response = client.get(f"{BASE_URL}/1")
    assert result.status_code == 200
    data = result.json()
    assert isinstance(data, dict)
    assert len(data) > 0
    assert data["detail_colis_quantitee"] == 4

def test_get_detail_colis_by_id_404(client: TestClient):
    result: Response = client.get(f"{BASE_URL}/100")
    assert result.status_code == 404

def test_create_detail_colis(client: TestClient):
    new_detail_colis= {
        "detail_colis_quantitee": 50,
        "detail_colis_commentaire": "Penser à racheter des t-shirts"
    }

    result: Response = client.post(f"{BASE_URL}/", json=new_detail_colis)
    assert result.status_code == 201
    created_detail_colis: dict = result.json()
    assert created_detail_colis["detail_colis_quantitee"] == 50
    assert created_detail_colis["detail_colis_commentaire"] == "Penser à racheter des t-shirts"

def test_create_detail_colis_blank(client: TestClient):
    new_detail_colis= {}

    result: Response = client.post(f"{BASE_URL}/", json=new_detail_colis)
    assert result.status_code == 201

def test_patch_detail_colis(client: TestClient):
    update_detail_colis = {
        "detail_colis_commentaire" : "Ce n'est plus une simple commande",    
    }
    result: Response = client.patch(f"{BASE_URL}/1", json=update_detail_colis)
    assert result.status_code == 200
    data = result.json()
    assert data["detail_colis_commentaire"] == "Ce n'est plus une simple commande"
    assert data["detail_colis_quantitee"] == 4

def test_patch_detail_colis_404(client: TestClient):
    update_detail_colis = {
        "detail_colis_commentaire" : "Ce n'est plus une simple commande",    
    }
    result: Response = client.patch(f"{BASE_URL}/1000000", json=update_detail_colis)
    assert result.status_code == 404

def test_delete_detail_colis(client: TestClient):
    result: Response = client.delete(f"{BASE_URL}/1")
    assert result.status_code == 204
    result_alt: Response = client.get(f"{BASE_URL}/1")
    assert result_alt.status_code == 404

def test_delete_detail_colis_404(client: TestClient):
    result: Response = client.delete(f"{BASE_URL}/1000")
    assert result.status_code == 404