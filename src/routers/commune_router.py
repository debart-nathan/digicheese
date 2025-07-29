from fastapi import APIRouter, Depends, Query, HTTPException, status
from sqlmodel import Session
from ..database import get_db
from ..models import Commune, CommuneCreate, CommuneRead, CommuneUpdate
from ..repositories import CommuneRepository

# Create an APIRouter instance for commune-related endpoints
router = APIRouter(prefix="/commune", tags=['Commune'])

@router.get("/", response_model=list[CommuneRead])
def get_all_commune(offset: int = 0, limit: int = Query(default=100, le=100), session: Session = Depends(get_db)) -> list[Commune]:
    """
    Retrieve all communes with pagination support.
    
    Parameters:
    - offset: int - Number of items to skip (for pagination)
    - limit: int - Maximum number of items to return (max 100)
    - session: Session - Database session dependency
    
    Returns:
    - list[CommuneRead]: List of commune objects
    """
    return CommuneRepository(session).get_all_communes(limit, offset)

@router.get("/{id}", response_model=CommuneRead,responses={
    404:{"description":"Commune id non trouvé"}
})
def get_commune(id: int, session: Session = Depends(get_db)):
    """
    Retrieve a specific commune by ID.
    
    Parameters:
    - id: int - ID of the commune to retrieve
    - session: Session - Database session dependency
    
    Returns:
    - CommuneRead: The requested commune object
    
    Raises:
    - HTTPException 404: If commune is not found
    """
    commune = CommuneRepository(session).get_commune(id)
    if not commune:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"commune :{id} non trouvé")
    return commune

@router.post("/", response_model=CommuneRead, status_code=status.HTTP_201_CREATED)
def post_commune(commune: CommuneCreate, session: Session = Depends(get_db)):
    """
    Create a new commune.
    
    Parameters:
    - commune: CommuneCreate - Commune data for creation
    - session: Session - Database session dependency
    
    Returns:
    - CommuneRead: The created commune object
    """
    commune_instance = Commune.model_validate(commune)
    created_commune = CommuneRepository(session).create_commune(commune_instance)
    return created_commune

@router.patch("/{id}", response_model=CommuneRead,responses={
    404:{"description":"Commune id non trouvé"}
})
def patch_commune(id: int, commune: CommuneUpdate, session: Session = Depends(get_db)):
    """
    Partially update a commune's information.
    
    Parameters:
    - id: int - ID of the commune to update
    - commune: CommuneUpdate - Commune data for partial update
    - session: Session - Database session dependency
    
    Returns:
    - CommuneRead: The updated commune object
    
    Raises:
    - HTTPException 404: If commune is not found
    """
    created_commune = CommuneRepository(session).update_commune(id, **commune.model_dump(exclude_unset=True))
    if not created_commune:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"commune :{id} non trouvé")
    return created_commune

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT,responses={
    404:{"description":"Commune id non trouvé"}
})
def delete_commune(id: int, session: Session = Depends(get_db)):
    """
    Delete a commune by ID.
    
    Parameters:
    - id: int - ID of the commune to delete
    - session: Session - Database session dependency
    
    Returns:
    - None: Empty response with status code 204
    
    Raises:
    - HTTPException 404: If commune is not found
    """
    commune = CommuneRepository(session).delete_commune(id)
    if not commune:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"commune:{id} non trouvé")
    return commune