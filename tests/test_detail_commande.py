from fastapi import Response
from fastapi.testclient import TestClient

BASE_URL = "/detail_commande"

def test_get_all_detail_commandes(client: TestClient):
    result: Response = client.get(f"{BASE_URL}/")
    assert result.status_code == 200
    data = result.json()
    assert isinstance(data, list)
    assert len(data) > 0


def test_get_detail_commande_by_id(client: TestClient):
    result: Response = client.get(f"{BASE_URL}/1")
    assert result.status_code == 200
    created_detail_commande:dict = result.json()
    assert created_detail_commande["detail_commande_quantitee"] == 25


def test_get_detail_commande_by_id_404(client: TestClient):
    result: Response = client.get(f"{BASE_URL}/300")
    assert result.status_code == 404

def test_create_detail_commande(client: TestClient):
    new_detail = {
        "detail_commande_quantitee": 3,
    }
    result: Response = client.post(f"{BASE_URL}/", json=new_detail)
    assert result.status_code == 201
    created_detail: dict = result.json()
    assert created_detail["detail_commande_quantitee"] == 3


def test_patch_detail_commande(client: TestClient):
    new_detail = {
        "detail_commande_quantitee": 1,

    }
    create_result = client.post(f"{BASE_URL}/", json=new_detail)
    detail_commande = create_result.json()
    assert detail_commande["detail_commande_quantitee"]== 1

def test_patch_detail_commande(client: TestClient):
    update_data = {
        "detail_commande_quantitee": 5
    }
    result: Response = client.patch(f"{BASE_URL}/1", json=update_data)
    assert result.status_code == 200
    updated_detail: dict = result.json()
    assert updated_detail["detail_commande_quantitee"] == 5


def test_patch_detail_commande_404(client: TestClient):
    update_detail_commandecommande = {
        "detail_commande_quantitee": 5
    }
    result: Response = client.patch(f"{BASE_URL}/5555", json=update_detail_commandecommande)
    assert result.status_code == 404

def test_delete_detail_commande(client: TestClient):
    result: Response = client.delete(f"{BASE_URL}/1")
    assert result.status_code == 204
    result = client.get(f"{BASE_URL}/1")
    assert result.status_code == 404

def test_delete_detail_commande_404(client: TestClient):
    result: Response = client.delete(f"{BASE_URL}/3000")
    assert result.status_code == 404