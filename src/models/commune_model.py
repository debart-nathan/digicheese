from sqlmodel import SQLModel, Field, Relationship
from .departement_model import Departement


class CommuneBase(SQLModel):

    fk_commune_departement: str | None = Field(foreign_key="t_departements.departement_code", max_length=2, nullable=False)
    commune_codepostal: str | None = Field(default=None, max_length=5, nullable=True)
    commune_ville: str | None = Field(default=None, max_length=50, nullable=True)

class Commune(CommuneBase, table=True):
    """Table représentant les communes associées à un département."""
    
    __tablename__ = "t_communes"

    commune_id: int | None = Field(default=None, primary_key=True)
    departement: Departement | None = Relationship(back_populates="communes")
    clients: list["Client"] = Relationship(back_populates="commune")


class CommuneCreate(CommuneBase):
    pass  # héritage direct, tous champs requis

class CommuneUpdate(SQLModel):
     fk_commune_departement: str | None = Field(foreign_key="t_departements.departement_code", max_length=2)

class CommuneRead(CommuneBase):
    commune_id: int | None = Field(default=None, primary_key=True)