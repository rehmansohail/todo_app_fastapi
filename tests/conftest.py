import pytest
from sqlmodel import SQLModel, create_engine, Session
from fastapi.testclient import TestClient
from main import app
from database import get_session


TEST_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})



@pytest.fixture(name="session")
def session_fixture():
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session
    SQLModel.metadata.drop_all(engine)



@pytest.fixture(name="client")
def client_fixture(session: Session):
    def get_test_session():
        yield session

    app.dependency_overrides[get_session] = get_test_session

    client = TestClient(app)
    yield client

    app.dependency_overrides.clear()