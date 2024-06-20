from src.domain.dto.user import ItemDTO, UserDTO
from sqlalchemy import Column, ForeignKey, Integer, Table, Text
from sqlalchemy.orm import relationship
from src.mappers.base import mapper_registry, metadata


item = Table(
    "item",
    metadata,
    Column("item_id", Integer, primary_key=True, autoincrement=True, nullable=False),
    Column("user_id", Integer, ForeignKey("user_app.user_id"), nullable=False),
    Column("item_name", Text, nullable=False),
)


user = Table(
    "user_app",
    metadata,
    Column("user_id", Integer, primary_key=True, autoincrement=True, nullable=False),
    Column("user_name", Text, nullable=False),
)


def start_mappers():
    mapper_registry.map_imperatively(
        UserDTO,
        user,
        properties={
            "items": relationship(
                ItemDTO, cascade="all, delete, delete-orphan", backref="user"
            )
        },
    )
    mapper_registry.map_imperatively(ItemDTO, item)
