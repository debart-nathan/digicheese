from sqlmodel import SQLModel, Field, Relationship
import datetime
from .client_model import Client
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .detail_commande_model import DetailCommande

class CommandeBase(SQLModel):
    """
    Schéma de base pour représenter les commandes des clients.

    Encapsule les champs partagés, y compris les métadonnées de la commande, les valeurs financières,
    et les références au client associé.
    """

    commande_date: datetime.date | None = Field(
        default=None,
        nullable=True,
        description="Date à laquelle la commande a été passée"
    )

    fk_client_id: int | None = Field(
        default=None,
        foreign_key="t_clients.client_id",
        nullable=True,
        description="Identifiant du client associé à la commande"
    )

    client_timbre: float | None = Field(
        default=None,
        nullable=True,
        description="Valeur des timbres envoyés par le client"
    )

    commande_timbre: float | None = Field(
        default=None,
        nullable=True,
        description="Valeur des timbres requis pour la commande"
    )

    client_cheque: float | None = Field(
        default=None,
        nullable=True,
        description="Montant du chèque envoyé par le client"
    )

    commande_commentaire: str | None = Field(
        default="",
        max_length=255,
        nullable=True,
        description="Commentaire facultatif concernant la commande"
    )


class Commande(CommandeBase, table=True):
    """
    Modèle ORM mappé à la table 't_commandes' de la base de données.

    Inclut des relations avec le client et les détails de la commande associés.
    """

    __tablename__ = "t_commandes"

    commande_id: int | None = Field(
        default=None,
        primary_key=True,
        description="Identifiant unique de la commande"
    )

    client: Client = Relationship(
        back_populates="commandes"
    )

    details_commande: list["DetailCommande"] = Relationship(
        back_populates="commande"
    )


class CommandeCreate(CommandeBase):
    """
    Schéma utilisé pour créer une nouvelle commande.

    Hérite de tous les champs du schéma de base et est utilisé lors des requêtes POST.
    """
    pass


class CommandeUpdate(CommandeBase):
    """
    Schéma utilisé pour mettre à jour une commande existante.

    Tous les champs sont optionnels pour prendre en charge les mises à jour partielles via PUT/PATCH.
    """
    pass


class CommandeRead(CommandeBase):
    """
    Schéma utilisé pour récupérer les données de commande.

    Étend le schéma de base avec un champ d'identifiant.
    """

    commande_id: int | None = Field(
        default=None,
        primary_key=True,
        description="Identifiant unique affiché lors de la lecture"
    )
