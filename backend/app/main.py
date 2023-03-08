from __future__ import annotations

from typing import Any

from fastapi import Depends
from fastapi import FastAPI
from fastapi import File
from fastapi import HTTPException
from fastapi import UploadFile
from sqlalchemy.orm import Session

from .database import get_session
from .schemas import File as FileSchema
from .schemas import FileContent
from .schemas import FileUpload

app = FastAPI(
    title="CPD",
    description="CPD API",
    docs_url="/api/docs",
    openapi_url="/api/openapi.json",
)


@app.post("/upload_file", response_model=FileUpload)
def upload_file(
    session: Session = Depends(get_session),
    files: list[UploadFile] = File(...),
) -> Any:
    uploaded_files: list[FileUpload] = []
    for file in files:
        new_file: FileSchema = FileSchema(name=file.filename, content=file.file.read())
        session.add(new_file)
        upload_file.append(new_file.id)
    session.commit()
    return uploaded_files


@app.get("/file_content", response_model=FileContent)
def get_file_content(id: int, session: Session = Depends(get_session)) -> Any:
    file: FileSchema = session.query(FileSchema).filter(FileSchema.id == id).first()
    if file is None:
        raise HTTPException(status_code=404, detail="File not found")
    return FileContent(name=file.name, content=file.content)
