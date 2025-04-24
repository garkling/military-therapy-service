from typing import Annotated

from fastapi import APIRouter
from fastapi import Depends
from starlette import status

from api.auth.dto import Auth0UserInfo
from api.auth.guards import APIGuard
from api.auth.guards import FirstLoginGuard
from api.user.dto import MilitaryUserCreate
from api.user.dto import MilitaryUserRead
from api.user.services import MilitaryService
from api.user.services import UserService

router = APIRouter(prefix='/user')


class UserController:

    def __init__(
        self,
        user_service: Annotated[UserService, Depends()],
        military_service: Annotated[MilitaryService, Depends()],
    ):
        self._user_service = user_service
        self._military_service = military_service

    def create_user(self, auth0_info: Auth0UserInfo, user_create: MilitaryUserCreate) -> MilitaryUserRead:
        created = self._military_service.create(
            user_id=auth0_info.id,
            email=auth0_info.email,
            **user_create.model_dump()
        )
        return MilitaryUserRead.model_validate(created)


@router.get("/me", status_code=status.HTTP_200_OK, response_model=MilitaryUserRead)
async def userinfo(
    user: APIGuard,
) -> MilitaryUserRead:
    return MilitaryUserRead.model_validate(user)


@router.post("", status_code=status.HTTP_201_CREATED, response_model=MilitaryUserRead)
async def create_user(
    user_create: MilitaryUserCreate,
    auth0_info: FirstLoginGuard,
    controller: Annotated[UserController, Depends()],
) -> MilitaryUserRead:
    user = await controller.create_user(auth0_info, user_create)
    return user
