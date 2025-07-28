from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlmodel import Session
from ..database import get_db
from ..models import Objet, ObjetCreate, ObjetRead, ObjetUpdate
from ..repositories import ObjetRepository

router = APIRouter(prefix="/objet",tags=['Objet'])

@router.get("/", response_model=list[ObjetRead])
def get_all_objet(offset: int = 0, limit: int = Query(default=100, le=100),session: Session= Depends(get_db))->list[Objet]:
    return ObjetRepository(session).get_all_objets(limit,offset)

@router.get("/{id}", response_model=ObjetRead )
def get_objet(id:int,session: Session= Depends(get_db)):
    objet = ObjetRepository(session).get_objet(id)
    if not objet:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"objet: {id} non trouvé")
    return objet

@router.post("/", response_model=ObjetRead,status_code=status.HTTP_201_CREATED)
def post_objet(objet: ObjetCreate, session: Session = Depends(get_db)):
    objet_instance = Objet.model_validate(objet)
    created_objet = ObjetRepository(session).create_objet(objet_instance)
    return created_objet


@router.patch("/{id}", response_model=ObjetRead)
def patch_objet(id:int,objet:ObjetUpdate,session: Session= Depends(get_db)):
    created_objet = ObjetRepository(session).update_objet(id,**objet.model_dump(exclude_unset=True))
    if not created_objet:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Objet: {id} non trouvé")
    return created_objet


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_objet(id:int,session: Session= Depends(get_db)):
    if not ObjetRepository(session).delete_objet(id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Objet: {id} non trouvé")
    return {"ok":True}