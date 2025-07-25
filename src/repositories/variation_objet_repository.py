from sqlmodel import Session, select
from ..models import VariationObjet

class VariationObjetRepository:   
    def __init__(self, session: Session):
        self.session = session

    def create_variation_objet(self, variation_objet: VariationObjet) -> VariationObjet:
        self.session.add(variation_objet)
        self.session.commit()
        self.session.refresh(variation_objet)
        return variation_objet

    def get_variation_objet(self, variation_objet_code: int) -> VariationObjet | None:
        statement = select(VariationObjet).where(VariationObjet.variation_objet_code == variation_objet_code)
        return self.session.exec(statement).one_or_none()

    def get_all_variation_objet(self,limit: int | None = None, offset: int | None = None ) -> list[VariationObjet]:
        statement = select(VariationObjet).limit(limit).offset(offset)
        return list(self.session.exec(statement).all())

    def update_variation_objet(self, variation_objet_code: int ,variation_objet_update: dict) -> VariationObjet | None:
        existing_variation_objet = self.get_variation_objet(variation_objet_code)
        if existing_variation_objet:
            existing_variation_objet.sqlmodel_update(variation_objet_update)
            self.session.add(existing_variation_objet)
            self.session.commit()
            self.session.refresh(existing_variation_objet)
            return existing_variation_objet
        return None

    def delete_variation_objet(self, variation_objet_code: int) -> bool:
        existing_variation_objet = self.get_variation_objet(variation_objet_code)
        if existing_variation_objet:
            self.session.delete(existing_variation_objet)
            self.session.commit()
            return True
        return False