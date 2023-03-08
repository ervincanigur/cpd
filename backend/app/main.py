from __future__ import annotations

from typing import Any

from fastapi import FastAPI
from fastapi import UploadFile

from .schemas import FileContent
from .schemas import FileUpload

app = FastAPI(
    title="CPD",
    description="CPD API",
    docs_url="/api/docs",
    openapi_url="/api/openapi.json",
)


@app.post("/upload_file", response_model=FileUpload)
def upload_file(file: UploadFile) -> Any:
    pass


@app.get("/file_content", response_model=FileContent)
def get_file_content(id: int) -> Any:
    pass
