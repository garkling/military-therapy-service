from typing import Annotated

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from starlette import status

from api.auth.dto import Auth0UserInfo
from api.auth.guards import APIGuard
from api.auth.guards import FirstLoginGuard
from api.errors import ErrorHandlingRoute
from api.user.dto import MilitaryUserCreate
from api.user.dto import MilitaryUserRead
from api.user.dto import TherapistCreate
from api.user.dto import TherapistUserRead
from api.user.dto import UserRead
from api.user.dto import UserReadType
from api.user.dto import UserUpdate
from api.user.models import User
from api.user.models import UserRole
from api.user.services import MilitaryService
from api.user.services import TherapistService
from api.user.services import UserService

router = APIRouter(prefix='/users', route_class=ErrorHandlingRoute)


class UserController:

    def __init__(
        self,
        user_service: Annotated[UserService, Depends()],
        therapist_service: Annotated[TherapistService, Depends()],
        military_service: Annotated[MilitaryService, Depends()],
    ):
        self._user_service = user_service
        self._therapist_service = therapist_service
        self._military_service = military_service

    async def create_user(self, auth0_info: Auth0UserInfo, user_create: MilitaryUserCreate) -> MilitaryUserRead:
        created = self._military_service.create(
            user_id=auth0_info.id,
            email=auth0_info.email,
            **user_create.model_dump()
        )
        return MilitaryUserRead.model_validate(created)

    async def update_user(self, body: UserUpdate, user: User) -> UserRead:
        if user.role == UserRole.MILITARY:
            updated = self._military_service.update(user.id, **body.extract())
        elif user.role == UserRole.THERAPIST:
            updated = self._therapist_service.update(user.id, **body.extract())
        else:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Not enough permissions')

        return UserRead.validate_python(updated)

    async def delete_user(self, user_id: str):
        self._user_service.delete(user_id)

    async def create_therapist(self, body: TherapistCreate) -> TherapistUserRead:
        therapist = self._therapist_service.create(**body.extract())
        return TherapistUserRead.model_validate(therapist)

    async def get_therapists(self) -> list[TherapistUserRead]:
        therapists = self._therapist_service.list()
        return [TherapistUserRead.model_validate(th) for th in therapists]


@router.get("/me", status_code=status.HTTP_200_OK, response_model=UserReadType)
async def userinfo(
    user: APIGuard,
) -> UserReadType:
    return UserRead.validate_python(user)


@router.post("", status_code=status.HTTP_201_CREATED, response_model=MilitaryUserRead)
async def create_user(
    user_create: MilitaryUserCreate,
    auth0_info: FirstLoginGuard,
    controller: Annotated[UserController, Depends()],
) -> MilitaryUserRead:
    user = await controller.create_user(auth0_info, user_create)
    return user


@router.put("", status_code=status.HTTP_200_OK, response_model=UserReadType)
async def update_user(
    user: APIGuard,
    body: UserUpdate,
    controller: Annotated[UserController, Depends()],
) -> UserReadType:
    response = await controller.update_user(body, user)
    return response


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
    user_id: str,
    user: APIGuard,
    controller: Annotated[UserController, Depends()],
):
    if user_id != user.id and user.role != UserRole.ADMIN:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Not enough permissions')

    await controller.delete_user(user_id)


@router.post("/therapists", status_code=status.HTTP_201_CREATED, response_model=TherapistUserRead)
async def create_therapist(
    user: APIGuard,
    body: TherapistCreate,
    controller: Annotated[UserController, Depends()],
) -> TherapistUserRead:
    # if user.role != UserRole.ADMIN:
    #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Not enough permissions')

    response = await controller.create_therapist(body)
    return response


@router.get("/therapists", status_code=status.HTTP_200_OK, response_model=list[TherapistUserRead])
async def get_therapists(
    user: APIGuard,
    controller: Annotated[UserController, Depends()],
) -> list[TherapistUserRead]:
    response = await controller.get_therapists()
    return response
