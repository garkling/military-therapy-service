from typing import Annotated

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from starlette import status

from api.auth.guards import APIGuard
from api.chats.dto import ChatCreate
from api.chats.dto import ChatPreviewRead
from api.chats.dto import ChatWithMessagesRead
from api.chats.models import ChatRoom
from api.chats.service import ChatMessageService
from api.chats.service import ChatRoomService
from api.user.models import User
from api.user.models import UserRole
from api.user.services import UserService

router = APIRouter(prefix="/chats")


class ChatController:

    def __init__(
        self,
        user_service: Annotated[UserService, Depends()],
        chat_service: Annotated[ChatRoomService, Depends()],
        chat_messages_service: Annotated[ChatMessageService, Depends()],
    ):
        self._chat_service = chat_service
        self._chat_messages_service = chat_messages_service
        self._user_service = user_service

    async def create_chat(self, participant_id: str, user: User) -> ChatWithMessagesRead:
        if user.role == UserRole.MILITARY:
            military_id = user.id
            therapist_id = participant_id
        else:
            military_id = participant_id
            therapist_id = user.id

        chat_data = self._chat_service.create_new_chat(
            therapist_id=therapist_id,
            military_id=military_id,
        )
        participant = self._user_service.get(participant_id)

        return ChatWithMessagesRead.from_model(**chat_data, participant=participant)

    async def get_chat(self, chat_id: str, user: User) -> ChatWithMessagesRead:
        chat_data = self._chat_service.get_chat_room_with_latest_messages(chat_id)
        chat: ChatRoom = chat_data['chat']
        if user.id == chat.military_id:
            participant_id = chat.therapist_id
        elif user.id == chat.therapist_id:
            participant_id = chat.military_id
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")

        participant = self._user_service.get(participant_id)
        return ChatWithMessagesRead.from_model(**chat_data, participant=participant)

    async def list_chats(self, user: User) -> list[ChatPreviewRead]:
        chats = self._chat_service.list_chat_rooms_for(user)

        chat_previews = []
        for chat, participant, last_message in chats:
            chat_previews.append(ChatPreviewRead.from_model(chat, participant, last_message))

        return chat_previews


@router.post("", status_code=status.HTTP_201_CREATED, response_model=ChatWithMessagesRead)
async def create_chat(
    body: ChatCreate,
    user: APIGuard,
    controller: Annotated[ChatController, Depends()]
) -> ChatWithMessagesRead:
    response = await controller.create_chat(body.participant_id, user)
    return response


@router.get("/{chat_id}", status_code=status.HTTP_200_OK, response_model=ChatWithMessagesRead)
async def get_chat(
    chat_id: str,
    user: APIGuard,
    controller: Annotated[ChatController, Depends()]
) -> ChatWithMessagesRead:
    response = await controller.get_chat(chat_id, user)
    return response


@router.get("", status_code=status.HTTP_200_OK, response_model=list[ChatPreviewRead])
async def list_chats(
    user: APIGuard,
    controller: Annotated[ChatController, Depends()],
) -> list[ChatPreviewRead]:
    response = await controller.list_chats(user)
    return response
