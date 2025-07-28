from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .detail_colis_model import DetailColis

class ColisBase(SQLModel):
    """
    Schéma de base pour représenter les métadonnées d'un colis.

    Inclut des champs partagés tels que le code de suivi, le coût d'affranchissement et un commentaire optionnel.
    Utilisé dans plusieurs schémas d'entrée/sortie.
    """

    colis_code_suivi: str | None = Field(
        default=None,
        max_length=100,
        nullable=True,
        description="Code de suivi du colis (optionnel)"
    )

    colis_timbre: float | None = Field(
        default=None,
        nullable=True,
        description="Valeur du timbre requis pour le colis"
    )

    colis_commentaire: str | None = Field(
        default=None,
        max_length=100,
        nullable=True,
        description="Commentaire facultatif sur le colis"
    )


class Colis(ColisBase, table=True):
    """
    Modèle ORM représentant la table 't_colis' de la base de données.

    Inclut la clé primaire et la relation avec les lignes de détail de colis associées.
    """

    __tablename__ = "t_colis"

    colis_id: int | None = Field(
        default=None,
        primary_key=True,
        description="Identifiant unique du colis"
    )

    details_colis: list["DetailColis"] = Relationship(
        back_populates="colis"
    )


class ColisCreate(ColisBase):
    """
    Schéma utilisé pour créer une nouvelle entrée de colis.

    Hérite de tous les champs requis du schéma de base.
    """
    pass


class ColisUpdate(ColisBase):
    """
    Schéma utilisé pour mettre à jour un colis existant.

    Tous les champs sont optionnels, permettant des mises à jour partielles via des requêtes PATCH.
    Cela signifie qu'une combinaison de champs peut être fournie pour la mise à jour.
    """

    colis_code_suivi: str | None = Field(
        default=None,
        description="Code de suivi mis à jour pour le colis."
    )
    
    colis_timbre: float | None = Field(
        default=None,
        description="Valeur d'affranchissement mise à jour pour le colis."
    )
    
    colis_commentaire: str | None = Field(
        default=None,
        description="Commentaire mis à jour pour le colis."
    )


class ColisRead(ColisBase):
    """
    Schéma utilisé pour lire les données d'un colis.

    Étend le schéma de base en incluant le champ d'identifiant unique.
    """

    colis_id: int = Field(
        description="Identifiant unique affiché lors de la lecture"
    )
