from sqlmodel import SQLModel, Field
from datetime import date

class Commande(SQLModel, table=True):
    """Table représentant les commandes passées par les clients."""
    
    __tablename__ = "t_commandes"
    
    commande_id: int | None = Field(default=None, primary_key=True)
    commande_date: date | None = Field(default=None, nullable=True)
    fk_client_id: int | None = Field(default=None, foreign_key="t_clients.client_id", nullable=True)
    client_timbre: float | None = Field(default=None, nullable=True) #value of the timbre send by the client
    commande_timbre: float | None = Field(default=None, nullable=True) #value of the timbre needed for the order
    client_cheque: float | None = Field(default=None, nullable=True) #value of the check send by the client
    commande_commentaire: str | None = Field(default=None, max_length=255, nullable=True)