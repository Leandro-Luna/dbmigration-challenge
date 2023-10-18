import io

from fastapi import APIRouter, HTTPException, Depends, UploadFile, Response, status
from sqlalchemy.orm import session

from ..dependencies import get_db
from services.ReportingService import employees_report, department_hires

router = APIRouter(
    prefix="/metrics",
    tags=["metrics"],
    responses={404: {"description": "Not foound"}}
)


@router.get("/employees_hires_report_Q")
def get_employees_hired_Q(year: int = 2021, db=Depends(get_db)):
    result = employees_report(db, year)
    return {"rows": result}


@router.get("/department_hires")
def get_department_hires(year: int=2021, db=Depends(get_db)):
    result = department_hires(db, year)
    return {"rows": result}

    
@router.get("/")
def base():
    return "Send requests to /employees_hires_report_Q and /department_hires"
