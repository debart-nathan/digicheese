from fastapi import APIRouter, Depends
from sqlmodel import Session
from ..database import get_db
from ..models import Commande, CommandeCreate, CommandeRead, CommandeUpdate

router = APIRouter(prefix="/commande",tags=['Commande'])

@router.get("/", response_model=list[CommandeRead])
def get_all_commande(session: Session= Depends(get_db))->list[Commande]:
    return []

@router.get("/{id}", response_model=CommandeRead )
def get_commande(id:int,session: Session= Depends(get_db)):
    pass

@router.post("/")
def post_commande(commande:CommandeCreate,session: Session= Depends(get_db)):
    pass


@router.patch("/{id}")
def patch_commande(id:int,commande:CommandeUpdate,session: Session= Depends(get_db)):
    pass


@router.delete("/{id}")
def delete_commande(id:int,session: Session= Depends(get_db)):
    pass