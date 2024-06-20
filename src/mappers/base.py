from sqlalchemy import inspect, Engine, MetaData
from sqlalchemy.orm import registry
from src.mappers.database import engine

mapper_registry = registry()
metadata = MetaData()


def create_tables(engine: Engine = engine) -> None:
    metadata.create_all(engine)


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
