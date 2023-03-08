from __future__ import annotations

import os

from sqlalchemy import create_engine
from sqlalchemy import URL
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_HOST = os.environ.get("DB_HOST")
DB_DATABASE = os.environ.get("DB_DATABASE")

db_url = URL.create(
    "postgresql",
    username=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    database=DB_DATABASE,
)
db_url_str = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_DATABASE}"

Base = declarative_base()
engine = create_engine(
    db_url,
    pool_pre_ping=True,
    pool_recycle=3600,
    pool_size=20,
    max_overflow=40,
)


def get_session() -> Session:
    session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    with session() as session:
        yield session
