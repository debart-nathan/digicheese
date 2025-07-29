from fastapi import APIRouter, Depends, Query, HTTPException, status
from sqlmodel import Session
from ..database import get_db
from ..models import Departement, DepartementCreate, DepartementRead, DepartementUpdate
from ..repositories import DepartementRepository

# Create an APIRouter instance for department-related endpoints
router = APIRouter(prefix="/departement", tags=['Departement'])

@router.get("/", response_model=list[DepartementRead])
def get_all_departements(offset: int = 0, limit: int = Query(default=100, le=100), session: Session = Depends(get_db)) -> list[Departement]:
    """
    Retrieve all departments with pagination support.
    
    Parameters:
    - offset: int - Number of items to skip (for pagination)
    - limit: int - Maximum number of items to return (max 100)
    - session: Session - Database session dependency
    
    Returns:
    - list[DepartementRead]: List of department objects
    """
    return DepartementRepository(session).get_all_departement(limit, offset)

@router.get("/{id}", response_model=DepartementRead,responses={
    404:{"description":"Departement id non trouvé"}
})
def get_departement(id: int, session: Session = Depends(get_db)):
    """
    Retrieve a specific department by ID.
    
    Parameters:
    - id: int - ID of the department to retrieve
    - session: Session - Database session dependency
    
    Returns:
    - DepartementRead: The requested department object
    
    Raises:
    - HTTPException 404: If department is not found
    
    """
    departement = DepartementRepository(session).get_departement(id)
    if not departement:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"departement :{id} non trouvé")
    return departement

@router.post("/", response_model=DepartementRead, status_code=status.HTTP_201_CREATED)
def post_departement(departement: DepartementUpdate, session: Session = Depends(get_db)):
    """
    Create a new department.
    
    Parameters:
    - departement: DepartementUpdate - Department data for creation
    - session: Session - Database session dependency
    
    Returns:
    - DepartementRead: The created department object
    
    """
    departement_instance = Departement.model_validate(departement)
    created_departement = DepartementRepository(session).create_departement(departement_instance)
    return created_departement

@router.patch("/{id}", response_model=DepartementRead,responses={
    404:{"description":"Departement id non trouvé"}
})
def patch_departement(id: int, departement : DepartementUpdate, session: Session = Depends(get_db)):
    """
    Partially update a department's information.
    
    Parameters:
    - id: int - ID of the department to update
    - departement: DepartementUpdate - Department data for partial update
    - session: Session - Database session dependency
    
    Returns:
    - DepartementRead: The updated department object
    
    Raises:
    - HTTPException 404: If department is not found
    
    """
    created_departement = DepartementRepository(session).update_departement(id, **departement.model_dump(exclude_unset=True))
    if not created_departement:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"departement :{id} non trouvé")
    return created_departement

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT,responses={
    404:{"description":"Departement id non trouvé"}
})
def delete_departement(id: int, session: Session = Depends(get_db)):
    """
    Delete a department by ID.
    
    Parameters:
    - id: int - ID of the department to delete
    - session: Session - Database session dependency
    
    Returns:
    - None: Empty response with status code 204
    
    Raises:
    - HTTPException 404: If department is not found
    
    """
    departement = DepartementRepository(session).delete_departement(id)
    if not departement:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"departement:{id} non trouvé")
    return DepartementRepository(session).delete_departement(id)