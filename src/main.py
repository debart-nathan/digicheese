from fastapi import FastAPI, HTTPException, status
from sqlmodel import SQLModel, select, Session

from .database import get_db, engine

from .routers import (
    router_commande,
    router_client,
    router_colis,
    router_commune,
    router_detail_colis,
    router_departement,
    router_detail_commande,
    router_objet,
    router_variation_objet
)

app = FastAPI()


routers = [
    router_commande,
    router_client,
    router_colis,
    router_commune,
    router_detail_colis,
    router_departement,
    router_detail_commande,
    router_objet,
    router_variation_objet
]

for router in routers:
    app.include_router(router)

SQLModel.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Welcome to the API! Visit /docs for documentation."}


@app.get("/coffee")
def read_cofee():
    raise HTTPException(status_code=status.HTTP_418_IM_A_TEAPOT, detail="I'm a teapot!")