from fastapi.testclient import TestClient
import pytest
from src.database import get_db
from src.main import app
from sqlmodel import create_engine, Session, SQLModel


db_url = "sqlite:///./test.db"
engine = create_engine(db_url, echo=False)



@pytest.fixture(scope="function", autouse=True)
def setup_database():
    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)
    yield


def override_get_session():
    testing_session = Session(engine, autocommit=False, autoflush=False)
    try:
        yield testing_session
    finally:
        testing_session.close()


app.dependency_overrides[get_db] = override_get_session


@pytest.fixture(scope="module")
def client():
    return TestClient(app)