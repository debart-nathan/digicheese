from sqlmodel import SQLModel, Field



class Colis(SQLModel, table=True):
    """Table représentant les colis."""
    
    __tablename__ = "t_colis"
    
    colis_id: int | None = Field(default=None, primary_key=True) 
    colis_code_suivi: str | None = Field(default=None, max_length=100, nullable=True )
    colis_timbre: float | None = Field(default=None, nullable=True) #value of the timbre needed for the order
    detail_colis_commentaire: str | None = Field(default=None, max_length=100, nullable=True)