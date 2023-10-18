from persistence.db import DBContext


def get_db():
    with DBContext() as db:
        yield db
