from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import session, sessionmaker
from sqlalchemy.sql import text
SQLALCHEMY_DATABASE_URI = "sqlite:///C:\\Users\\lluna\\dbmigration-challenge\\dbmigration-challenge\\app_db.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URI,
    connect_args={"check_same_thread": False},
    echo=True
)

SessionLocal = sessionmaker(
    autoflush=True,
    bind=engine
)

Base = declarative_base()


class DBContext:
    def __init__(self):
        self.db = SessionLocal()
    
    def __enter__(self):
        return self.df

    def __exit__(self, et, ev, traceback):
        self.db.close()