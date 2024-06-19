from dataclasses import dataclass


@dataclass
class ItemDTO:
    item_id: int
    user_id: int
    item_name: str


@dataclass
class UserDTO:
    user_id: int
    user_name: str
    items: list[ItemDTO]
