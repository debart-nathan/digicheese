from fastapi import APIRouter, Depends
from sqlmodel import Session
from ..database import get_db
from ..models import Commande

router = APIRouter(prefix="/commande",tags=['Commande'])

@router.get("")
def get_commandes(session: Session= Depends(get_db))->list[Commande]:
    return []

@router.get("/{id}" )
def get_commande(id:int,session: Session= Depends(get_db)):
    pass

@router.post("")
def post_commande(session: Session= Depends(get_db)):
    pass


@router.patch("/{id}")
def patch_commande(id:int,session: Session= Depends(get_db)):
    pass


@router.delete("/{id}")
def delete_commande(id:int,session: Session= Depends(get_db)):
    pass