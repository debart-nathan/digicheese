from sqlmodel import SQLModel, Field
from datetime import date

class Commande(SQLModel, table=True):
    """Table représentant les commandes passées par les clients."""
    
    __tablename__ = "t_commande"
    
    commande_id: int | None = Field(default=None, primary_key=True)
    commande_date: date | None = Field(default=None, nullable=True)
    fk_client_id: int | None = Field(default=None, foreign_key="t_client.codcli", nullable=True)
    client_timbre: float | None = Field(default=None, nullable=True)
    commande_timbre: float | None = Field(default=None, nullable=True)
    client_cheque: float | None = Field(default=None, nullable=True)
    commande_commentaire: str | None = Field(default=None, max_length=255, nullable=True)