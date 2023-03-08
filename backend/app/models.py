from __future__ import annotations

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from .database import Base


class File(Base):
    __tablename__ = "files"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    content = Column(String)
