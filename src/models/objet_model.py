from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .variation_objet_model import VariationObjet

class ObjetBase(SQLModel):
    """
    Schéma de base pour représenter les données d'objet.

    Représente les attributs principaux partagés par toutes les variantes de schéma, y compris le libellé
    et le nombre de points associés à l'objet.
    """

    objet_libelee: str | None = Field(
        default=None,
        max_length=50,
        nullable=True,
        description="Libellé de l'objet (optionnel, max 50 caractères)"
    )

    objet_points: int | None = Field(
        default=0,
        nullable=False,
        description="Nombre de points attribués à l'objet"
    )


class Objet(ObjetBase, table=True):
    """
    Modèle ORM mappé à la table 't_objets' dans la base de données.

    Inclut la logique de persistance et les relations avec les variations d'objet.
    """

    __tablename__ = "t_objets"

    objet_id: int | None = Field(
        default=None,
        primary_key=True,
        description="Identifiant unique de l'objet"
    )

    variations_objet: list["VariationObjet"] = Relationship(
        back_populates="objet"
    )


class ObjetCreate(ObjetBase):
    """
    Schéma utilisé pour créer un nouvel objet.

    Hérite de tous les champs du schéma de base.
    Utilisé pour les opérations POST.
    """
    pass


class ObjetUpdate(ObjetBase):
    """
    Schéma utilisé pour mettre à jour un objet existant.

    Tous les champs sont optionnels, permettant des mises à jour partielles via des requêtes PATCH.
    Cela signifie qu'une combinaison de champs peut être fournie pour la mise à jour.
    """

    objet_points: int | None = Field(
        default=0,
        nullable=True,
        description="Nouvelle valeur en points pour l'objet"
    )


class ObjetRead(ObjetBase):
    """
    Schéma utilisé pour lire les données d'objet.

    Étend le schéma de base avec le champ d'identifiant unique.
    """

    objet_id: int | None = Field(
        default=None,
        primary_key=True,
        description="Identifiant unique affiché lors de la lecture"
    )
