from fastapi import APIRouter, Depends
from sqlmodel import Session
from ..database import get_db
from ..models import Client, ClientCreate, ClientUpdate, ClientRead

router = APIRouter(prefix="/client",tags=['Client'])

@router.get("/")
def get_all_clients(client: ClientRead, session: Session= Depends(get_db))->list[ClientRead]:
    return []

@router.get("/{id}" )
def get_client(id:int, client: ClientRead, session: Session= Depends(get_db)):
    pass

@router.post("/")
def post_client(client: ClientCreate, session: Session= Depends(get_db)):
    pass


@router.patch("/{id}")
def patch_client(id:int, client: ClientUpdate, session: Session= Depends(get_db)):
    pass


@router.delete("/{id}")
def delete_client(id:int, session: Session= Depends(get_db)):
    pass