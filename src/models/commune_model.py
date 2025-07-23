from sqlmodel import SQLModel, Field, Relationship
from .departement_model import Departement


class Commune(SQLModel, table=True):
    """Table représentant les communes associées à un département."""
    
    __tablename__ = "t_communes"
    
    commune_id: int | None = Field(default=None, primary_key=True)
    fk_commune_departement: str = Field(foreign_key="t_departements.departement_code", max_length=2, nullable=False)
    commune_codepostal: str | None = Field(default=None, max_length=5, nullable=True)
    commune_ville: str | None = Field(default=None, max_length=50, nullable=True)
    
    departement: Departement | None = Relationship(back_populates="communes")

class CommuneBase(SQLModel):
    fk_commune_departement: str
    commune_codepostal: str
    commune_ville: str

class CommuneCreate(CommuneBase):
    pass  # héritage direct, tous champs requis

class CommuneUpdate(SQLModel):
    fk_commune_departement: str
    commune_codepostal: str | None = None
    commune_ville: str | None = None

class CommuneRead(CommuneBase):
    commune_id: int