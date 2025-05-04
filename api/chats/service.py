from typing import Annotated

from fastapi import Depends

from api.chats.models import ChatMessage
from api.chats.models import ChatRoom
from api.chats.repository import ChatMessageRepository
from api.chats.repository import ChatRepository
from api.user.models import Military
from api.user.models import Therapist
from api.user.models import User
from api.utils.utils import get_current_date_iso_string


class ChatRoomService:

    def __init__(
        self,
        chat_repository: Annotated[ChatRepository, Depends()],
        chat_message_repository: Annotated[ChatMessageRepository, Depends()],
    ):
        self._chat_repository = chat_repository
        self._chat_message_repository = chat_message_repository

    def create_new_chat(
        self,
        therapist_id: str,
        military_id: str,
    ) -> ChatRoom:
        if chat_id := self._chat_repository.check_if_chat_exists(therapist_id, military_id):
            return self.get_chat_or_raise(chat_id)

        chat = ChatRoom(therapist_id=therapist_id, military_id=military_id)
        self._chat_repository.create(chat)
        return chat

    def refresh_chat(self, chat: ChatRoom, message_id: str) -> ChatRoom:
        chat.last_updated_at = get_current_date_iso_string()
        chat.last_message_id = message_id
        self._chat_repository.update(chat)
        return chat

    def get_chat_or_raise(self, chat_id: str) -> ChatRoom:
        return self._chat_repository.get_or_raise(chat_id)

    def get_chat_room_with_latest_messages(
        self,
        chat_id: str,
        n_latest_messages: int = 20
    ) -> dict:
        chat = self._chat_repository.get_or_raise(chat_id)
        messages = self._chat_message_repository.get_n_messages_in_chat(chat.id, n_latest_messages)

        return dict(chat=chat, messages=messages)

    def list_chat_rooms_for(self, user: User) -> list[dict]:
        if user.role == Military:
            return self._chat_repository.list_chats_by(Military, user.id)
        else:
            return self._chat_repository.list_chats_by(Therapist, user.id)


class ChatMessageService:
    def __init__(
        self,
        repo: Annotated[ChatMessageRepository, Depends()],
    ):
        self._repo = repo

    def create_message(self, chat_id: str, author_id: str, content: str) -> ChatMessage:
        msg = ChatMessage(chat_id=chat_id, author_id=author_id, content=content)
        self._repo.create(msg)
        return msg

    def list_messages_in_chat(self, chat_id: str) -> list[ChatMessage]:
        msgs = self._repo.list_messages_in_chat(chat_id)
        return msgs

    def delete_message(self, message_id: str):
        msg = self._repo.get_or_raise(message_id)
        self._repo.delete(msg)
