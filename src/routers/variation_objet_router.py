from fastapi import APIRouter, Depends, Query
from sqlmodel import Session
from ..database import get_db
from ..models import VariationObjet, VariationObjetCreate, VariationObjetRead, VariationObjetUpdate
from ..repositories import VariationObjetRepository

router = APIRouter(prefix="/variation_objet",tags=['VariationObjet'])

@router.get("/", response_model=list[VariationObjetRead])
def get_all_variation_objet(offset: int = 0, limit: int = Query(default=100, le=100),session: Session= Depends(get_db))->list[VariationObjet]:
    return VariationObjetRepository(session).get_all_variation_objets(limit,offset)

@router.get("/{id}", response_model=VariationObjetRead )
def get_variation_objet(id:int,session: Session= Depends(get_db)):
    return VariationObjetRepository(session).get_variation_objet(id)

@router.post("/", response_model=VariationObjetRead)
def post_variation_objet(variation_objet: VariationObjetCreate, session: Session = Depends(get_db)):
    variation_objet_instance = VariationObjet.model_validate(variation_objet)
    created_variation_objet = VariationObjetRepository(session).create_variation_objet(variation_objet_instance)
    return created_variation_objet


@router.patch("/{id}")
def patch_variation_objet(id:int,variation_objet:VariationObjetUpdate,session: Session= Depends(get_db)):
    created_variation_objet = VariationObjetRepository(session).update_variation_objet(id,**variation_objet.model_dump(exclude_unset=True))
    return created_variation_objet


@router.delete("/{id}")
def delete_variation_objet(id:int,session: Session= Depends(get_db)):
    return VariationObjetRepository(session).delete_variation_objet(id)