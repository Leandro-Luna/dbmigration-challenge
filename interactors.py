from typing import List
from numpy import nan

import pandas as pd
from pydantic import TypeAdapter
from sqlalchemy.orm import session
from sqlalchemy import insert

from schemas import Department
import persistence.models as models
from persistence.db import SessionLocal, engine, DBContext


df = pd.read_csv("departments.csv", 
                 names=Department.model_fields.keys()).replace(nan, None)

DeptartmentListValidator = TypeAdapter(List[Department])

# print(df.to_dict(orient='records'))
ls = (DeptartmentListValidator.validate_python(df.to_dict(orient="records")))

with SessionLocal() as db:    
    db.execute(
        insert(models.Department),
        [obj.model_dump() for obj in ls]
    )
# print([obj.model_dump() for obj in ls])