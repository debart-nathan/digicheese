from fastapi import APIRouter, Depends, Query, HTTPException, status
from sqlmodel import Session
from ..database import get_db
from ..models import Client, ClientCreate, ClientUpdate, ClientRead
from ..services import ClientService

# Create an APIRouter instance for client-related endpoints
router = APIRouter(prefix="/client", tags=['Client'])

@router.get("/", response_model=list[ClientRead])
def get_all_clients(offset: int = 0, limit: int = Query(default=100, le=100), session: Session = Depends(get_db)) -> list[ClientRead]:
    """
    Retrieve all clients with pagination support.
    
    Parameters:
    - offset: int - Number of items to skip (for pagination)
    - limit: int - Maximum number of items to return (max 100)
    - session: Session - Database session dependency
    
    Returns:
    - list[ClientRead]: List of client objects
    """
    return ClientService(session).get_all(limit, offset)

@router.get("/{id}", response_model=ClientRead)
def get_client(id: int, session: Session = Depends(get_db)):
    """
    Retrieve a specific client by ID.
    
    Parameters:
    - id: int - ID of the client to retrieve
    - session: Session - Database session dependency
    
    Returns:
    - ClientRead: The requested client object
    
    Raises:
    - HTTPException 404: If client is not found
    """
    client = ClientService(session).get_by_id(id)
    if not client:
        raise HTTPException(status_code=404, detail=f"client :{id} non trouvé")
    return client

@router.post("/", response_model=ClientRead, status_code=status.HTTP_201_CREATED)
def post_client(client: ClientCreate, session: Session = Depends(get_db)):
    """
    Create a new client.
    
    Parameters:
    - client: ClientCreate - Client data for creation
    - session: Session - Database session dependency
    
    Returns:
    - ClientRead: The created client object
    
    Raises:
    - HTTPException 400: If there's a validation error
    """
    try:
        created_client = ClientService(session).create(client)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e)
    return created_client

@router.patch("/{id}", response_model=ClientRead)
def patch_client(id: int, client: ClientUpdate, session: Session = Depends(get_db)):
    """
    Partially update a client's information.
    
    Parameters:
    - id: int - ID of the client to update
    - client: ClientUpdate - Client data for partial update
    - session: Session - Database session dependency
    
    Returns:
    - ClientRead: The updated client object
    
    Raises:
    - HTTPException 400: If there's a validation error
    - HTTPException 404: If client is not found
    """
    try:
        created_client = ClientService(session).patch(id, **client.model_dump(exclude_unset=True))
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e)
    if not created_client:
        raise HTTPException(status_code=404, detail=f"client :{id} non trouvé")
    return created_client

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_client(id: int, session: Session = Depends(get_db)):
    """
    Delete a client by ID.
    
    Parameters:
    - id: int - ID of the client to delete
    - session: Session - Database session dependency
    
    Returns:
    - None: Empty response with status code 204
    
    Raises:
    - HTTPException 404: If client is not found
    """
    client = ClientService(session).delete(id)
    if not client:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"client:{id} non trouvé")
    return client