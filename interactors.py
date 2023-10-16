from typing import List
from numpy import nan

import pandas as pd
from pydantic import TypeAdapter
from sqlalchemy.orm import session
from sqlalchemy import insert, text

from schemas import Department
import persistence.models as models
from persistence.db import SessionLocal, engine, DBContext
from services.FileService import FileService

df = pd.read_csv("departments.csv", 
                 names=Department.model_fields.keys()).replace(nan, None)

DeptartmentListValidator = TypeAdapter(List[Department])

service = FileService(SessionLocal)
service.insert_departments(values=df.to_dict(orient="records"))