from fastapi import APIRouter
from ..models.commande import Commande

router = APIRouter(prefix="/commande",tags=['Commande'])

@router.get("")
def get_commandes()->list[Commande]:
    return []

@router.get("/{id}")
def get_commande(id:int):
    pass

@router.post("")
def post_commande():
    pass


@router.patch("/{id}")
def patch_commande(id:int):
    pass


@router.delete("/{id}")
def delete_commande(id:int):
    pass