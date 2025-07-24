from sqlmodel import SQLModel, Field, Relationship
from typing import List

class DepartementBase(SQLModel):
    departement_nom: str | None = Field(default=None, max_length=50, nullable=True)
    


class Departement(DepartementBase, table=True):
    """Table représentant les départements français."""
    
    __tablename__ = "t_departements"
    
    departement_code: str | None = Field(primary_key=True, max_length=2)

    communes: List["Commune"] = Relationship(back_populates="departement")


class DepartementCreate(DepartementBase):
    pass  # héritage direct, tous champs requis

class DepartementUpdate(DepartementBase):
    departement_nom: str | None = None

class DepartementRead(DepartementBase):
    departement_code: str