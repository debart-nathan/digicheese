from sqlmodel import SQLModel, Field, Relationship
from .colis_model import Colis
from .detail_commande_model import DetailCommande

class DetailColisBase(SQLModel):
    """
    Schéma de base pour créer et lire les enregistrements de détails d'expédition.

    Représente les attributs principaux partagés par toutes les variantes de schéma, y compris les références à
    la commande et au colis associés, la quantité d'articles et des commentaires optionnels.
    """

    fk_detail_commande_id: int | None = Field(
        default=None,
        foreign_key="t_details_commandes.detail_commande_id",
        index=True,
        nullable=True,
        description="Identifiant de la commande associée"
    )

    fk_colis_id: int | None = Field(
        default=None,
        foreign_key="t_colis.colis_id",
        index=True,
        nullable=True,
        description="Identifiant du colis associé"
    )

    detail_colis_quantitee: int | None = Field(
        default=1,
        description="Quantité d'articles dans le colis"
    )

    detail_colis_commentaire: str | None = Field(
        default=None,
        max_length=100,
        description="Commentaire facultatif sur le colis"
    )


class DetailColis(DetailColisBase, table=True):
    """
    Modèle ORM mappé à la table 't_details_colis'.

    Inclut la logique de persistance et les relations avec le détail de commande parent et le colis.
    """

    __tablename__ = "t_details_colis"

    detail_colis_id: int | None = Field(
        default=None,
        primary_key=True,
        description="Identifiant unique du détail du colis"
    )

    detail_commande: DetailCommande = Relationship(
        back_populates="details_colis"
    )

    colis: Colis = Relationship(
        back_populates="details_colis"
    )


class DetailColisCreate(DetailColisBase):
    """
    Schéma utilisé pour créer un nouveau détail de colis.

    Hérite de tous les champs du schéma de base.
    Utilisé pour les opérations POST.
    """
    pass


class DetailColisUpdate(DetailColisBase):
    """
    Schéma utilisé pour mettre à jour un détail de colis existant.

    Tous les champs sont optionnels, permettant des mises à jour partielles via des requêtes PATCH.
    Cela signifie qu'une combinaison de champs peut être fournie pour la mise à jour.
    """

    fk_detail_commande_id: int | None = Field(
        default=None,
        description="Nouvel identifiant de détail de commande (facultatif)."
    )
    
    fk_colis_id: int | None = Field(
        default=None,
        description="Nouvel identifiant de colis (facultatif)."
    )
    
    detail_colis_quantitee: int | None = Field(
        default=None,
        description="Quantité mise à jour (facultatif)."
    )
    
    detail_colis_commentaire: str | None = Field(
        default=None,
        description="Commentaire mis à jour (facultatif)."
    )


class DetailColisRead(DetailColisBase):
    """
    Schéma utilisé pour lire les enregistrements de détails de colis.

    Étend le schéma de base avec le champ d'identifiant unique.
    """

    detail_colis_id: int = Field(
        description="Identifiant unique affiché lors de la lecture"
    )
