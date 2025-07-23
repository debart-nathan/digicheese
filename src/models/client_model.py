from sqlmodel import SQLModel, Field

class Client(SQLModel, table=True):
    """Table représentant les clients de la fidélisation de la fromagerie."""
    
    __tablename__ = "t_clients"
    
    client_id: int | None = Field(default=None, primary_key=True)
    client_genre: str | None = Field(default=None, max_length=8, nullable=True)
    client_nom: str | None = Field(default=None, max_length=40, index=True, nullable=True)
    client_prenom: str | None = Field(default=None, max_length=30, nullable=True)
    client_adresse1: str | None = Field(default=None, max_length=50, nullable=True)
    client_adresse2: str | None = Field(default=None, max_length=50, nullable=True)
    client_adresse3: str | None = Field(default=None, max_length=50, nullable=True)
    fk_commune_id: int | None = Field(default=None, foreign_key="t_communes.commune_id", nullable=True)
    client_telephone_fix: str | None = Field(default=None, max_length=10, nullable=True)
    client_telephone_portable: str | None = Field(default=None, max_length=10, nullable=True)
    client_email: str | None = Field(default=None, max_length=255, nullable=True)
    client_newsletter: int | None = Field(default=None, nullable=True)

class ClientBase(SQLModel):
    """Schéma abstrait de la classe Client

    Args:
        SQLModel (class): _description_
    """
    client_genre: str
    client_nom: str
    client_prenom: str
    client_adresse1: str
    client_adresse2: str
    client_adresse3: str
    fk_commune_id: int
    client_telephone_fix: str
    client_telephone_portable: str
    client_email: str
    client_newsletter: int

class ClientCreate(ClientBase):
    """Schéma pour la création d'un client

    Args:
        ClientBase (class): _description_
    """
    pass


class ClientUpdate(SQLModel):
    """_summary_

    Args:
        SQLModel (_type_): _description_
    """
    client_genre: str | None = None
    client_nom: str | None = None
    client_prenom: str | None = None
    client_adresse1: str | None = None
    client_adresse2: str | None = None
    client_adresse3: str | None = None
    fk_commune_id: int | None = None
    client_telephone_fix: str | None = None
    client_telephone_portable: str | None = None
    client_email: str | None = None
    client_newsletter: int | None = None

class ClientRead(ClientBase):
    """_summary_

    Args:
        ClientBase (_type_): _description_
    """
    client_id: int
