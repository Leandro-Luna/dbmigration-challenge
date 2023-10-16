from typing import List

from sqlalchemy import insert
from sqlalchemy.orm import session
from pydantic import BaseModel, TypeAdapter

import persistence.models as models
import schemas


class FileService():
    
    def __init__(self, Session: session):
        self.Session = Session
    
    def _validate(self, values: dict, schema: BaseModel):
        
        TypeAdapter(List[schema]).validate_python(values)

    def insert_departments(self, values: dict):

        self._validate(values, schemas.Department)            

        with self.Session() as ss:
            ss.bulk_insert_mappings(models.Department, values)
            ss.commit()
    



