from sqlmodel import SQLModel, Field, Relationship
from .variation_objet_model import VariationObjet
from .commande_model import Commande
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .detail_commande_model import DetailCommande

class DetailCommandeBase(SQLModel):
    """
    Schéma de base pour représenter les lignes de commande.

    Représente les attributs principaux partagés par toutes les variantes de schéma, y compris les références à
    la commande associée, la quantité d'articles et des commentaires optionnels.
    """

    fk_detail_commande_commande_id: int | None = Field(
        default=None,
        foreign_key="t_commandes.commande_id",
        index=True,
        nullable=True,
        description="Identifiant de la commande associée"
    )

    detail_commande_quantitee: int | None = Field(
        default=1,
        description="Quantité d'objets dans la ligne de commande"
    )

    detail_commande_commentaire: str | None = Field(
        default="",
        max_length=100,
        description="Commentaire facultatif sur cette ligne de commande"
    )

    fk_detail_commande_variation_objet_id: int | None = Field(
        default=None,
        foreign_key="t_variations_objets.variation_objet_id",
        nullable=True,
        description="Identifiant de la variation d'objet associée"
    )


class DetailCommande(DetailCommandeBase, table=True):
    """
    Modèle ORM mappé à la table 't_details_commandes'.

    Inclut la logique de persistance et les relations avec la commande parent et la variation d'objet.
    """

    __tablename__ = "t_details_commandes"

    detail_commande_id: int | None = Field(
        default=None,
        primary_key=True,
        description="Identifiant unique de la ligne de commande"
    )

    commande: Commande = Relationship(
        back_populates="details_commande"
    )

    variation_objet: VariationObjet = Relationship(
        back_populates="details_commandes"
    )

    details_colis: list["DetailColis"] = Relationship(
        back_populates="detail_commande"
    )


class DetailCommandeCreate(DetailCommandeBase):
    """
    Schéma utilisé pour créer une nouvelle ligne de détail de commande.

    Hérite de tous les champs du schéma de base.
    Utilisé pour les opérations POST.
    """
    pass


class DetailCommandeUpdate(DetailCommandeBase):
    """
    Schéma utilisé pour mettre à jour une ligne de détail de commande existante.

    Tous les champs sont optionnels, permettant des mises à jour partielles via des requêtes PATCH.
    Cela signifie qu'une combinaison de champs peut être fournie pour la mise à jour.
    """

    detail_commande_quantitee: int | None = Field(
        default=None,
        nullable=True,
        description="Nouvelle quantité (optionnelle)"
    )

    detail_commande_commentaire: str | None = Field(
        default=None,
        max_length=100,
        nullable=True,
        description="Nouveau commentaire (optionnel)"
    )


class DetailCommandeRead(DetailCommandeBase):
    """
    Schéma utilisé pour lire les enregistrements de lignes de détail de commande.

    Étend le schéma de base avec le champ d'identifiant unique.
    """

    detail_commande_id: int | None = Field(
        default=None,
        primary_key=True,
        description="Identifiant unique affiché lors de la lecture"
    )
