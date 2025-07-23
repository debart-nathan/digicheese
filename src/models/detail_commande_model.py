from sqlmodel import SQLModel, Field



class DetailCommande(SQLModel, table=True):
    """Table représentant les détails des commandes."""
    
    __tablename__ = "t_detail_commandes"
    
    detail_commande_id: int | None = Field(default=None, primary_key=True) 
    fk_commande_id: int | None = Field(default=None, foreign_key="t_commandes.commande_id", index=True, nullable=True)
    detail_commande_quantitee: int = Field(default=1)
    detail_commande_commentaire: str | None = Field(default=None, max_length=100, nullable=True)