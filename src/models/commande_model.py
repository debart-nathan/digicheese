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


class CommandeBase(SQLModel):
    commande_date: date
    fk_client_id: int
    client_timbre: float
    commande_timbre: float
    client_cheque: float
    commande_commentaire: str

class CommandeCreate(CommandeBase):
    pass

class CommandeUpdate(SQLModel):
    commande_date: date | None = None
    fk_client_id: int | None = None
    client_timbre: float | None = None
    commande_timbre: float | None = None
    client_cheque: float | None = None
    commande_commentaire: str | None = None


class CommandeRead(CommandeBase):
    commande_id: int