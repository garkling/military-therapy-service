from typing import Annotated

from fastapi import Depends

from api.profiles.models import MilitaryProfile
from api.profiles.repository import MilitaryProfileRepository
from api.utils.utils import get_current_date_iso_string


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

    def get(self, user_id: str) -> MilitaryProfile:
        profile = self._repo.get(user_id)
        return profile

    def update(self, user_id: str, **updates) -> MilitaryProfile:
        profile = self._repo.get(user_id)
        profile.update_attributes(**updates)
        profile.updated_at = get_current_date_iso_string()
        updated = self._repo.update(profile)
        return updated
