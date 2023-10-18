from typing import List

from sqlalchemy.orm import session
from pydantic import BaseModel, TypeAdapter

import persistence.models as models
import schemas


class FileService():
    lookup_schema = {
        "departments": {
            "schema": schemas.Department,
            "model": models.Department
        },
        "jobs": {
            "schema": schemas.Job,
            "model": models.Job
        },
        "hired_employees": {
            "schema": schemas.HiredEmployee,
            "model": models.Employee
        }
    }

    def __init__(self, db: session):
        self.db = db

    def _validate(self, values: dict, schema: BaseModel):

        return TypeAdapter(List[schema]).validate_python(values)

    def insert_file(self, table: str, values: dict):

        values = self._validate(values, FileService.lookup_schema[table]["schema"])

        self.db.bulk_insert_mappings(
            FileService.lookup_schema[table]["model"], values
        )
        self.db.commit()

