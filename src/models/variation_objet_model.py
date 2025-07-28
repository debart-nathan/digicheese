from sqlmodel import SQLModel, Field, Relationship
from decimal import Decimal
from .objet_model import Objet
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .detail_commande_model import DetailCommande

class VariationObjetBase(SQLModel):
    """
    Schéma de base pour gérer les données de variation d'objet.

    Définit les attributs partagés à travers différents schémas liés aux variations d'objet,
    y compris la taille, le poids et une clé étrangère vers l'objet associé.
    """

    variation_objet_taille: str | None = Field(
        default=None,
        max_length=50,
        nullable=True,
        description="Taille de la variation de l'objet (optionnelle, max 50 caractères)"
    )

    variation_objet_poids: Decimal | None = Field(
        default=Decimal("0.0000"),
        nullable=False,
        description="Poids de la variation de l'objet en kilogrammes"
    )

    fk_variation_objet_objet_id: int | None = Field(
        default=None,
        foreign_key="t_objets.objet_id",
        nullable=False,
        description="Identifiant de l'objet associé à cette variation"
    )


class VariationObjet(VariationObjetBase, table=True):
    """
    Modèle ORM mappé à la table 't_variations_objets'.

    Inclut la logique de persistance et les relations avec l'objet parent et les détails de commande associés.
    """

    __tablename__ = "t_variations_objets"

    variation_objet_id: int | None = Field(
        default=None,
        primary_key=True,
        description="Identifiant unique de la variation"
    )

    objet: Objet | None = Relationship(back_populates="variations_objet")
    details_commandes: list["DetailCommande"] = Relationship(back_populates="variation_objet")


class VariationObjetCreate(VariationObjetBase):
    """
    Schéma utilisé pour créer une nouvelle variation d'objet.

    Hérite de tous les champs du schéma de base.
    """
    pass


class VariationObjetUpdate(VariationObjetBase):
    """
    Schéma utilisé pour mettre à jour une variation d'objet existante.

    Permet des mises à jour partielles en remplaçant des champs sélectionnés.
    """

    variation_objet_poids: Decimal | None = Field(
        default=None,
        description="Poids mis à jour de la variation"
    )

    fk_objet_id: int | None = Field(
        default=None,
        description="Nouvel identifiant de l'objet si changement"
    )


class VariationObjetRead(VariationObjetBase):
    """
    Schéma utilisé pour lire les données de variation d'objet.

    Étend le schéma de base avec l'identifiant de variation pour identifier de manière unique les enregistrements.
    """

    variation_objet_id: int | None = Field(
        default=None,
        primary_key=True,
        description="Identifiant unique affiché lors de la lecture"
    )
