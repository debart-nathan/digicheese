from sqlmodel import SQLModel, Field

class Colis(SQLModel, table=True):
    """Table representing packages (colis) in the database.
    
    Attributes:
        colis_id (int | None): The unique identifier for the package (primary key).
        colis_code_suivi (str | None): The tracking code for the package.
        colis_timbre (float | None): The value of the postage required for the package.
        detail_colis_commentaire (str | None): Comments or details about the package.
    """
    
    __tablename__ = "t_colis"
    
    colis_id: int | None = Field(default=None, primary_key=True) 
    colis_code_suivi: str | None = Field(default=None, max_length=100, nullable=True)
    colis_timbre: float | None = Field(default=None, nullable=True)  # Value of the postage needed for the package
    detail_colis_commentaire: str | None = Field(default=None, max_length=100, nullable=True)


class ColisBase(SQLModel):
    """Base class for creating and reading package data.
    
    Attributes:
        colis_code_suivi (str): The tracking code for the package (required).
        colis_timbre (float): The value of the postage required for the package (required).
        detail_colis_commentaire (str): Comments or details about the package (required).
    """
    
    colis_code_suivi: str
    colis_timbre: float    
    detail_colis_commentaire: str


class ColisCreate(ColisBase):
    """Class for creating new package entries.
    
    Attributes:
        colis_code_suivi (str): The tracking code for the package (required).
        colis_timbre (float): The value of the postage required for the package (required).
        detail_colis_commentaire (str): Comments or details about the package (required).
    """
    pass  # Direct inheritance, all fields are required


class ColisUpdate(SQLModel):
    """Class for updating existing package entries.
    
    Attributes:
        colis_code_suivi (str | None): The tracking code for the package (optional).
        colis_timbre (float | None): The value of the postage required for the package (optional).
        detail_colis_commentaire (str | None): Comments or details about the package (optional).
    """
    
    colis_code_suivi: str | None = None
    colis_timbre: float | None = None
    detail_colis_commentaire: str | None = None


class ColisRead(ColisBase):
    """Class for reading package entries from the database.
    
    Attributes:
        colis_code_suivi (str): The tracking code for the package (required).
        colis_timbre (float): The value of the postage required for the package (required).
        detail_colis_commentaire (str): Comments or details about the package (required).
        colis_id (int): The unique identifier for the package (primary key).
    """
    colis_id: int
