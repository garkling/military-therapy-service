from typing import Annotated

from fastapi import Depends

from api.user.models import Military
from api.user.models import User
from api.user.repositories.user_repository import UserRepository


class UserService:

    def __init__(
        self,
        repo: Annotated[UserRepository, Depends()]
    ):
        self._repo = repo

    def get(self, user_id: str) -> User | None:
        return self._repo.get(user_id)

    def create(
        self,
        user_id: str,
        email: str,
        **user_create
    ):
        user = Military(
            id=user_id,
            email=email,
            **user_create
        )
        self._repo.create(user)
        return user
