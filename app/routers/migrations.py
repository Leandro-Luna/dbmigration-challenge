import io

from fastapi import APIRouter, HTTPException, Depends, UploadFile, Response, status
from sqlalchemy.orm import session
import pandas as pd
from numpy import nan

from ..dependencies import get_db
from services.FileService import FileService

router = APIRouter(
    prefix="/migrations",
    tags=["migrations"],
    responses={404: {"description": "Not foound"}}
)


@router.post("/{table}")
async def upload_file(table: str, file: UploadFile, db=Depends(get_db)):
    if table not in ("departments", "jobs", "hired_employees"):
        raise HTTPException(404, detail="Table not found")
    service = FileService(db)

    contents = await file.read()

    # Create a memory buffer and write the contents to it
    buffer = io.BytesIO(contents)

    schema = FileService.lookup_schema[table]['schema']
    df = pd.read_csv(buffer,
                    names=schema.model_fields.keys()).replace(nan, None)

    service.insert_file(table=table, values=df.to_dict(orient='records'))
    return Response(
        status_code=status.HTTP_201_CREATED,
        content='File uploaded successfully')


@router.get("/")
def base():
    return "Endpoint for uploading csv files of tables. Add the name of the table to be uploades"