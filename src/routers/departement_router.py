from fastapi import APIRouter, Depends
from sqlmodel import Session
from ..database import get_db
from ..models import Departement

router = APIRouter(prefix="/departement",tags=['Departement'])

@router.get("/")
def get_all_departements(session: Session= Depends(get_db))->list[Departement]:
    return []

@router.get("/{id}" )
def get_departement(id:int,session: Session= Depends(get_db)):
    pass

@router.post("/")
def post_departement(session: Session= Depends(get_db)):
    pass


@router.patch("/{id}")
def patch_departement(id:int,session: Session= Depends(get_db)):
    pass


@router.delete("/{id}")
def delete_departement(id:int,session: Session= Depends(get_db)):
    pass