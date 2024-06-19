from sqlalchemy import Engine, MetaData
from src.mappers.database import engine


metadata = MetaData()


def create_tables(engine: Engine = engine) -> None:
    metadata.create_all(engine)
