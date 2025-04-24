from typing import Annotated

from fastapi import Depends

from api.user.models import Military
from api.user.models import Therapist
from api.user.models import User
from api.user.repositories import MilitaryRepository
from api.user.repositories import TherapistRepository


class UserService:

    def __init__(
        self,
        military_repo: Annotated[MilitaryRepository, Depends(MilitaryRepository)],
        therapist_repo: Annotated[TherapistRepository, Depends(TherapistRepository)],
    ):
        self._therapist_repo = therapist_repo
        self._military_repo = military_repo

    def get(self, user_id: str) -> Military | Therapist | None:
        return (self._military_repo.get(user_id)
                or self._therapist_repo.get(user_id))


class MilitaryService:

    def __init__(
        self,
        repo: Annotated[MilitaryRepository, Depends()]
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
