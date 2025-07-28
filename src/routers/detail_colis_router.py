from fastapi import APIRouter, Depends, Query, HTTPException, status
from sqlmodel import Session
from ..database import get_db
from ..models import DetailColis, DetailColisCreate, DetailColisRead, DetailColisUpdate
from ..repositories import DetailColisRepository

# Create an APIRouter instance for package detail (DetailColis) endpoints
router = APIRouter(prefix="/detail_colis", tags=['DetailColis'])

@router.get("/", response_model=list[DetailColisRead])
def get_all_detail_colis(offset: int = 0, limit: int = Query(default=100, le=100), session: Session = Depends(get_db)) -> list[DetailColis]:
    """
    Retrieve all package details with pagination support.
    
    Parameters:
    - offset: int - Number of items to skip (pagination offset)
    - limit: int - Maximum number of items to return (max 100)
    - session: Session - Database session dependency
    
    Returns:
    - list[DetailColisRead]: List of package detail objects
    """
    return DetailColisRepository(session).get_all_detail_colis(limit, offset)

@router.get("/{id}", response_model=DetailColisRead)
def get_detail_colis(id: int, session: Session = Depends(get_db)):
    """
    Retrieve a specific package detail by ID.
    
    Parameters:
    - id: int - ID of the package detail to retrieve
    - session: Session - Database session dependency
    
    Returns:
    - DetailColisRead: The requested package detail object
    
    Raises:
    - HTTPException 404: If package detail is not found
    """
    detail_colis = DetailColisRepository(session).get_detail_colis(id)
    if not detail_colis:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Detail Colis: {id} non trouvé")
    return detail_colis

@router.post("/", response_model=DetailColisRead, status_code=status.HTTP_201_CREATED)
def post_detail_colis(detail_colis: DetailColisCreate, session: Session = Depends(get_db)):
    """
    Create a new package detail.
    
    Parameters:
    - detail_colis: DetailColisCreate - Package detail data for creation
    - session: Session - Database session dependency
    
    Returns:
    - DetailColisRead: The created package detail object
    """
    detail_colis_instance = DetailColis.model_validate(detail_colis)
    created_detail_colis = DetailColisRepository(session).create_detail_colis(detail_colis_instance)
    return created_detail_colis

@router.patch("/{id}")
def patch_detail_colis(id: int, detail_colis: DetailColisUpdate, session: Session = Depends(get_db)):
    """
    Partially update a package detail's information.
    
    Parameters:
    - id: int - ID of the package detail to update
    - detail_colis: DetailColisUpdate - Package detail data for partial update
    - session: Session - Database session dependency
    
    Returns:
    - The updated package detail object
    
    Raises:
    - HTTPException 404: If package detail is not found
    
    Note: The response_model is not specified in the decorator, which may cause inconsistent response documentation
    """
    created_detail_colis = DetailColisRepository(session).update_detail_colis(id, **detail_colis.model_dump(exclude_unset=True))
    if not created_detail_colis:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Detail Colis: {id} non trouvé")
    return created_detail_colis

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_detail_colis(id: int, session: Session = Depends(get_db)):
    """
    Delete a package detail by ID.
    
    Parameters:
    - id: int - ID of the package detail to delete
    - session: Session - Database session dependency
    
    Returns:
    - dict: {"ok": True} if successful (though 204 No Content typically returns nothing)
    
    Raises:
    - HTTPException 404: If package detail is not found
    
    Note: The implementation returns a JSON response despite using status_code 204 (No Content),
    which is inconsistent. Typically, 204 responses should have no body.
    """
    result: bool = DetailColisRepository(session).delete_detail_colis(id)
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Detail Colis: {id} non trouvé")
    return {"ok": True}