from typing import Literal
from src.domain.repository.user import UserRepository
from src.dependencies.route_dependencies import get_session
from src.api.schemas.user import ResponseUserGet
from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session

user_router = APIRouter(prefix="/user", tags=["User Data"])


@user_router.get("", name="Get all users", response_model=ResponseUserGet)
async def users(
    req: Request, session: Session = Depends(get_session)
) -> ResponseUserGet:
    repo = UserRepository(session)
    return {"data": repo.get_all()}


@user_router.get(
    "/{user_id}",
    name="Get user by id",
    response_model=ResponseUserGet,
)
async def user(
    user_id: int, session: Session = Depends(get_session)
) -> ResponseUserGet:
    repo = UserRepository(session)
    return {"data": [repo.get(user_id)]}
