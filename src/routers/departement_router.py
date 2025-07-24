from fastapi import APIRouter, Depends, Query
from sqlmodel import Session
from ..database import get_db
from ..models import Departement, DepartementCreate, DepartementRead, DepartementUpdate
from .. repositories import DepartementRepository

router = APIRouter(prefix="/departement",tags=['Departement'])

@router.get("/", response_model=list[DepartementRead])
def get_all_departements(offset: int = 0, limit: int = Query(default=100, le=100), session: Session= Depends(get_db))->list[Departement]:
    return DepartementRepository(session).get_all_departement(limit, offset)


@router.get("/{id}", response_model=DepartementRead)
def get_departement(id:int, session: Session= Depends(get_db)):
    return DepartementRepository(session).get_departement(id)

@router.post("/", response_model= DepartementRead)
def post_departement(departement = DepartementUpdate, session: Session= Depends(get_db)):
    departement_instance = Departement.model_validate(departement)
    created_departement = DepartementRepository(session).create_departement(departement_instance)
    return created_departement

@router.patch("/{id}")
def patch_departement(id:int, departement = DepartementUpdate, session: Session= Depends(get_db)):
    created_departement = DepartementRepository(session).update_departement(id, **departement.model_dump(exclude_unset=True))
    return created_departement


@router.delete("/{id}")
def delete_departement(id:int,session: Session= Depends(get_db)):
    return DepartementRepository(session).delete_departement(id)