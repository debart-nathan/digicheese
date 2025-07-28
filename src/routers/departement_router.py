from fastapi import APIRouter, Depends, Query, HTTPException, status
from sqlmodel import Session
from ..database import get_db
from ..models import Departement, DepartementCreate, DepartementRead, DepartementUpdate
from .. repositories import DepartementRepository
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/departement",tags=['Departement'])

@router.get("/", response_model=list[DepartementRead])
def get_all_departements(offset: int = 0, limit: int = Query(default=100, le=100), session: Session= Depends(get_db))->list[Departement]:
    return DepartementRepository(session).get_all_departement(limit, offset)

@router.get("/{id}", response_model=DepartementRead)
def get_departement(id:int, session: Session= Depends(get_db)):
    departement=DepartementRepository(session).get_commande(id)
    if not departement:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"departement :{id} non trouvé")
    return departement

@router.post("/", response_model=DepartementRead,status_code=status.HTTP_201_CREATED)
def post_departement(departement = DepartementUpdate, session: Session= Depends(get_db)):
    departement_instance = Departement.model_validate(departement)
    created_departement = DepartementRepository(session).create_departement(departement_instance)
    return created_departement

@router.patch("/{id}",response_model=DepartementRead)
def patch_departement(id:int, departement = DepartementUpdate, session: Session= Depends(get_db)):
    created_departement = DepartementRepository(session).update_departement(id, **departement.model_dump(exclude_unset=True))
    if not created_departement:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"departement :{id} non trouvé")
    return created_departement


@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_departement(id:int,session: Session= Depends(get_db)):
    departement=DepartementRepository(session).delete_departement(id)
    if not  departement:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"departement:{id} non trouvé")
    return DepartementRepository(session).delete_departement(id)
