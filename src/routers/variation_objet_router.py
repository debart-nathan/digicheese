from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlmodel import Session
from ..database import get_db
from ..models import VariationObjet, VariationObjetCreate, VariationObjetRead, VariationObjetUpdate
from ..repositories import VariationObjetRepository

# Create an APIRouter instance for object variation endpoints
router = APIRouter(prefix="/variation_objet", tags=['VariationObjet'])

@router.get("/", response_model=list[VariationObjetRead])
def get_all_variation_objets(offset: int = 0, limit: int = Query(default=100, le=100), session: Session = Depends(get_db)) -> list[VariationObjet]:
    """
    Retrieve all object variations with pagination support.
    
    Parameters:
    - offset: int - Number of items to skip (pagination offset)
    - limit: int - Maximum number of items to return (max 100)
    - session: Session - Database session dependency
    
    Returns:
    - list[VariationObjetRead]: List of object variation records
    
    """
    return VariationObjetRepository(session).get_all_variation_objets(limit, offset)

@router.get("/{id}", response_model=VariationObjetRead,responses={
    404: {"description": "Variation objet id non trouvé"}})
def get_variation_objet(id: int, session: Session = Depends(get_db)):
    """
    Retrieve a specific object variation by ID.
    
    Parameters:
    - id: int - ID of the object variation to retrieve
    - session: Session - Database session dependency
    
    Returns:
    - VariationObjetRead: The requested object variation record
    
    Raises:
    - HTTPException 404: If object variation is not found
    
    """
    variation_objet = VariationObjetRepository(session).get_variation_objet(id)
    if not variation_objet:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Variation objet: {id} non trouvé")
    return variation_objet

@router.post("/", response_model=VariationObjetRead, status_code=status.HTTP_201_CREATED)
def post_variation_objet(variation_objet: VariationObjetCreate, session: Session = Depends(get_db)):
    """
    Create a new object variation.
    
    Parameters:
    - variation_objet: VariationObjetCreate - Object variation data for creation
    - session: Session - Database session dependency
    
    Returns:
    - VariationObjetRead: The created object variation record
    
    """
    variation_objet_instance = VariationObjet.model_validate(variation_objet)
    created_variation_objet = VariationObjetRepository(session).create_variation_objet(variation_objet_instance)
    return created_variation_objet

@router.patch("/{id}", response_model=VariationObjetRead, responses={
    404: {"description": "Variation id non trouvé"}})
def patch_variation_objet(id: int, variation_objet: VariationObjetUpdate, session: Session = Depends(get_db)):
    """
    Partially update an object variation's information.
    
    Parameters:
    - id: int - ID of the object variation to update
    - variation_objet: VariationObjetUpdate - Object variation data for partial update
    - session: Session - Database session dependency
    
    Returns:
    - VariationObjetRead: The updated object variation record
    
    Raises:
    - HTTPException 404: If object variation is not found
    
    """
    created_variation_objet = VariationObjetRepository(session).update_variation_objet(id, **variation_objet.model_dump(exclude_unset=True))
    if not created_variation_objet:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Variation objet: {id} non trouvé")
    return created_variation_objet

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT,responses={
    404: {"description": "Variation objet id non trouvé"}})
def delete_variation_objet(id: int, session: Session = Depends(get_db)):
    """
    Delete an object variation by ID.
    
    Parameters:
    - id: int - ID of the object variation to delete
    - session: Session - Database session dependency
    
    Returns:
    - None: Empty response with status code 204
    
    Raises:
    - HTTPException 404: If object variation is not found
    
    """
    if not VariationObjetRepository(session).delete_variation_objet(id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Variation objet: {id} non trouvé")
    return {"ok": True}