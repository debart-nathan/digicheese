from fastapi import APIRouter, Depends, Query, HTTPException, status
from sqlmodel import Session
from ..database import get_db
from ..models import DetailCommande, DetailCommandeCreate, DetailCommandeRead, DetailCommandeUpdate
from ..repositories import DetailCommandeRepository

# Create an APIRouter instance for order detail (DetailCommande) endpoints
router = APIRouter(prefix="/detail_commande", tags=['DetailCommande'])

@router.get("/", response_model=list[DetailCommandeRead])
def get_all_detail_commande(offset: int = 0, limit: int = Query(default=100, le=100), session: Session = Depends(get_db)) -> list[DetailCommande]:
    """
    Retrieve all order details with pagination support.
    
    Parameters:
    - offset: int - Number of items to skip (pagination offset)
    - limit: int - Maximum number of items to return (max 100)
    - session: Session - Database session dependency
    
    Returns:
    - list[DetailCommandeRead]: List of order detail objects
    """
    return DetailCommandeRepository(session).get_all_detail_commandes(limit, offset)

@router.get("/{id}", response_model=DetailCommandeRead,responses={
    404:{"description":"Commande detail id non trouvé"}
})
def get_detail_commande(id: int, session: Session = Depends(get_db)):
    """
    Retrieve a specific order detail by ID.
    
    Parameters:
    - id: int - ID of the order detail to retrieve
    - session: Session - Database session dependency
    
    Returns:
    - DetailCommandeRead: The requested order detail object
    
    Raises:
    - HTTPException 404: If order detail is not found
    """
    detail_commande = DetailCommandeRepository(session).get_detail_commande(id)
    if not detail_commande:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Detail Commande: {id} non trouvé")
    return detail_commande

@router.post("/", response_model=DetailCommandeRead, status_code=status.HTTP_201_CREATED)
def post_detail_commande(detail_commande: DetailCommandeCreate, session: Session = Depends(get_db)):
    """
    Create a new order detail.
    
    Parameters:
    - detail_commande: DetailCommandeCreate - Order detail data for creation
    - session: Session - Database session dependency
    
    Returns:
    - DetailCommandeRead: The created order detail object
    """
    detail_commande_instance = DetailCommande.model_validate(detail_commande)
    created_detail_commande = DetailCommandeRepository(session).create_detail_commande(detail_commande_instance)
    return created_detail_commande

@router.patch("/{id}", response_model=DetailCommandeRead,responses={
    404:{"description":"Commande detail id non trouvé"}
})
def patch_detail_commande(id: int, detail_commande: DetailCommandeUpdate, session: Session = Depends(get_db)):
    """
    Partially update an order detail's information.
    
    Parameters:
    - id: int - ID of the order detail to update
    - detail_commande: DetailCommandeUpdate - Order detail data for partial update
    - session: Session - Database session dependency
    
    Returns:
    - DetailCommandeRead: The updated order detail object
    
    Raises:
    - HTTPException 404: If order detail is not found
    """
    created_detail_commande = DetailCommandeRepository(session).update_detail_commande(id, **detail_commande.model_dump(exclude_unset=True))
    if not created_detail_commande:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Detail Commande: {id} non trouvé")
    return created_detail_commande

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT,responses={
    404:{"description":"Commande detail id non trouvé"}
})
def delete_detail_commande(id: int, session: Session = Depends(get_db)):
    """
    Delete an order detail by ID.
    
    Parameters:
    - id: int - ID of the order detail to delete
    - session: Session - Database session dependency
    
    Returns:
    - dict: {"ok": True} if successful (though 204 No Content typically returns nothing)
    
    Raises:
    - HTTPException 404: If order detail is not found
    
    """
    detail_commande = DetailCommandeRepository(session).delete_detail_commande(id)
    if not detail_commande:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Detail Commande: {id} non trouvé")
    return {"ok": True}