from sqlmodel import SQLModel, Field

class DetailColis(SQLModel, table=True):
    """Table représentant les détails des colis.
    
    Attributes:
        detail_colis_id (int | None): L'identifiant unique pour le détail du colis (clé primaire).
        fk_detail_commande_id (int | None): L'identifiant de la commande associée (clé étrangère).
        fk_colis_id (int | None): L'identifiant du colis associé (clé étrangère).
        detail_colis_quantitee (int): La quantité d'articles dans le colis (valeur par défaut: 1).
        detail_colis_commentaire (str | None): Commentaires ou détails supplémentaires sur le colis.
    """
    
    __tablename__ = "t_detail_colis"
    
    detail_colis_id: int|None = Field(default="", primary_key=True) 
    fk_detail_commande_id: int | None = Field(default="", foreign_key="t_detail_commandes.detail_commande_id", index=True, nullable=True)
    fk_colis_id: int | None = Field(default="", foreign_key="t_colis.colis_id", index=True, nullable=True)
    detail_colis_quantitee: int = Field(default=1)
    detail_colis_commentaire: str | None = Field(default="", max_length=100)


class DetailColisBase(SQLModel):
    """Base class for creating and reading detail colis data.
    
    Attributes:
        fk_detail_commande_id (int | None): L'identifiant de la commande associée (facultatif).
        fk_colis_id (int | None): L'identifiant du colis associé (facultatif).
        detail_colis_quantitee (int): La quantité d'articles dans le colis (obligatoire).
        detail_colis_commentaire (str | None): Commentaires ou détails supplémentaires sur le colis (facultatif).
    """
    
    fk_detail_commande_id: int | None = None
    fk_colis_id: int | None = None
    detail_colis_quantitee: int
    detail_colis_commentaire: str | None = None


class DetailColisCreate(DetailColisBase):
    """Class for creating new detail colis entries.
    
    Attributes:
        fk_detail_commande_id (int | None): L'identifiant de la commande associée (facultatif).
        fk_colis_id (int | None): L'identifiant du colis associé (facultatif).
        detail_colis_quantitee (int): La quantité d'articles dans le colis (obligatoire).
        detail_colis_commentaire (str | None): Commentaires ou détails supplémentaires sur le colis (facultatif).
    """
    pass  # Direct inheritance, all fields are required except for foreign keys


class DetailColisUpdate(SQLModel):
    """Class for updating existing detail colis entries.
    
    Attributes:
        fk_detail_commande_id (int | None): L'identifiant de la commande associée (facultatif).
        fk_colis_id (int | None): L'identifiant du colis associé (facultatif).
        detail_colis_quantitee (int | None): La quantité d'articles dans le colis (facultatif).
        detail_colis_commentaire (str | None): Commentaires ou détails supplémentaires sur le colis (facultatif).
    """
    
    fk_detail_commande_id: int | None = None
    fk_colis_id: int | None = None
    detail_colis_quantitee: int | None = None
    detail_colis_commentaire: str | None = None


class DetailColisRead(DetailColisBase):
    """Class for reading detail colis entries from the database.
    
    Attributes:
        detail_colis_id (int): L'identifiant unique pour le détail du colis (clé primaire).
        fk_detail_commande_id (int | None): L'identifiant de la commande associée (facultatif).
        fk_colis_id (int | None): L'identifiant du colis associé (facultatif).
        detail_colis_quantitee (int): La quantité d'articles dans le colis (obligatoire).
        detail_colis_commentaire (str | None): Commentaires ou détails supplémentaires sur le colis (facultatif).
    """
    
    detail_colis_id: int
