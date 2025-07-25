from fastapi import APIRouter, Depends, Query, HTTPException, status
from sqlmodel import Session
from ..database import get_db
from ..models import DetailColis, DetailColisCreate, DetailColisRead, DetailColisUpdate
from ..repositories import DetailColisRepository

router = APIRouter(prefix="/detail_colis",tags=['DetailColis'])

@router.get("/", response_model=list[DetailColisRead])
def get_all_detail_colis(offset: int = 0, limit: int = Query(default=100, le=100),session: Session= Depends(get_db))->list[DetailColis]:
    return DetailColisRepository(session).get_all_detail_colis(limit,offset)

@router.get("/{id}", response_model=DetailColisRead )
def get_detail_colis(id:int,session: Session= Depends(get_db)):
    detail_colis= DetailColisRepository(session).get_detail_colis(id)
    if not detail_colis:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Detail Colis: {id} non trouvé")
    return detail_colis

@router.post("/", response_model=DetailColisRead,status_code=status.HTTP_201_CREATED)
def post_detail_colis(detail_colis: DetailColisCreate, session: Session = Depends(get_db)):
    detail_colis_instance = DetailColis.model_validate(detail_colis)
    created_detail_colis = DetailColisRepository(session).create_detail_colis(detail_colis_instance)
    return created_detail_colis


@router.patch("/{id}")
def patch_detail_colis(id:int,detail_colis:DetailColisUpdate,session: Session= Depends(get_db)):
    created_detail_colis = DetailColisRepository(session).update_detail_colis(id,**detail_colis.model_dump(exclude_unset=True))
    if not created_detail_colis:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Detail Colis: {id} non trouvé")
    return created_detail_colis


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_detail_colis(id:int,session: Session= Depends(get_db)):
    result: bool = DetailColisRepository(session).delete_detail_colis(id)
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Detail Colis: {id} non trouvé")
    return {"ok": True}