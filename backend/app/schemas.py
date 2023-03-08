from __future__ import annotations

from pydantic import BaseModel


# DB
class File(BaseModel):
    id: int
    name: str
    content: str

    class Config:
        orm_mode = True


# Response models
class FileUpload(BaseModel):
    id: int


class FileContent(BaseModel):
    name: str
    content: str
