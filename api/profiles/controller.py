from typing import Annotated

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from starlette import status

from api.auth.guards import APIGuard
from api.profiles.dto import MilitaryProfileCreate
from api.profiles.dto import MilitaryProfileRead
from api.profiles.dto import MilitaryProfileUpdate
from api.profiles.service import MilitaryProfileService
from api.user.models import Military
from api.user.models import User
from api.user.models import UserRole

router = APIRouter()


class UserProfileController:

    def __init__(
        self,
        military_profile_service: Annotated[MilitaryProfileService, Depends()]
    ):
        self._military_profile_service = military_profile_service

    async def create_profile(self, body: MilitaryProfileCreate, user: Military) -> MilitaryProfileRead:
        created = self._military_profile_service.create(
            user.id,
            body.model_dump()
        )
        return MilitaryProfileRead.model_validate(created)

    async def get_profile(self, user_id: str, user: User) -> MilitaryProfileRead:
        profile = self._military_profile_service.get(user_id)
        return MilitaryProfileRead.model_validate(profile)

    async def update_profile(self, body: MilitaryProfileUpdate, user: User) -> MilitaryProfileRead:
        updated = self._military_profile_service.update(user.id, **body.extract())
        return MilitaryProfileRead.model_validate(updated)


@router.post("/profile", status_code=status.HTTP_201_CREATED, response_model=MilitaryProfileRead)
async def create_profile(
    body: MilitaryProfileCreate,
    user: APIGuard,
    controller: Annotated[UserProfileController, Depends()]
) -> MilitaryProfileRead:
    if user.role != UserRole.MILITARY:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Action is not allowed")

    response = await controller.create_profile(body, user)
    return MilitaryProfileRead.model_validate(response)


@router.get("/{user_id}/profile", status_code=status.HTTP_200_OK, response_model=MilitaryProfileRead)
async def get_profile(
    user_id: str,
    user: APIGuard,
    controller: Annotated[UserProfileController, Depends()]
) -> MilitaryProfileRead:
    if user.id != user_id and user.role not in (UserRole.THERAPIST, UserRole.ADMIN):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")

    response = await controller.get_profile(user_id=user_id, user=user)
    return response


@router.put("/profile", status_code=status.HTTP_200_OK, response_model=MilitaryProfileRead)
async def update_profile(
    body: MilitaryProfileUpdate,
    user: APIGuard,
    controller: Annotated[UserProfileController, Depends()]
) -> MilitaryProfileRead:
    if user.role != UserRole.MILITARY:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Action is not allowed")

    response = await controller.update_profile(body=body, user=user)
    return response
