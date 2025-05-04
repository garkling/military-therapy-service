from typing import Annotated

from fastapi import APIRouter
from fastapi import Body
from fastapi import Depends
from fastapi import HTTPException
from starlette import status

from api.auth.guards import APIGuard
from api.chats.dto import ChatCreate
from api.chats.dto import ChatPreviewRead
from api.chats.dto import ChatRead
from api.chats.dto import MessagePreviewRead
from api.chats.service import ChatMessageService
from api.chats.service import ChatRoomService
from api.pusher.client import PusherClient
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
        pusher_client: Annotated[PusherClient, Depends()],
    ):
        self._chat_service = chat_service
        self._chat_messages_service = chat_messages_service
        self._user_service = user_service

        self._pusher_client = pusher_client

    async def create_chat(self, participant_id: str, user: User) -> ChatRead:
        if user.role == UserRole.MILITARY:
            military_id = user.id
            therapist_id = participant_id
        else:
            military_id = participant_id
            therapist_id = user.id

        chat = self._chat_service.create_new_chat(
            therapist_id=therapist_id,
            military_id=military_id,
        )
        participant = self._user_service.get(participant_id)

        return ChatRead.from_model(chat, participant=participant)

    async def get_chat(self, chat_id: str, user: User) -> ChatRead:
        chat = self._chat_service.get_chat_or_raise(chat_id)
        if user.id == chat.military_id:
            participant_id = chat.therapist_id
        elif user.id == chat.therapist_id:
            participant_id = chat.military_id
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")

        participant = self._user_service.get(participant_id)
        return ChatRead.from_model(chat, participant=participant)

    async def list_chats(self, user: User) -> list[ChatPreviewRead]:
        chats = self._chat_service.list_chat_rooms_for(user)

        chat_previews = []
        for chat, participant, last_message, in chats:
            last_message_preview = None
            if last_message:
                last_message_author = self._user_service.get(last_message.author_id)
                last_message_preview = MessagePreviewRead.from_model(last_message, last_message_author)

            chat_previews.append(ChatPreviewRead.from_model(chat, participant, last_message_preview))

        return chat_previews

    async def create_message(self, chat_id: str, content: str, user: User) -> MessagePreviewRead:
        chat = self._chat_service.get_chat_or_raise(chat_id)
        message = self._chat_messages_service.create_message(
            chat_id=chat_id,
            author_id=user.id,
            content=content,
        )
        self._chat_service.refresh_chat(chat, message.id)

        message_preview = MessagePreviewRead.from_model(message, user)
        self._pusher_client.send(chat.id, message_preview.model_dump(mode='json'))
        return message_preview

    async def list_messages(self, chat_id: str, user: User) -> list[MessagePreviewRead]:
        messages = self._chat_messages_service.list_messages_in_chat(chat_id)

        author_ids = [m.author_id for m in messages]
        authors = self._user_service.list_by_ids(author_ids)
        author_map = {author.id: author for author in authors}

        message_previews = []
        for message in messages:
            author = author_map.get(message.author_id)
            preview = MessagePreviewRead.from_model(message, author)
            message_previews.append(preview)

        return message_previews

    async def delete_message(self, chat_id: str, message_id: str, user: User):
        self._chat_messages_service.delete_message(message_id)


@router.post("", status_code=status.HTTP_201_CREATED, response_model=ChatRead)
async def create_chat(
    body: ChatCreate,
    user: APIGuard,
    controller: Annotated[ChatController, Depends()]
) -> ChatRead:
    response = await controller.create_chat(body.participant_id, user)
    return response


@router.get("/{chat_id}", status_code=status.HTTP_200_OK, response_model=ChatRead)
async def get_chat(
    chat_id: str,
    user: APIGuard,
    controller: Annotated[ChatController, Depends()]
) -> ChatRead:
    response = await controller.get_chat(chat_id, user)
    return response


@router.get("", status_code=status.HTTP_200_OK, response_model=list[ChatPreviewRead])
async def list_chats(
    user: APIGuard,
    controller: Annotated[ChatController, Depends()],
) -> list[ChatPreviewRead]:
    response = await controller.list_chats(user)
    return response


@router.post("/{chat_id}/messages", status_code=status.HTTP_201_CREATED, response_model=MessagePreviewRead)
async def create_message(
    chat_id: str,
    user: APIGuard,
    message: Annotated[str, Body(embed=True)],
    controller: Annotated[ChatController, Depends()]
) -> MessagePreviewRead:
    response = await controller.create_message(chat_id, message, user)
    return response


@router.get("/{chat_id}/messages", status_code=status.HTTP_200_OK, response_model=list[MessagePreviewRead])
async def list_messages(
    chat_id: str,
    user: APIGuard,
    controller: Annotated[ChatController, Depends()]
) -> list[MessagePreviewRead]:
    response = await controller.list_messages(chat_id, user)
    return response


@router.delete("/{chat_id}/messages/{message_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_message(
    chat_id: str,
    message_id: str,
    user: APIGuard,
    controller: Annotated[ChatController, Depends()]
):
    response = await controller.delete_message(chat_id, message_id, user)
    return response
