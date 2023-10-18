# Database Migration Challenge

## Overview

This is an implementation of an HTTP API intended to be used as an interface for csv file uploading, in the context of a database migration.
In addition, it includes two endpoints to query metrics about the hirings by Q from the staff and the departments hiring on a given year.

## Prerequisites

The app and a MySQL database are containarized with docker compose, which is the only requisite to run this application.

### Installation

Steps:
* Clone this repository
```
git clone https://github.com/Leandro-Luna/dbmigration-challenge.git
```
* Then move into the repository folder
```
cd dbmigration-challenge
```
* Build and run the app:
```
docker-compose up
```

## Usage

After running the app contatiner, it will be ready to be used in [localhost](http://localhost:80)

The main page shows the Swagger UI, but all the endpoint could be reached from any client.

Endpoints included:
* /migrations/{table_name} -> table_name must be one of (departments, hired_employees, jobs)
* /metrics/employees_hires_report_Q{?year} -> year to be summarized, default=2021
* /metrics/employees_hires_report_Q{?year} -> year to be summarized, default=2021

For the migrations endpoint, a table name must be given, representing the table to be migrated to a new database.
First the jobs and departments tables have to be uploaded, and then the hired_employees tables, this is due to the Foreign Key Constraints present on the hired_employee table.
