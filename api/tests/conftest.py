import os
import pytest
from fastapi.testclient import TestClient

from main import app
from api.database.connection import engine
from api.models.taxi_fare_model import Base

test_db_url = "sqlite:///./test.db"

client = TestClient(app)


@pytest.fixture(scope="session", autouse=True)
def setup_database():
    # Criação do banco de dados de teste
    app.state.db = engine(test_db_url)
    Base.metadata.create_all(bind=app.state.db)
    yield
    # Limpeza do banco de dados de teste
    Base.metadata.drop_all(bind=app.state.db)


@pytest.fixture
def test_client():
    return client
