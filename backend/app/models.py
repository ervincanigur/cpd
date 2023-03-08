from __future__ import annotations

from sqlalchemy import Column
from sqlalchemy import Float
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from .database import Base


class File(Base):
    __tablename__ = "files"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    content = Column(String)


class CodeCompare(Base):
    __tablename__ = "code_compare"
    id = Column(Integer, primary_key=True, index=True)
    file1_id: File = relationship("File", back_populates="code_compare")
    file2_id: File = relationship("File", back_populates="code_compare")
    confidence = Column(Float)
