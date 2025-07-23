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

from .routers.commande_router import router as commande_router

app = FastAPI()
app.include_router(commande_router)
SQLModel.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"Hello": "World"}