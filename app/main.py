from fastapi import FastAPI

from .dependencies import get_db
from .routers import migrations, metrics


description= r"""
Database Migration Challenge

## Use Cases

* File Upload
* Metrics 

## File Upload
You can upload a .csv file with the data to be migrated to a new MySQL Database

## Metrics
You can query:
* Number of employees hired for each job and department divided by quarter
* Data about employees hired by departments that hired the top 50% of employees 
"""

tags_metadata = [
    {
        "name": "migrations",
        "description": "Allows file upload of .csv files, given the table name, to be uploaded to a new database",
    },
    {
        "name": "metrics",
        "description": "Main endpoint for querying reports"
    }
]
app = FastAPI(
    title="DBMigragrion-Challenge",
    description=description,
    docs_url="/"
    )

app.include_router(migrations.router)
app.include_router(metrics.router)
