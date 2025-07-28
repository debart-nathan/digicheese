from fastapi import APIRouter, Depends, Query
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

    return JSONResponse(content=colis, status_code=200)

@router.post("/", response_model=ColisRead)
def post_colis(colis: ColisCreate, session: Session = Depends(get_db)):
    colis_instance = Colis.model_validate(colis)
    created_colis = ColisRepository(session).create_colis(colis_instance)
    return created_colis


@router.patch("/{id}")
def patch_colis(id:int,colis:ColisUpdate,session: Session= Depends(get_db)):
    created_colis = ColisRepository(session).update_colis(id,**colis.model_dump(exclude_unset=True))
    return created_colis


@router.delete("/{id}")
def delete_colis(id:int,session: Session= Depends(get_db)):
    return ColisRepository(session).delete_colis(id)