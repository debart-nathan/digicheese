from fastapi import APIRouter, Depends, Query
from sqlmodel import Session
from ..database import get_db
from ..models import DetailCommande, DetailCommandeCreate, DetailCommandeRead, DetailCommandeUpdate
from ..repositories import DetailCommandeRepository

router = APIRouter(prefix="/detail_commande",tags=['DetailCommande'])

@router.get("/", response_model=list[DetailCommandeRead])
def get_all_detail_commande(offset: int = 0, limit: int = Query(default=100, le=100),session: Session= Depends(get_db))->list[DetailCommande]:
    return DetailCommandeRepository(session).get_all_detail_commandes(limit,offset)

@router.get("/{id}", response_model=DetailCommandeRead )
def get_detail_commande(id:int,session: Session= Depends(get_db)):
    return DetailCommandeRepository(session).get_detail_commande(id)

@router.post("/", response_model=DetailCommandeRead)
def post_detail_commande(detail_commande: DetailCommandeCreate, session: Session = Depends(get_db)):
    detail_commande_instance = DetailCommande.model_validate(detail_commande)
    created_detail_commande = DetailCommandeRepository(session).create_detail_commande(detail_commande_instance)
    return created_detail_commande


@router.patch("/{id}")
def patch_detail_commande(id:int,detail_commande:DetailCommandeUpdate,session: Session= Depends(get_db)):
    created_detail_commande = DetailCommandeRepository(session).update_detail_commande(id,**detail_commande.model_dump(exclude_unset=True))
    return created_detail_commande


@router.delete("/{id}")
def delete_detail_commande(id:int,session: Session= Depends(get_db)):
    return DetailCommandeRepository(session).delete_detail_commande(id)