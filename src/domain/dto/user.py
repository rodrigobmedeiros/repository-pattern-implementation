from dataclasses import dataclass, field


@dataclass
class ItemDTO:
    item_id: int
    user_id: int
    item_name: str


@dataclass
class UserDTO:
    user_id: int
    user_name: str
    items: list[ItemDTO] = field(default_factory=list)
