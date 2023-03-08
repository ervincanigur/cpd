from __future__ import annotations

from enum import Enum

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


# Job
class JobID(BaseModel):
    job_id: str


class Status(Enum):
    PENDING = "pending"
    RUNNING = "running"
    SUCCESS = "success"
    FAILURE = "failure"


class JobStatus(BaseModel):
    status: Status


# Compare Code
class CodeCompareResult(BaseModel):
    status: JobStatus
    result: list[tuple[int, int, float]]
