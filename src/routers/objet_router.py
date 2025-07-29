from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlmodel import Session
from ..database import get_db
from ..models import Objet, ObjetCreate, ObjetRead, ObjetUpdate
from ..repositories import ObjetRepository

# Create an APIRouter instance for object (Objet) endpoints
router = APIRouter(prefix="/objet", tags=['Objet'])

@router.get("/", response_model=list[ObjetRead])
def get_all_objet(offset: int = 0, limit: int = Query(default=100, le=100), session: Session = Depends(get_db)) -> list[Objet]:
    """
    Retrieve all objects with pagination support.
    
    Parameters:
    - offset: int - Number of items to skip (pagination offset)
    - limit: int - Maximum number of items to return (max 100)
    - session: Session - Database session dependency
    
    Returns:
    - list[ObjetRead]: List of object records
    """
    return ObjetRepository(session).get_all_objets(limit, offset)

@router.get("/{id}", response_model=ObjetRead,responses={
    404:{"description":"Commande detail id non trouvé"}
})
def get_objet(id: int, session: Session = Depends(get_db)):
    """
    Retrieve a specific object by ID.
    
    Parameters:
    - id: int - ID of the object to retrieve
    - session: Session - Database session dependency
    
    Returns:
    - ObjetRead: The requested object record
    
    Raises:
    - HTTPException 404: If object is not found
    """
    objet = ObjetRepository(session).get_objet(id)
    if not objet:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"objet: {id} non trouvé")
    return objet

@router.post("/", response_model=ObjetRead, status_code=status.HTTP_201_CREATED)
def post_objet(objet: ObjetCreate, session: Session = Depends(get_db)):
    """
    Create a new object.
    
    Parameters:
    - objet: ObjetCreate - Object data for creation
    - session: Session - Database session dependency
    
    Returns:
    - ObjetRead: The created object record
    """
    objet_instance = Objet.model_validate(objet)
    created_objet = ObjetRepository(session).create_objet(objet_instance)
    return created_objet

@router.patch("/{id}", response_model=ObjetRead,responses={
    404:{"description":"Commande detail id non trouvé"}
})
def patch_objet(id: int, objet: ObjetUpdate, session: Session = Depends(get_db)):
    """
    Partially update an object's information.
    
    Parameters:
    - id: int - ID of the object to update
    - objet: ObjetUpdate - Object data for partial update
    - session: Session - Database session dependency
    
    Returns:
    - ObjetRead: The updated object record
    
    Raises:
    - HTTPException 404: If object is not found
    """
    created_objet = ObjetRepository(session).update_objet(id, objet.model_dump(exclude_unset=True))
    if not created_objet:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Objet: {id} non trouvé")
    return created_objet

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT,responses={
    404:{"description":"Objet id non trouvé"}
})
def delete_objet(id: int, session: Session = Depends(get_db)):
    """
    Delete an object by ID.
    
    Parameters:
    - id: int - ID of the object to delete
    - session: Session - Database session dependency
    
    Returns:
    - dict: {"ok": True} if successful (though 204 No Content typically returns nothing)
    
    Raises:
    - HTTPException 404: If object is not found

    """
    if not ObjetRepository(session).delete_objet(id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Objet: {id} non trouvé")
    return {"ok": True}