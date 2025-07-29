from sqlmodel import SQLModel, Field, Relationship
from .commune_model import Commune
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .commande_model import Commande

class ClientBase(SQLModel):
    """
    Schéma de base pour représenter les métadonnées du client.

    Utilisé dans toutes les variantes de création, mise à jour et lecture des clients.
    Inclut des informations personnelles, des champs d'adresse et un statut d'abonnement à la newsletter optionnel.
    """

    client_genre: str | None = Field(
        default=None,
        max_length=8,
        description="Genre ou civilité du client (ex: Monsieur, Madame)"
    )

    client_nom: str | None = Field(
        default=None,
        max_length=40,
        index=True,
        description="Nom de famille du client, sera mis en majuscules."
    )

    client_prenom: str | None = Field(
        default=None,
        max_length=30,
        description="Prénom du client, sera capitalisé."
    )

    client_adresse1: str | None = Field(
        default=None,
        max_length=50,
        description="Adresse principale du client"
    )

    client_adresse2: str | None = Field(
        default=None,
        max_length=50,
        nullable=True,
        description="Complément d'adresse (facultatif)"
    )

    client_adresse3: str | None = Field(
        default=None,
        max_length=50,
        nullable=True,
        description="Deuxième complément d'adresse (facultatif)"
    )

    fk_commune_id: int | None = Field(
        default=None,
        foreign_key="t_communes.commune_id",
        nullable=True,
        description="Identifiant de la commune du client"
    )

    client_telephone_fix: str | None = Field(
        default=None,
        max_length=10,
        nullable=True,
        description="Numéro de téléphone fixe (facultatif)"
    )

    client_telephone_portable: str | None = Field(
        default=None,
        max_length=10,
        nullable=True,
        description="Numéro de téléphone portable (facultatif)"
    )

    client_email: str | None = Field(
        default=None,
        max_length=255,
        nullable=True,
        description="Adresse email du client (facultative)"
    )

    client_newsletter: int | None = Field(
        default=None,
        nullable=True,
        description="Inscription à la newsletter (0 = non, 1 = oui)"
    )


class Client(ClientBase, table=True):
    """
    Modèle ORM mappé à la table 't_clients'.

    Représente les clients du programme de fidélité et inclut des relations avec leur commune et leurs commandes.
    """

    __tablename__ = "t_clients"

    client_id: int | None = Field(
        default=None,
        primary_key=True,
        description="Identifiant unique du client"
    )

    commandes: list["Commande"] = Relationship(
        back_populates="client"
    )

    commune: Commune = Relationship(
        back_populates="clients"
    )


class ClientCreate(ClientBase):
    """
    Schéma pour créer un nouveau client.

    Utilisé pour les requêtes POST avec tous les champs requis.
    """
    pass


class ClientUpdate(ClientBase):
    """
    Schéma pour mettre à jour un client existant.

    Tous les champs sont optionnels pour permettre des mises à jour partielles via PUT ou PATCH.
    """
    pass


class ClientRead(ClientBase):
    """
    Schéma utilisé pour récupérer les données d'un client.

    Étend le schéma de base avec un champ de clé primaire pour l'identification.
    """

    client_id: int | None = Field(
        default=None,
        primary_key=True,
        description="Identifiant unique affiché lors de la lecture"
    )
