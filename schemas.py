from datetime import datetime

from pydantic import BaseModel, field_validator, StrictInt


class HiredEmployee(BaseModel):
    id: StrictInt
    name: str
    datetime: datetime
    department_id: StrictInt
    job_id: StrictInt


class Department(BaseModel):
    id: int
    department: str


class Job(BaseModel):
    id: int
    job: str
