from fastapi import APIRouter, Depends
from sqlmodel import Session
from ..database import get_db
from ..models import Client

router = APIRouter(prefix="/client",tags=['Client'])

@router.get("/")
def get_all_clients(session: Session= Depends(get_db))->list[Client]:
    return []

@router.get("/{id}" )
def get_client(id:int,session: Session= Depends(get_db)):
    pass

@router.post("/")
def post_client(session: Session= Depends(get_db)):
    pass


@router.patch("/{id}")
def patch_client(id:int,session: Session= Depends(get_db)):
    pass


@router.delete("/{id}")
def delete_client(id:int,session: Session= Depends(get_db)):
    pass