from sqlalchemy import inspect
from sqlalchemy.orm import declarative_base
from src.mappers.database import engine

Base = declarative_base()


def orm_as_dict(orm_model):
    """
    Convert an ORM model instance to a dictionary.

    Args:
        orm_model: The ORM model instance to convert.

    Returns:
        dict: A dictionary representation of the ORM model instance, where the
        keys are the column names and the values are the corresponding attribute values.
    """
    return {
        c.key: getattr(orm_model, c.key) for c in inspect(orm_model).mapper.column_attrs
    }


def create_tables():
    """
    Creates database tables based on the defined metadata and binds them to the engine.

    This function should be called to create the necessary tables in the database before using them.

    Parameters:
        None

    Returns:
        None
    """
    Base.metadata.create_all(bind=engine)
