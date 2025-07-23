from sqlmodel import SQLModel, Field



class DetailColis(SQLModel, table=True):
    """Table représentant les détails des colis."""
    
    __tablename__ = "t_detail_colis"
    
    detail_colis_id: int | None = Field(default=None, primary_key=True) 
    fk_detail_commande_id: int | None = Field(default=None, foreign_key="t_detail_commandes.detail_commande_id", index=True, nullable=True)
    fk_colis_id: int | None = Field(default=None, foreign_key="t_colis.colis_id", index=True, nullable=True)
    detail_colis_quantitee: int = Field(default=1)
    detail_colis_commentaire: str | None = Field(default=None, max_length=100, nullable=True)