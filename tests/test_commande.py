from fastapi import Response
from fastapi.testclient import TestClient
import datetime

BASE_URL = "/commande"

def test_get_all_commandes(client: TestClient):
    result: Response = client.get(f"{BASE_URL}/")
    assert result.status_code == 200
    data = result.json()
    assert isinstance(data, list)
    assert len(data) > 0

def test_get_all_commandes_limit(client: TestClient):
    result: Response = client.get(f"{BASE_URL}/?limit=1")
    assert result.status_code == 200
    data = result.json()
    assert isinstance(data, list)
    assert len(data) > 0

def test_get_all_commandes_offset(client: TestClient):
    result: Response = client.get(f"{BASE_URL}/?offset=1")
    assert result.status_code == 200
    data = result.json()
    assert isinstance(data, list)
    assert len(data) == 0

def test_get_commande_by_id(client: TestClient):
    result: Response = client.get(f"{BASE_URL}/1")
    assert result.status_code == 200
    data = result.json()
    assert isinstance(data, dict)
    assert len(data) > 0
    assert data["client_cheque"] == 20.0

def test_get_commande_by_id_404(client: TestClient):
    result: Response = client.get(f"{BASE_URL}/100")
    assert result.status_code == 404

def test_create_commande(client: TestClient):
    new_commande = {
        "commande_date": "2025-12-12",
        "client_timbre": "80",
        "commande_timbre": "50.2",
        "client_cheque": "74.5",
        "commande_commentaire" : "Erreur de calcul"
    }

    result: Response = client.post(f"{BASE_URL}/", json=new_commande)
    assert result.status_code == 201
    created_commande: dict = result.json()
    assert created_commande["client_timbre"] == 80
    assert created_commande["commande_timbre"] == 50.2
    assert created_commande["client_cheque"] == 74.5
    assert created_commande["commande_commentaire"] == "Erreur de calcul"
    assert created_commande["commande_date"] == "2025-12-12"

def test_create_commande_blank(client: TestClient):
    new_commande = {}
    result: Response = client.post(f"{BASE_URL}/", json=new_commande)
    assert result.status_code == 201


def test_patch_commande(client: TestClient):
    update_commande = {
        "commande_commentaire" : "Appeler la Poste",    
    }
    result: Response = client.patch(f"{BASE_URL}/1", json=update_commande)
    assert result.status_code == 200
    data = result.json()
    assert data["commande_commentaire"] == "Appeler la Poste"
    assert data["client_cheque"] == 20.0

def test_patch_commande_404(client: TestClient):
    update_commande = {
        "commande_commentaire" : "Appeler la Poste",    
    }
    result: Response = client.patch(f"{BASE_URL}/1000000", json=update_commande)
    assert result.status_code == 404

def test_delete_commande(client: TestClient):
    result: Response = client.delete(f"{BASE_URL}/1")
    assert result.status_code == 204
    result_alt: Response = client.get(f"{BASE_URL}/1")
    assert result_alt.status_code == 404

def test_delete_commande_404(client: TestClient):
    result: Response = client.delete(f"{BASE_URL}/1000")
    assert result.status_code == 404