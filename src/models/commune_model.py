from sqlmodel import SQLModel, Field, Relationship
from .departement_model import Departement
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .client_model import Client

class CommuneBase(SQLModel):
    """
    Schéma de base pour représenter les données de la commune.

    Champs partagés dans tous les schémas liés aux communes,
    y compris le code du département, le code postal et le nom de la ville.
    """

    fk_commune_departement: str | None = Field(
        foreign_key="t_departements.departement_code",
        max_length=2,
        nullable=False,
        description="Code du département auquel la commune est rattachée"
    )

    commune_codepostal: str | None = Field(
        default=None,
        max_length=5,
        nullable=True,
        description="Code postal de la commune"
    )

    commune_ville: str | None = Field(
        default=None,
        max_length=50,
        nullable=True,
        description="Nom de la commune (ville)"
    )


class Commune(CommuneBase, table=True):
    """
    Modèle ORM mappé à la table 't_communes' de la base de données.

    Inclut la logique de persistance et les relations avec le département et les clients associés.
    """

    __tablename__ = "t_communes"

    commune_id: int | None = Field(
        default=None,
        primary_key=True,
        description="Identifiant unique de la commune"
    )

    departement: Departement | None = Relationship(
        back_populates="communes"
    )

    clients: list["Client"] = Relationship(
        back_populates="commune"
    )


class CommuneCreate(CommuneBase):
    """
    Schéma utilisé pour créer une nouvelle entrée de commune.

    Hérite de tous les champs requis du schéma de base.
    """
    pass


class CommuneUpdate(CommuneBase):
    """
    Schéma utilisé pour mettre à jour l'association d'un département à une commune.

    Inclut uniquement la clé étrangère du département pour des mises à jour partielles.
    """

    fk_commune_departement: str | None = Field(
        foreign_key="t_departements.departement_code",
        max_length=2,
        nullable=True,
        description="Nouveau code département mis à jour",
        default=None
        
    )


class CommuneRead(CommuneBase):
    """
    Schéma utilisé pour lire les données de la commune.

    Étend le schéma de base avec l'identifiant de clé primaire.
    """

    commune_id: int | None = Field(
        default=None,
        primary_key=True,
        description="Identifiant unique affiché lors de la lecture"
    )
