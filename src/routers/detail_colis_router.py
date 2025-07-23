from fastapi import APIRouter, Depends
from sqlmodel import Session
from ..database import get_db
from ..models import DetailColis

router = APIRouter(prefix="/detail_colis",tags=['DetailColis'])

@router.get("/")
def get_all_detail_colis(session: Session= Depends(get_db))->list[DetailColis]:
    return []

@router.get("/{id}" )
def get_detail_colis(id:int,session: Session= Depends(get_db)):
    pass

@router.post("/")
def post_detail_colis(session: Session= Depends(get_db)):
    pass


@router.patch("/{id}")
def patch_detail_colis(id:int,session: Session= Depends(get_db)):
    pass


@router.delete("/{id}")
def delete_detail_colis(id:int,session: Session= Depends(get_db)):
    pass