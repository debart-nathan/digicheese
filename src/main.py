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
    router_detail_commande
)

app = FastAPI()

app.include_router(router_commande)
app.include_router(router_client)
app.include_router(router_colis)
app.include_router(router_commune)
app.include_router(router_detail_colis)
app.include_router(router_departement)
app.include_router(router_detail_commande)

SQLModel.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

@app.get("/coffee")
def read_cofee():
    raise HTTPException(status_code=status.HTTP_418_IM_A_TEAPOT)