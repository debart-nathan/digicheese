from fastapi import APIRouter, Depends
from sqlmodel import Session
from ..database import get_db
from ..models import DetailColis, DetailColisCreate, DetailColisRead, DetailColisUpdate

router = APIRouter(prefix="/detail-colis",tags=['DetailColis'])

@router.get("/", response_model=list[DetailColisRead])
def get_all_detail_colis(session: Session= Depends(get_db))->list[DetailColis]:
    return []

@router.get("/{id}", response_model=DetailColisRead )
def get_detail_colis(id:int,session: Session= Depends(get_db)):
    pass

@router.post("/")
def post_detail_colis(detail_colis:DetailColisCreate,session: Session= Depends(get_db)):
    pass


@router.patch("/{id}")
def patch_detail_colis(id:int,detail_colis:DetailColisUpdate,session: Session= Depends(get_db)):
    pass


@router.delete("/{id}")
def delete_detail_colis(id:int,session: Session= Depends(get_db)):
    pass