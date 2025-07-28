from fastapi import APIRouter, Depends, Query, HTTPException,status
from sqlmodel import Session
from ..database import get_db
from ..models import Commande, CommandeCreate, CommandeRead, CommandeUpdate
from ..repositories import CommandeRepository
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/commande",tags=['Commande'])

@router.get("/", response_model=list[CommandeRead])
def get_all_commande(offset: int = 0, limit: int = Query(default=100, le=100),session: Session= Depends(get_db))->list[Commande]:
    return CommandeRepository(session).get_all_commandes(limit,offset)

@router.get("/{id}", response_model=CommandeRead )
def get_commande(id:int,session: Session= Depends(get_db)):
    commande=CommandeRepository(session).get_commande(id)
    if not commande:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"commande :{id} non trouvé")
    return commande

@router.post("/", response_model=CommandeRead,status_code=status.HTTP_201_CREATED)
def post_commande(commande: CommandeCreate, session: Session = Depends(get_db)):
    commande_instance = Commande.model_validate(commande)
    created_commande = CommandeRepository(session).create_commande(commande_instance)
    return created_commande


@router.patch("/{id}",response_model=CommandeRead)
def patch_commande(id:int,commande:CommandeUpdate,session: Session= Depends(get_db)):
    created_commande = CommandeRepository(session).update_commande(id,**commande.model_dump(exclude_unset=True))
    if not created_commande:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"commande :{id} non trouvé")
    return created_commande


@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_commande(id:int,session: Session= Depends(get_db)):
    commande=CommandeRepository(session).delete_commande(id)
    if not  commande:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"commade:{id} non trouvé")
    return commande