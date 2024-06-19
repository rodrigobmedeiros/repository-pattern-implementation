from pydantic import BaseModel


class ItemSchema(BaseModel):
    user_id: int
    item_name: str
    item_id: int

    class Config:
        from_attributes = True


class UserSchema(BaseModel):
    user_name: str
    user_id: int
    items: list[ItemSchema]

    class Config:
        from_attributes = True


class ResponseUserGet(BaseModel):
    data: list[UserSchema]
