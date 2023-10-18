from sqlalchemy import text
import pandas as pd


def employees_report(conn, year: int):
    stmt = text("""SELECT
    d.department,
    j.job,
    CAST(SUM(CASE WHEN QUARTER(e.datetime) = 1 THEN 1 ELSE 0 END) AS SIGNED) AS Q1,
    CAST(SUM(CASE WHEN QUARTER(e.datetime) = 2 THEN 1 ELSE 0 END) AS SIGNED) AS Q2,
    CAST(SUM(CASE WHEN QUARTER(e.datetime) = 3 THEN 1 ELSE 0 END) AS SIGNED) AS Q3,
    CAST(SUM(CASE WHEN QUARTER(e.datetime) = 4 THEN 1 ELSE 0 END) AS SIGNED) AS Q4
FROM employee e
JOIN departments d ON e.department_id = d.id
JOIN jobs as j ON e.job_id = j.id
WHERE EXTRACT(YEAR FROM datetime) = :y
GROUP BY d.department, j.job
ORDER BY d.department, j.job""")
    result = conn.execute(stmt.bindparams(y=year)).all()

    df = pd.DataFrame(result,
                      columns=["department", "job", "Q1", "Q2", "Q3", "Q4"])

    return df.to_dict(orient='records')


def department_hires(conn, year: int):
    stmt = text("""WITH hires_CTE
AS
(
SELECT department_id, COUNT(*) as hired
FROM employee
WHERE YEAR(datetime) = :y
GROUP BY department_id
)
SELECT
    h.department_id,
    d.department,
    hired
FROM hires_CTE h
JOIN departments d ON department_id = d.id
WHERE hired > (SELECT AVG(hired) FROM hires_CTE)
ORDER BY hired DESC """)

    result = conn.execute(stmt.bindparams(y=year)).all()

    df = pd.DataFrame(result, columns=["id", "department", "hired"])

    return df.to_dict(orient='records')
