from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .db import Base


class Department(Base):
    __tablename__ = 'departments'

    id = Column(Integer, primary_key=True)
    department = Column(String(60), nullable=False)
    
    employees = relationship("Employee", back_populates="department")


class Job(Base):
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True)
    job = Column(String(60), nullable=False)

    employees = relationship("Employee", back_populates="job")


class Employee(Base):
    __tablename__ = 'employee'

    id = Column(Integer, primary_key=True)
    name = Column(String(60), nullable=True)
    datetime = Column(DateTime, nullable=True)
    department_id = Column(Integer, ForeignKey('departments.id'))
    job_id = Column(Integer, ForeignKey('jobs.id'))

    department = relationship("Department", back_populates="employees")
    job = relationship("Job", back_populates="employees")
