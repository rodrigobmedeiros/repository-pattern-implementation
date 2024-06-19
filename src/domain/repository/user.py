from src.dependencies.route_dependencies import get_session
from src.domain.repository.abstract_repository import AbstractRepository
from src.domain.dto.user import UserDTO
from sqlalchemy.orm import Session


class UserRepository(AbstractRepository):

    def __init__(self, session: Session | None):

        if session is None:
            session = next(get_session())
        self.session = session

    def get(self, id: int) -> UserDTO:
        user = self.session.query(UserDTO).filter(UserDTO.user_id == id).first()
        return user

    def get_all(self) -> list[UserDTO]:
        users = self.session.query(UserDTO).all()
        return users
