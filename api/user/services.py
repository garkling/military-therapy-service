from typing import Annotated

from fastapi import Depends
from fastapi import HTTPException
from starlette import status

from api.profiles.repository import TherapistExpertiseRepository
from api.user.models import Military
from api.user.models import Therapist
from api.user.models import UserRole
from api.user.repositories import MilitaryRepository
from api.user.repositories import TherapistRepository
from api.utils.utils import get_current_date_iso_string


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

    def list_by_ids(self, user_ids: list[str]) -> list[Military | Therapist]:
        therapists = self._therapist_repo.batch_get(user_ids)
        militaries = self._military_repo.batch_get(user_ids)
        return [*therapists, *militaries]

    def delete(self, user_id: str) -> Military | Therapist | None:
        user = self.get(user_id)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

        if user.role == UserRole.THERAPIST:
            self._therapist_repo.delete(user)
        if user.role == UserRole.MILITARY:
            self._military_repo.delete(user)

        return user


class MilitaryService:

    def __init__(
        self,
        repo: Annotated[MilitaryRepository, Depends()]
    ):
        self._repo = repo

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

    def update(
        self,
        user_id: str,
        **updates
    ) -> Military:
        military = self._repo.get(user_id)
        military.update_attributes(**updates)
        military.updated_at = get_current_date_iso_string()
        self._repo.update(military)
        return military


class TherapistService:
    def __init__(
        self,
        repo: Annotated[TherapistRepository, Depends()],
        expertise_repo: Annotated[TherapistExpertiseRepository, Depends()]
    ):
        self._therapist_repo = repo
        self._expertise_repo = expertise_repo

    def create(
        self,
        user_id: str,
        email: str,
        **user_create
    ):
        expertises = user_create.pop("expertises", None)
        user = Therapist(
            id=user_id,
            email=email,
            **user_create
        )
        user = self._therapist_repo.create(user)
        self.update_expertises(user, expertises)
        return user

    def update(
        self,
        user_id: str,
        **updates
    ) -> Therapist:
        therapist = self._therapist_repo.get(user_id)
        self.update_expertises(therapist, updates.pop('expertises', None))
        therapist.update_attributes(**updates)
        therapist.updated_at = get_current_date_iso_string()
        self._therapist_repo.update(therapist)
        return therapist

    def update_expertises(self, user: Therapist, expertises: list[int] | None):
        if not expertises:
            return user

        user.expertises = self._expertise_repo.get_by_codes(expertises)
        self._therapist_repo.update(user)
        return user

    def list(self):
        return self._therapist_repo.list()
