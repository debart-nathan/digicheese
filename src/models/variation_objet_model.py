from sqlmodel import SQLModel, Field, Relationship
from decimal import Decimal
from .objet_model import Objet  # Importing the Objet class

class VariationObjetBase(SQLModel):
    variation_objet_taille: str | None = Field(default=None, max_length=50, nullable=True)
    variation_objet_poids: Decimal | None = Field(default=Decimal("0.0000"), nullable=False)
    fk_objet_id: int | None = Field(default=None, foreign_key="t_objet.objet_id", nullable=False)

class VariationObjet(VariationObjetBase, table=True):
    __tablename__ = "t_variation_objet"
    variation_objet_id: int | None = Field(default=None, primary_key=True)
    objet: Objet | None = Relationship(back_populates="variations")


class VariationObjetCreate(VariationObjetBase):
    pass


class VariationObjetUpdate(VariationObjetBase):
    variation_objet_poids: Decimal | None = Field(default=Decimal("0.0000"), nullable=True)
    fk_objet_id: int | None = Field(default=None, foreign_key="t_objet.objet_id", nullable=True)



class VariationObjetRead(VariationObjetBase):
    variation_objet_id: int | None = Field(default=None, primary_key=True)
