from sqlmodel import SQLModel, Field
from datetime import date

class CommandeBase(SQLModel, table=True):
    commande_date: date | None = Field(default=None, nullable=True)
    fk_client_id: int | None = Field(default=None, foreign_key="t_clients.client_id", nullable=True)
    client_timbre: float | None = Field(default=None, nullable=True) #value of the timbre send by the client
    commande_timbre: float | None = Field(default=None, nullable=True) #value of the timbre needed for the order
    client_cheque: float | None = Field(default=None, nullable=True) #value of the check send by the client
    commande_commentaire: str | None = Field(default=None, max_length=255, nullable=True)


class Commande(CommandeBase, table=True):
    __tablename__ = "t_commandes"

    commande_id: int | None = Field(default=None, primary_key=True)

class CommandeCreate(CommandeBase):
    pass

class CommandeUpdate(CommandeBase):
    pass



class CommandeRead(CommandeBase):
    commande_id: int | None = Field(default=None, primary_key=True)