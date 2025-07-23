from sqlmodel import SQLModel, Field, Relationship
from .commune_model import Commune
from typing import List

class Departement(SQLModel, table=True):
    """Table représentant les départements français."""
    
    __tablename__ = "t_departements"
    
    departement_code: str = Field(primary_key=True, max_length=2)
    departement_nom: str | None = Field(default=None, max_length=50, nullable=True)
    
    communes: List["Commune"] = Relationship(back_populates="departement")