##################
# Modules import #
##################

from decimal import Decimal
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
from src.models.objet_model import Objet
from src.models.colis_model import Colis
from src.models.variation_objet_model import VariationObjet

############
# Fixtures #
############

@pytest.fixture(scope="session")
def test_session():
    """
    Crée une base de données SQLite en fichier pour vérifier.
    Initialise les tables et insère des données par défaut, incluant un Objet et une VariationObjet.
    """
    db_url = "sqlite:///./test.db"
    engine = create_engine(db_url, echo=False, connect_args={"check_same_thread": False})
    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        # Création des clients
        robin = ClientModel(client_prenom="Robin", client_nom="HOTTON", client_adresse1="1 rue de la Paix")
        daniel = ClientModel(client_prenom="Daniel", client_nom="HOTTON", client_adresse1="2 rue de la Paix")
        session.add_all([robin, daniel])

        # Création de la commune et du département
        wervicq = Commune(commune_ville="Wervicq-Sud", commune_codepostal="59117")
        nord = Departement(departement_nom="Nord", departement_code="59")
        var = Departement(departement_nom="Var", departement_code="83")
        session.add_all([wervicq, nord])
        session.add(var)

        # Création d'un colis
        colis = Colis(colis_code_suivi="1445", colis_timbre=14.5, colis_commentaire="Bien envoyé")
        session.add(colis)

        # Création d'un objet
        magic_sword = Objet(
            objet_libelee="Épée magique",
            objet_points=50
        )

        magic_staff = Objet(
            objet_libelee="Baton magique",
            objet_points=30
        )
        session.add_all([magic_sword,magic_staff])

        # Création d'une variation pour l'objet
        variation = VariationObjet(
            variation_objet_taille="Moyen",
            variation_objet_poids=Decimal("1.2500")
        )
        session.add(variation)

        # Associations
        robin.commune = wervicq
        daniel.commune = wervicq
        wervicq.departement = nord
        variation.objet = magic_staff

        session.flush()
        session.commit()
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