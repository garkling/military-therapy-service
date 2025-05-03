from sqlmodel import select

from api.base.repository import BaseRepository
from api.chats.models import ChatMessage
from api.chats.models import ChatRoom
from api.user.models import Military
from api.user.models import Therapist


class ChatRepository(BaseRepository[ChatRoom]):

    def check_if_chat_exists(self, therapist_id: str, military_id: str) -> str | None:
        stmt = (
            select(ChatRoom.id)
            .where(
                ChatRoom.military_id == military_id,
                ChatRoom.therapist_id == therapist_id
            )
            .limit(1)
        )
        chat_id = self.session.exec(stmt).first()
        return chat_id

    def list_chats_by(self, user_model: type[Military | Therapist], by_id: str) -> list[dict]:
        if isinstance(user_model, Military):
            other_part = Therapist
            field = ChatRoom.therapist_id
        else:
            other_part = Military
            field = ChatRoom.military_id

        stmt = (
            select(ChatRoom, other_part, ChatMessage)
            .join(other_part, other_part.id == field, isouter=True)
            .join(ChatMessage, ChatMessage.id == ChatRoom.last_message_id, isouter=True)
            .where(user_model.id == by_id)
            .order_by(ChatRoom.last_updated_at.desc())  # type: ignore
        )

        items = self.session.exec(stmt).all()
        return list(items)


class ChatMessageRepository(BaseRepository[ChatMessage]):

    def get_n_messages_in_chat(self, chat_id: str, n: int) -> list[ChatMessage]:
        stmt = (
            select(ChatMessage)
            .where(ChatMessage.chat_id == chat_id)  # type: ignore
            .limit(n)
            .order_by(ChatMessage.sent_at.desc())   # type: ignore
        )

        items = self.session.exec(stmt).all()
        return [ChatMessage.model_validate(item) for item in items]

    def list_messages_in_chat(self, chat_id: str) -> list[ChatMessage]:
        stmt = (
            select(ChatMessage)
            .where(ChatMessage.chat_id == chat_id)
            .order_by(ChatMessage.sent_at.desc())   # type: ignore
        )

        items = self.session.exec(stmt).all()
        return [ChatMessage.model_validate(item) for item in items]
