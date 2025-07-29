##################
# Modules import #
##################

import pytest
from fastapi.testclient import TestClient
from sqlmodel import create_engine, Session, SQLModel

###############
# SRC imports #
###############

from src.main import app
from src.database import get_db
from src.models.client_model import Client as ClientModel
from src.models.commune_model import Commune
from src.models.departement_model import Departement

############
# Fixtures #
############

@pytest.fixture(scope="session")
def test_session():
    """
    Crée une base de données SQLite en fichier pour vérifier.
    Initialise les tables, et insère un permet d'insérer des données par défaut.
    """
    db_url = "sqlite:///./test.db"
    engine = create_engine(db_url, echo=False)
    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)
    
    with Session(engine) as session:
        # Création d'un client
        robin = ClientModel(client_prenom="Robin", client_nom="HOTTON", client_adresse1="1 rue de la Paix")
        daniel = ClientModel(client_prenom="Daniel", client_nom="HOTTON", client_adresse1="2 rue de la Paix")
        session.add(robin)
        session.add(daniel)
        
        # Création d'une commune
        wervicq = Commune(commune_ville="Wervicq-Sud", commune_codepostal="59117")
        session.add(wervicq)
        
        # Création d'un département
        nord = Departement(departement_nom="Nord", departement_code="59")
        session.add(nord)
        
        # Association des entités
        daniel.commune = wervicq
        robin.commune = wervicq
        wervicq.departement = nord
        
        # Commit les changements
        session.commit()
        
        # Retourne la session de test
        yield session


@pytest.fixture(scope="function")
def client(test_session):
    """Crée un client FastAPI qui utilise la session de test en override."""
    def override_get_session():
        yield test_session
        
    # Ecrase la connexion à l'ancienne base de données par la nouvelle
    app.dependency_overrides[get_db] = override_get_session

    with TestClient(app) as test_client:
        yield test_client

    app.dependency_overrides.clear()