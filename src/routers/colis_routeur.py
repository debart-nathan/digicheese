from fastapi import APIRouter, Depends
from sqlmodel import Session
from ..database import get_db
from ..models import Colis, ColisCreate, ColisRead, ColisUpdate

router = APIRouter(prefix="/colis",tags=['Colis'])

@router.get("/", response_model=list[ColisRead])
def get_all_colis(session: Session= Depends(get_db))->list[Colis]:
    return []

@router.get("/{id}", response_model=ColisRead )
def get_colis(id:int,session: Session= Depends(get_db)):
    pass

@router.post("/")
def post_colis(colis:ColisCreate,session: Session= Depends(get_db)):
    pass


@router.patch("/{id}")
def patch_colis(id:int,colis:ColisUpdate,session: Session= Depends(get_db)):
    pass


@router.delete("/{id}")
def delete_colis(id:int,session: Session= Depends(get_db)):
    pass