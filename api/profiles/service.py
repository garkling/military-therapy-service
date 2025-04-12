from typing import Annotated

from fastapi import Depends

from api.profiles.models import MilitaryProfile
from api.profiles.repository import MilitaryProfileRepository


class MilitaryProfileService:

    def __init__(
        self,
        repo: Annotated[MilitaryProfileRepository, Depends()]
    ):
        self._repo = repo

    def create(self, user_id: str, profile_create: dict) -> MilitaryProfile:
        profile = MilitaryProfile(user_id=user_id, **profile_create)
        self._repo.create(profile)

        return profile
