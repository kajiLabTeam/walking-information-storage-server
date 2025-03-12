import sqlalchemy.sql.functions
from sqlalchemy import func


def timestamp() -> sqlalchemy.sql.functions.Function:
    return func.current_timestamp()
