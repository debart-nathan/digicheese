from sqlmodel import SQLModel, Field, Relationship
from .departement_model import Departement

class Commune(SQLModel, table=True):
    """Table représentant les communes associées à un département."""
    
    __tablename__ = "t_communes"
    
    commune_id: int | None = Field(default=None, primary_key=True)
    fk_commune_departement: str = Field(foreign_key="t_departement.code_departement", max_length=2, nullable=False)
    commune_codepostal: str | None = Field(default=None, max_length=5, nullable=True)
    commune_ville: str | None = Field(default=None, max_length=50, nullable=True)
    
    departement: Departement | None = Relationship(back_populates="communes")