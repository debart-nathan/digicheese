from sqlmodel import SQLModel, Field, Relationship
from .variation_objet_model import VariationObjet
from .commande_model import Commande



class DetailCommandeBase(SQLModel):
    """Table représentant les détails des commandes."""

    fk_detail_commande_commande_id: int | None = Field(default=None, foreign_key="t_commandes.commande_id", index=True, nullable=True)
    detail_commande_quantitee: int | None = Field(default=1)
    detail_commande_commentaire: str | None = Field(default="", max_length=100)
    fk_detail_commande_variation_objet_id: int | None = Field(default=None, foreign_key="t_variations_objets.variation_objet_id", nullable=True)


class DetailCommande(DetailCommandeBase, table=True):
    """Table représentant les détails des commandes."""
    
    __tablename__ = "t_details_commandes"
    
    detail_commande_id: int | None = Field(default=None, primary_key=True)
    details_colis: list["DetailColis"] = Relationship(back_populates="detail_commande")
    commande: Commande = Relationship(back_populates="details_commande")
    variation_objet: VariationObjet = Relationship(back_populates="details_commandes")


class DetailCommandeCreate(DetailCommandeBase):
    pass

class DetailCommandeUpdate(DetailCommandeBase):
    detail_commande_quantitee: int | None = Field(default=None, nullable=True)
    detail_commande_commentaire: str | None = Field(default=None,max_length=100 ,nullable=True)


class DetailCommandeRead(DetailCommandeBase):
    detail_commande_id: int | None = Field(default=None, primary_key=True)
