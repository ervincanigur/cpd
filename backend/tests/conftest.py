from __future__ import annotations

from collections.abc import Generator

import pytest
from app.database import Base
from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import Session


@pytest.fixture(scope="session")
def db_engine() -> Generator[Engine, None, None]:
    engine = create_engine("sqlite://", connect_args={"check_same_thread": False})
    Base.metadata.create_all(bind=engine)
    yield engine


@pytest.fixture(scope="function")
def session(db_engine: Engine) -> Generator[Session, None, None]:
    connection = db_engine.connect()
    transaction = connection.begin()
    db = Session(bind=connection)
    try:
        yield db
    finally:
        db.close()
        transaction.rollback()
        connection.close()
