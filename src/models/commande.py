from sqlmodel import SQLModel, Field, Relationship
from datetime import date

class Commande(SQLModel, table=True):
    """Table représentant les commandes passées par les clients."""
    
    __tablename__ = "t_entcde"
    
    commande: int | None = Field(default=None, primary_key=True)
    datcde: date | None = Field(default=None, nullable=True)
    codcli: int | None = Field(default=None, foreign_key="t_client.codcli", nullable=True)
    timbrecli: float | None = Field(default=None, nullable=True)
    timbrecde: float | None = Field(default=None, nullable=True)
    nbcolis: int = Field(default=1)
    cheqcli: float | None = Field(default=None, nullable=True)
    idcondit: int = Field(default=0)
    cdeComt: str | None = Field(default=None, max_length=255, nullable=True)
    barchive: int = Field(default=0)
    bstock: int = Field(default=0)