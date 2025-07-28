from fastapi import APIRouter, Depends, Query, HTTPException, status
from sqlmodel import Session
from ..database import get_db
from ..models import Colis, ColisCreate, ColisRead, ColisUpdate
from ..repositories import ColisRepository
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/colis",tags=['Colis'])

@router.get("/", response_model=list[ColisRead])
def get_all_colis(offset: int = 0, limit: int = Query(default=100, le=100),session: Session= Depends(get_db))->list[Colis]:
    return ColisRepository(session).get_all_colis(limit,offset)

@router.get("/{id}", response_model=ColisRead )
def get_colis(id:int,session: Session= Depends(get_db)):
    colis=ColisRepository(session).get_colis(id)
    if not colis:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"colis :{id} non trouvé")
    return colis


@router.post("/", response_model=ColisRead,status_code=status.HTTP_201_CREATED)
def post_colis(colis: ColisCreate, session: Session = Depends(get_db)):
    colis_instance = Colis.model_validate(colis)
    created_colis = ColisRepository(session).create_colis(colis_instance)
    return created_colis


@router.patch("/{id}",response_model=ColisRead)
def patch_colis(id:int,colis:ColisUpdate,session: Session= Depends(get_db)):
    created_colis = ColisRepository(session).update_colis(id,**colis.model_dump(exclude_unset=True))
    if not created_colis:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"colis :{id} non trouvé")
    return created_colis

@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_colis(id:int,session: Session= Depends(get_db)):
    colis=ColisRepository(session).delete_colis(id)
    if not  Colis:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"colis:{id} non trouvé")
    return ColisRepository(session).delete_colis(id)