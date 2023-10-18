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
        if d is str:
            try:
                value = datetime.fromisoformat(d)
                return value.strftime('%Y-%m-%d %H:%M:%S')
            except ValueError:
                raise ValueError("Date should be ISO format.")
        elif d is datetime:
            return d.strftime('%Y-%m-%d %H:%M:%S')
        else:
            return d


class Department(BaseModel):
    id: int
    department: str


class Job(BaseModel):
    id: int
    job: str
