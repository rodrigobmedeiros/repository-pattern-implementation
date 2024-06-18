from pydantic import BaseModel


class ItemBase(BaseModel):
    user_id: int
    item_name: str

    class Config:
        from_attributes = True


class ItemGet(ItemBase):
    item_id: int


class UserBase(BaseModel):
    user_name: str

    class Config:
        from_attributes = True


class UserGet(UserBase):
    user_id: int
    items: list[ItemGet]


class UserPost(UserBase):
    items: list[ItemBase]


class ResponseUserGet(BaseModel):
    data: list[UserGet]
