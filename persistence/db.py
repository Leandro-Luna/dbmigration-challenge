from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import session, sessionmaker
from sqlalchemy.sql import text
import os
from os.path import join, dirname
# from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
# load_dotenv(dotenv_path)

DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("MYSQL_ROOT_PASSWORD")
DB_DATABASE = os.environ.get("MYSQL_DATABASE")
DB_HOST =  os.environ.get("DB_HOST")
SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:3306/{DB_DATABASE}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URI,
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
        return self.db

    def __exit__(self, et, ev, traceback):
        self.db.close()