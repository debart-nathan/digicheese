from sqlmodel import SQLModel, Field, Relationship

from typing import List

class Departement(SQLModel, table=True):
    """Table représentant les départements français."""
    
    __tablename__ = "t_departements"
    
    departement_code: str = Field(primary_key=True, max_length=2)
    departement_nom: str | None = Field(default=None, max_length=50, nullable=True)
    
    communes: List["Commune"] = Relationship(back_populates="departement")


class DepartementBase(SQLModel):
    departement_code: str
    departement_nom: str

class DepartementCreate(DepartementBase):
    pass  # héritage direct, tous champs requis

class DepartementUpdate(SQLModel):
    departement_code: str | None = None
    departement_nom: str | None = None

class DepartementRead(DepartementBase):
    departement_code: str