from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .commune_model import Commune

class DepartementBase(SQLModel):
    """
    Schéma de base pour représenter les données des départements français.

    Fournit des attributs partagés à travers les variantes de schéma pour les modèles liés aux départements.
    """

    departement_nom: str | None = Field(
        default=None,
        max_length=50,
        nullable=True,
        description="Nom du département français (optionnel, max 50 caractères)"
    )


class Departement(DepartementBase, table=True):
    """
    Modèle ORM mappé à la table 't_departements' de la base de données.

    Inclut le code du département comme clé primaire et une relation avec ses communes.
    """

    __tablename__ = "t_departements"

    departement_code: str | None = Field(
        primary_key=True,
        max_length=2,
        description="Code officiel du département (clé primaire, 2 caractères)"
    )

    communes: list["Commune"] = Relationship(
        back_populates="departement"
    )


class DepartementCreate(DepartementBase):
    """
    Schéma utilisé pour créer un nouveau département.

    Hérite de tous les champs du schéma de base. Utilisé dans les opérations POST.
    """
    pass


class DepartementUpdate(DepartementBase):
    """
    Schéma utilisé pour mettre à jour un département existant.

    Tous les champs sont optionnels, permettant des mises à jour partielles via des requêtes PATCH.
    Cela signifie qu'une combinaison de champs peut être fournie pour la mise à jour.
    """

    departement_nom: str | None = Field(
        default=None,
        description="Nom du département mis à jour (facultatif)."
    )


class DepartementRead(DepartementBase):
    """
    Schéma utilisé pour lire les données d'un département.

    Étend le schéma de base avec un champ de code requis utilisé pour identifier les enregistrements.
    """

    departement_code: str = Field(
        description="Code unique affiché lors de la lecture"
    )
