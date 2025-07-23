from fastapi import APIRouter, Depends
from sqlmodel import Session
from ..database import get_db
from ..models import DetailCommande

router = APIRouter(prefix="/detailcommande",tags=['DetailCommande'])

@router.get("/")
def get_all_detailcommandes(session: Session= Depends(get_db))->list[DetailCommande]:
    return []

@router.get("/{id}" )
def get_detailcommande(id:int,session: Session= Depends(get_db)):
    pass

@router.post("/")
def post_detailcommande(session: Session= Depends(get_db)):
    pass


@router.patch("/{id}")
def patch_detailcommande(id:int,session: Session= Depends(get_db)):
    pass


@router.delete("/{id}")
def delete_detailcommande(id:int,session: Session= Depends(get_db)):
    pass