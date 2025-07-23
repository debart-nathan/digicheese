from fastapi import APIRouter, Depends
from sqlmodel import Session
from ..database import get_db
from ..models import Commune

router = APIRouter(prefix="/commune",tags=['Commune'])

@router.get("/")
def get_all_communes(session: Session= Depends(get_db))->list[Commune]:
    return []

@router.get("/{id}" )
def get_commune(id:int,session: Session= Depends(get_db)):
    pass

@router.post("/")
def post_commune(session: Session= Depends(get_db)):
    pass


@router.patch("/{id}")
def patch_commune(id:int,session: Session= Depends(get_db)):
    pass


@router.delete("/{id}")
def delete_commune(id:int,session: Session= Depends(get_db)):
    pass