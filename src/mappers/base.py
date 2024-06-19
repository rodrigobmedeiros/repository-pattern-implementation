from sqlalchemy import inspect
from sqlalchemy.orm import declarative_base, registry
from src.mappers.database import engine

Base = declarative_base()
mapper_registry = registry()


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
