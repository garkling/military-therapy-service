from pydantic import BaseModel

from api.chats.models import ChatMessage
from api.chats.models import ChatRoom
from api.user.dto import UserRead
from api.user.dto import UserReadType
from api.user.models import User
from api.user.models import UserRole


class ChatCreate(BaseModel):
    participant_id: str


class MessagePreviewRead(BaseModel):
    id: str
    chat_id: str
    author_id: str
    author_name: str
    author_role: UserRole | None
    content: str

    sent_at: str

    @classmethod
    def from_model(cls, msg: ChatMessage, user: User | None):
        return cls(
            **msg.model_dump(mode='json'),
            author_name=user.name if user else "Deleted",
            author_role=user.role if user else None
        )


class ChatRead(BaseModel):
    id: str

    created_at: str
    updated_at: str | None

    participant: UserReadType | None

    last_updated_at: str
    last_message_id: str | None

    @classmethod
    def from_model(cls, chat: ChatRoom, participant: UserReadType | None = None):
        return cls(
            **chat.model_dump(mode='json'),
            participant=UserRead.validate_python(participant) if participant else None,
        )


class ChatPreviewRead(BaseModel):
    id: str

    created_at: str
    updated_at: str | None

    participant: UserReadType | None

    last_updated_at: str
    last_message: MessagePreviewRead | None

    @classmethod
    def from_model(cls, chat: ChatRoom, participant: UserReadType | None = None, last_message: MessagePreviewRead | None = None):
        return cls(
            **chat.model_dump(mode='json'),
            participant=UserRead.validate_python(participant) if participant else None,
            last_message=last_message
        )
