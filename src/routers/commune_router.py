from fastapi import APIRouter, Depends, Query
from sqlmodel import Session
from ..database import get_db
from ..models import Commune, CommuneCreate, CommuneRead, CommuneUpdate
from ..repositories import CommuneRepository

router = APIRouter(prefix="/commune",tags=['Commune'])

@router.get("/", response_model=list[CommuneRead])
def get_all_commune(offset: int = 0, limit: int = Query(default=100, le=100),session: Session= Depends(get_db))->list[Commune]:
    return CommuneRepository(session).get_all_communes(limit,offset)

@router.get("/{id}", response_model=CommuneRead )
def get_commune(id:int,session: Session= Depends(get_db)):
    return CommuneRepository(session).get_commune(id)

@router.post("/", response_model=CommuneRead)
def post_commune(commune: CommuneCreate, session: Session = Depends(get_db)):
    commune_instance = Commune.model_validate(commune)
    created_commune = CommuneRepository(session).create_commune(commune_instance)
    return created_commune


@router.patch("/{id}")
def patch_commune(id:int,commune:CommuneUpdate,session: Session= Depends(get_db)):
    created_commune = CommuneRepository(session).update_commune(id,**commune.model_dump(exclude_unset=True))
    return created_commune


@router.delete("/{id}")
def delete_commune(id:int,session: Session= Depends(get_db)):
    return CommuneRepository(session).delete_commune(id)