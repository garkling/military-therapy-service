from pydantic import BaseModel

from api.chats.models import ChatMessage
from api.chats.models import ChatRoom
from api.user.dto import UserRead
from api.user.dto import UserReadType
from api.user.models import User


class ChatCreate(BaseModel):
    participant_id: str


class ChatMessageRead(BaseModel):
    created_at: str
    sent_at: str

    id: str
    chat_id: str
    author_id: str
    content: str


class ChatWithMessagesRead(BaseModel):
    created_at: str

    id: str
    participant: UserReadType | None

    last_updated_at: str
    last_messages: list[ChatMessageRead]

    @classmethod
    def from_model(cls, chat: ChatRoom, messages: list[ChatMessage] | None = None, participant: User | None = None):
        messages = messages or []
        return cls(
            **chat.model_dump(mode='json'),
            participant=UserRead.validate_python(participant),
            last_messages=[ChatMessageRead.model_validate(item) for item in messages]
        )


class ChatPreviewRead(BaseModel):
    created_at: str
    updated_at: str | None

    participant: UserReadType | None

    last_updated_at: str
    last_message: ChatMessageRead | None

    @classmethod
    def from_model(cls, chat: ChatRoom, participant: UserReadType | None = None, last_message: ChatMessage | None = None):
        return cls(
            **chat.model_dump(mode='json'),
            participant=UserRead.validate_python(participant) if participant else None,
            last_message=ChatMessageRead.model_validate(last_message) if last_message else None
        )
