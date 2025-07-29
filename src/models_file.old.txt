from sqlmodel import SQLModel, Field, Relationship
from typing import List
from datetime import date
from decimal import Decimal



class Conditionnement(SQLModel, table=True):
    """Table représentant les conditionnements disponibles pour les objets."""

    __tablename__ = "t_conditionnement"
    
    idcondit: int | None = Field(default=None, primary_key=True)
    libcondit: str | None = Field(default=None, max_length=50, nullable=True)
    poidscondit: int | None = Field(default=None, nullable=True)
    prixcond: Decimal = Field(default=Decimal("0.0000"), nullable=False)
    ordreimp: int | None = Field(default=None, nullable=True)
    
    objets: List["ObjetCond"] = Relationship(back_populates="condit")


class ObjetCond(SQLModel, table=True):
    """Table représentant la relation entre les objets et les conditionnements."""
    
    __tablename__ = "t_rel_cond"
    
    idrelcond: int | None = Field(default=None, primary_key=True, index=True)
    qteobjdeb: int = Field(default=0)
    qteobjfin: int = Field(default=0)
    codobj: int | None = Field(default=None, foreign_key="t_objet.codobj", nullable=True)
    codcond: int | None = Field(default=None, foreign_key="t_conditionnement.idcondit", nullable=True)
    
    objets: Objet | None = Relationship(back_populates="condit")
    condit: Conditionnement | None = Relationship(back_populates="objets")


class DetailObjet(SQLModel, table=True):
    """Table représentant les détails des objets associés aux commandes."""
    
    __tablename__ = "t_dtlcode_codobj"
    
    id: int | None = Field(default=None, primary_key=True)
    detail_id: int | None = Field(default=None, foreign_key="t_dtlcode.id", nullable=True)
    objet_id: int | None = Field(default=None, foreign_key="t_objet.codobj", nullable=True)

class Enseigne(SQLModel, table=True):
    """Table représentant les enseignes que la société travaille avec."""
    
    __tablename__ = "t_enseigne"
    
    id_enseigne: int | None = Field(default=None, primary_key=True)
    lb_enseigne: str | None = Field(default=None, max_length=50, nullable=True)
    ville_enseigne: str | None = Field(default=None, max_length=50, nullable=True)
    dept_enseigne: int = Field(default=0)

class Poids(SQLModel, table=True):
    """Table représentant les poids et timbres associés aux commandes."""
    
    __tablename__ = "t_poids"
    
    id: int | None = Field(default=None, primary_key=True)
    valmin: Decimal | None = Field(default=Decimal("0"), nullable=True)
    valtimbre: Decimal | None = Field(default=Decimal("0"), nullable=True)
    
class Vignette(SQLModel, table=True):
    """Table représentant les vignettes (timbre) avec leurs prix pour un certain poids."""
    
    __tablename__ = "t_poidsv"
    
    id: int | None = Field(default=None, primary_key=True)
    valmin: Decimal | None = Field(default=Decimal("0"), nullable=True)
    valtimbre: Decimal | None = Field(default=Decimal("0"), nullable=True)


class Role(SQLModel, table=True):
    """Table représentant les rôles dans le système."""
    
    __tablename__ = "t_role"
    
    codrole: int | None = Field(default=None, primary_key=True)
    librole: str | None = Field(default=None, max_length=25, nullable=True)

class Utilisateur(SQLModel, table=True):
    """Table représentant les utilisateurs dans le système."""
    
    __tablename__ = "t_utilisateur"
    
    code_utilisateur: int | None = Field(default=None, primary_key=True)
    nom_utilisateur: str | None = Field(default=None, max_length=50, nullable=True)
    prenom_utilisateur: str | None = Field(default=None, max_length=50, nullable=True)
    username: str | None = Field(default=None, max_length=50, nullable=True)
    couleur_fond_utilisateur: int = Field(default=0)
    date_insc_utilisateur: date | None = Field(default=None, nullable=True)

class RoleUtilisateur(SQLModel, table=True):
    """Table d'association entre les utilisateurs et leurs rôles."""
    
    __tablename__ = "t_utilisateur_role"
    
    id: int | None = Field(default=None, primary_key=True)
    utilisateur_id: int | None = Field(default=None, foreign_key="t_utilisateur.code_utilisateur", nullable=True)
    role_id: int | None = Field(default=None, foreign_key="t_role.codrole", nullable=True)
