from fastapi import APIRouter, Depends, Query, HTTPException, status
from sqlmodel import Session
from ..database import get_db
from ..models import Client, ClientCreate, ClientUpdate, ClientRead
from ..services import ClientService

router = APIRouter(prefix="/client",tags=['Client'])

@router.get("/", response_model=list[ClientRead])
def get_all_clients(offset: int = 0, limit: int = Query(default=100, le=100),session: Session= Depends(get_db))->list[ClientRead]:
    return ClientService(session).get_all(limit, offset)

@router.get("/{id}", response_model=ClientRead)
def get_client(id:int, session: Session= Depends(get_db)):
    client=ClientService(session).get_by_id(id)
    if not client:
        raise HTTPException(status_code=404,detail=f"client :{id} non trouvé")
    return client

@router.post("/", response_model=ClientRead,status_code=status.HTTP_201_CREATED)
def post_client(client: ClientCreate, session: Session= Depends(get_db)):
    try :
        created_client = ClientService(session).create(client)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e)
    return created_client


@router.patch("/{id}", response_model=ClientRead)
def patch_client(id:int, client: ClientUpdate, session: Session= Depends(get_db)):
    try :
        created_client = ClientService(session).patch(id,**client.model_dump(exclude_unset=True))
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e)
    if not created_client:
        raise HTTPException(status_code=404,detail=f"client :{id} non trouvé")
    return created_client


@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_client(id:int, session: Session= Depends(get_db)):
    client= ClientService(session).delete(id)
    if not client:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"client:{id} non trouvé")
    return client