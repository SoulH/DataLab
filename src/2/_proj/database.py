from core.data.database import IDatabase
from sqla.database import SQLADatabase


def db_factory() -> IDatabase:
    return SQLADatabase()