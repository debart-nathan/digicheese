from fastapi import APIRouter, Depends, Query
from sqlmodel import Session
from ..database import get_db
from ..models import Client, ClientCreate, ClientUpdate, ClientRead
from ..repositories import ClientRepository

router = APIRouter(prefix="/client",tags=['Client'])

@router.get("/", response_model=list[ClientRead])
def get_all_clients(offset: int = 0, limit: int = Query(default=100, le=100),session: Session= Depends(get_db))->list[Client]:
    return ClientRepository(session).get_all_clients(limit, offset)

@router.get("/{id}", response_model=ClientRead)
def get_client(id:int, session: Session= Depends(get_db)):
    return ClientRepository(session).get_client(id)

@router.post("/", response_model=ClientRead)
def post_client(client: ClientCreate, session: Session= Depends(get_db)):
    client_instance = Client.model_validate(client)
    created_client = ClientRepository(session).create_client(client_instance)
    return created_client


@router.patch("/{id}", response_model=ClientRead)
def patch_client(id:int, client: ClientUpdate, session: Session= Depends(get_db)):
    created_client = ClientRepository(session).update_client(id,**client.model_dump(exclude_unset=True))
    return created_client


@router.delete("/{id}")
def delete_client(id:int, session: Session= Depends(get_db)):
    return ClientRepository(session).delete_client(id)