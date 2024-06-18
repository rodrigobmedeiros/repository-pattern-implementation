from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.config import settings


def create_engine_and_session(database_url):
    """
    Creates an engine and session for the specified database URL.

    Args:
        database_url (str): The URL of the database.

    Returns:
        engine (sqlalchemy.engine.Engine): The SQLAlchemy engine object.
        SessionLocal (sqlalchemy.orm.session.Session): The SQLAlchemy session object.

    """
    engine = create_engine(database_url)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return engine, SessionLocal


engine, SessionLocal = create_engine_and_session(settings.SQLALCHEMY_DATABASE_URL)
