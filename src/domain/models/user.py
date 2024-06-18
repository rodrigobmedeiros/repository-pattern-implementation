from sqlalchemy import Column, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship
from src.mappers.base import Base


class User(Base):
    __tablename__ = "user_app"

    user_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    user_name = Column(Text, nullable=False)
    items = relationship("Item", cascade="all, delete, delete-orphan")


class Item(Base):
    __tablename__ = "item"

    item_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    user_id = Column(Integer, ForeignKey("user_app.user_id"), nullable=False)
    item_name = Column(Text, nullable=False)
