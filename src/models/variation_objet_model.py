from sqlmodel import SQLModel, Field, Relationship
from decimal import Decimal
from .objet_model import Objet

class VariationObjetBase(SQLModel):
    variation_objet_taille: str | None = Field(default=None, max_length=50, nullable=True)
    variation_objet_poids: Decimal | None = Field(default=Decimal("0.0000"), nullable=False)
    fk_variation_objet_objet_id: int | None = Field(default=None, foreign_key="t_objets.objet_id", nullable=False)

class VariationObjet(VariationObjetBase, table=True):
    __tablename__ = "t_variations_objets"
    variation_objet_id: int | None = Field(default=None, primary_key=True)
    objet: Objet | None = Relationship(back_populates="variations_objet")
    details_commandes: list["DetailCommande"] = Relationship(back_populates="variation_objet")


class VariationObjetCreate(VariationObjetBase):
    pass


class VariationObjetUpdate(VariationObjetBase):
    variation_objet_poids: Decimal | None = None
    fk_objet_id: int | None = None



class VariationObjetRead(VariationObjetBase):
    variation_objet_id: int | None = Field(default=None, primary_key=True)
