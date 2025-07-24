from sqlmodel import SQLModel, Field



class DetailCommandeBase(SQLModel):
    """Table représentant les détails des commandes."""

    fk_commande_id: int | None = Field(default=None, foreign_key="t_commandes.commande_id", index=True, nullable=True)
    detail_commande_quantitee: int | None = Field(default=1)
    detail_commande_commentaire: str | None = Field(default="", max_length=100)


class DetailCommande(DetailCommandeBase, table=True):
    """Table représentant les détails des commandes."""
    
    __tablename__ = "t_detail_commandes"
    
    detail_commande_id: int | None = Field(default=None, primary_key=True)


class DetailCommandeCreate(DetailCommandeBase):
    pass

class DetailCommandeUpdate(DetailCommandeBase):
    detail_commande_quantitee: int | None = Field(default=None, nullable=True)
    detail_commande_commentaire: str | None = Field(default=None,max_length=100 ,nullable=True)


class DetailCommandeRead(DetailCommandeBase):
    detail_commande_id: int | None = Field(default=None, primary_key=True)
