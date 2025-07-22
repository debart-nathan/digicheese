from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, select, Session

from .database import get_db, engine
from .models_file import (
    Departement,
    Commune,
    Client,
    Conditionnement,
    Objet,
    ObjetCond,
    Detail,
    DetailObjet,
    Enseigne,
    Poids,
    Role,
    Utilisateur,
    RoleUtilisateur
)

from .models import commande

app = FastAPI()
SQLModel.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"Hello": "World"}