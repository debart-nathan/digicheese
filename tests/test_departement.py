from fastapi import Response
from fastapi.testclient import TestClient

BASE_URL = "/departement"

def test_get_all_departements(client: TestClient):
    result: Response = client.get(f"{BASE_URL}/")
    assert result.status_code == 200
    data = result.json()
    assert isinstance(data, list)
    assert len(data) > 0
    
def test_get_departement_by_id(client: TestClient):
    result: Response = client.get(f"{BASE_URL}/59")
    assert result.status_code == 200
    data = result.json()
    assert data["departement_nom"] == "Nord"

def test_create_departement(client: TestClient):
    new_departement = {
        "departement_nom": "Rhone",
        "departement_code": "69"

    }
    result: Response = client.post(f"{BASE_URL}/", json=new_departement)
    assert result.status_code == 201
    created_departement: dict = result.json()
    assert created_departement["departement_nom"] == "Rhone"
    assert created_departement["departement_code"] == "69"


def test_patch_departement(client: TestClient):
    new_departement = {
    "departement_nom": "Rhone"
    }
    result: Response = client.patch(f"{BASE_URL}/59", json=new_departement)
    assert result.status_code == 200
    updated_departement: dict= result.json()
    assert updated_departement["departement_nom"]=="Rhone"
  

def test_delete_departement(client: TestClient):
    result:Response= client.delete(f"{BASE_URL}/83")
    assert result.status_code == 204
    result: Response = client.get(f"{BASE_URL}/83")
    assert result.status_code == 404

def test_delete_departement_404(client: TestClient):
    result:Response= client.delete(f"{BASE_URL}/64")
    assert result.status_code == 404


def test_get_departement_by_id_404(client: TestClient):
    result: Response = client.get(f"{BASE_URL}/999999")
    assert result.status_code == 404
    
    


    
    