from fastapi import APIRouter, Depends, Query, HTTPException, status
from sqlmodel import Session
from ..database import get_db
from ..models import Colis, ColisCreate, ColisRead, ColisUpdate
from ..repositories import ColisRepository

# Create an APIRouter instance for package (colis) related endpoints
router = APIRouter(prefix="/colis", tags=['Colis'])

@router.get("/", response_model=list[ColisRead])
def get_all_colis(offset: int = 0, limit: int = Query(default=100, le=100), session: Session = Depends(get_db)) -> list[Colis]:
    """
    Retrieve all packages (colis) with pagination support.
    
    Parameters:
    - offset: int - Number of items to skip (for pagination)
    - limit: int - Maximum number of items to return (max 100)
    - session: Session - Database session dependency
    
    Returns:
    - list[ColisRead]: List of package objects
    """
    return ColisRepository(session).get_all_colis(limit, offset)

@router.get("/{id}", response_model=ColisRead)
def get_colis(id: int, session: Session = Depends(get_db)):
    """
    Retrieve a specific package (colis) by ID.
    
    Parameters:
    - id: int - ID of the package to retrieve
    - session: Session - Database session dependency
    
    Returns:
    - ColisRead: The requested package object
    
    Raises:
    - HTTPException 404: If package is not found
    """
    colis = ColisRepository(session).get_colis(id)
    if not colis:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"colis :{id} non trouvé")
    return colis

@router.post("/", response_model=ColisRead, status_code=status.HTTP_201_CREATED)
def post_colis(colis: ColisCreate, session: Session = Depends(get_db)):
    """
    Create a new package (colis).
    
    Parameters:
    - colis: ColisCreate - Package data for creation
    - session: Session - Database session dependency
    
    Returns:
    - ColisRead: The created package object
    """
    colis_instance = Colis.model_validate(colis)
    created_colis = ColisRepository(session).create_colis(colis_instance)
    return created_colis

@router.patch("/{id}", response_model=ColisRead)
def patch_colis(id: int, colis: ColisUpdate, session: Session = Depends(get_db)):
    """
    Partially update a package's (colis) information.
    
    Parameters:
    - id: int - ID of the package to update
    - colis: ColisUpdate - Package data for partial update
    - session: Session - Database session dependency
    
    Returns:
    - ColisRead: The updated package object
    
    Raises:
    - HTTPException 404: If package is not found
    """
    created_colis = ColisRepository(session).update_colis(id, **colis.model_dump(exclude_unset=True))
    if not created_colis:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"colis :{id} non trouvé")
    return created_colis

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT, responses={
    404: {"description": "package is not found"},
})
def delete_colis(id: int, session: Session = Depends(get_db)):
    """
    Delete a package (colis) by ID.
    
    Parameters:
    - id: int - ID of the package to delete
    - session: Session - Database session dependency
    
    Returns:
    - None: Empty response with status code 204
    
    Raises:
    - HTTPException 404: If package is not found
    
    """
    colis = ColisRepository(session).delete_colis(id)
    if not colis:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"colis:{id} non trouvé")
    return ColisRepository(session).delete_colis(id)