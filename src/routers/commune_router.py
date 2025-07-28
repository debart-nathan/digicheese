from fastapi import APIRouter, Depends, Query, HTTPException,status
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
    commune=CommuneRepository(session).get_commande(id)
    if not commune:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"commune :{id} non trouvé")
    return commune

@router.post("/", response_model=CommuneRead, status_code=status.HTTP_201_CREATED)
def post_commune(commune: CommuneCreate, session: Session = Depends(get_db)):
    commune_instance = Commune.model_validate(commune)
    created_commune = CommuneRepository(session).create_commune(commune_instance)
    return created_commune


@router.patch("/{id}",response_model=CommuneRead)
def patch_commune(id:int,commune:CommuneUpdate,session: Session= Depends(get_db)):
    created_commune = CommuneRepository(session).update_commune(id,**commune.model_dump(exclude_unset=True))
    if not created_commune:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"commune :{id} non trouvé")
    return created_commune


@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_commune(id:int,session: Session= Depends(get_db)):
    commune=CommuneRepository(session).delete_commune(id)
    if not commune:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"commune:{id} non trouvé")
    return commune