from typing import Literal
from src.api.dependencies.route_dependencies import get_session
from src.api.schemas.user import ResponseUserGet, UserGet
from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from src.domain.models.user import User

user_router = APIRouter(prefix="/user", tags=["User Data"])


@user_router.get("", name="Get all users", response_model=ResponseUserGet)
async def users(
    req: Request, session: Session = Depends(get_session)
) -> dict[Literal["data"], list[UserGet]]:
    db_users = session.query(User).all()
    users = [UserGet.model_validate(user) for user in db_users]
    return {"data": users}


@user_router.get(
    "/{user_id}",
    name="Get user by id",
    response_model=ResponseUserGet,
)
async def user(
    user_id: int, session: Session = Depends(get_session)
) -> dict[Literal["data"], list[UserGet]]:
    db_users = session.query(User).get(user_id)
    users = [UserGet.model_validate(user) for user in db_users]
    return {"data": users}
