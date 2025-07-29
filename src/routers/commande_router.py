from fastapi import APIRouter, Depends, Query, HTTPException, status
from sqlmodel import Session
from ..database import get_db
from ..models import Commande, CommandeCreate, CommandeRead, CommandeUpdate
from ..repositories import CommandeRepository

# Create an APIRouter instance for order (commande) related endpoints
router = APIRouter(prefix="/commande", tags=['Commande'])

@router.get("/", response_model=list[CommandeRead])
def get_all_commande(offset: int = 0, limit: int = Query(default=100, le=100), session: Session = Depends(get_db)) -> list[Commande]:
    """
    Retrieve all orders with pagination support.
    
    Parameters:
    - offset: int - Number of items to skip (for pagination)
    - limit: int - Maximum number of items to return (max 100)
    - session: Session - Database session dependency
    
    Returns:
    - list[CommandeRead]: List of order objects
    """
    return CommandeRepository(session).get_all_commandes(limit, offset)

@router.get("/{id}", response_model=CommandeRead,responses={
    "404":{"description":"Commande id non trouvé"}
})
def get_commande(id: int, session: Session = Depends(get_db)):
    """
    Retrieve a specific order by ID.
    
    Parameters:
    - id: int - ID of the order to retrieve
    - session: Session - Database session dependency
    
    Returns:
    - CommandeRead: The requested order object
    
    Raises:
    - HTTPException 404: If order is not found
    """
    commande = CommandeRepository(session).get_commande(id)
    if not commande:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"commande :{id} non trouvé")
    return commande

@router.post("/", response_model=CommandeRead, status_code=status.HTTP_201_CREATED)
def post_commande(commande: CommandeCreate, session: Session = Depends(get_db)):
    """
    Create a new order.
    
    Parameters:
    - commande: CommandeCreate - Order data for creation
    - session: Session - Database session dependency
    
    Returns:
    - CommandeRead: The created order object
    """
    commande_instance = Commande.model_validate(commande)
    created_commande = CommandeRepository(session).create_commande(commande_instance)
    return created_commande

@router.patch("/{id}", response_model=CommandeRead,responses={
    404:{"description":"Commande id non trouvé"}
})
def patch_commande(id: int, commande: CommandeUpdate, session: Session = Depends(get_db)):
    """
    Partially update an order's information.
    
    Parameters:
    - id: int - ID of the order to update
    - commande: CommandeUpdate - Order data for partial update
    - session: Session - Database session dependency
    
    Returns:
    - CommandeRead: The updated order object
    
    Raises:
    - HTTPException 404: If order is not found
    """
    created_commande = CommandeRepository(session).update_commande(id, **commande.model_dump(exclude_unset=True))
    if not created_commande:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"commande :{id} non trouvé")
    return created_commande

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT,responses={
    404:{"description":"Commande id non trouvé"}
})
def delete_commande(id: int, session: Session = Depends(get_db)):
    """
    Delete an order by ID.
    
    Parameters:
    - id: int - ID of the order to delete
    - session: Session - Database session dependency
    
    Returns:
    - None: Empty response with status code 204
    
    Raises:
    - HTTPException 404: If order is not found
    """
    commande = CommandeRepository(session).delete_commande(id)
    if not commande:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"commande:{id} non trouvé")
    return commande