from datetime import datetime
from typing import Optional

from pydantic import BaseModel, field_validator


class HiredEmployee(BaseModel):
    id: int
    name: Optional[str]
    datetime: Optional[datetime]
    department_id: Optional[int]
    job_id: Optional[int]

    @field_validator("datetime", mode="before")
    def validate_iso_datetime(cls, d: str | datetime) -> datetime:
        if d is datetime:
            try:
                value = datetime.fromisoformat(d)
                return value
            except ValueError:
                raise ValueError("Date should be ISO format.")
        else:
            return d


class Department(BaseModel):
    id: int
    department: str


class Job(BaseModel):
    id: int
    job: str
