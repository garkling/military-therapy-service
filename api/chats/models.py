from sqlmodel import Field

from api.base.model import Base
from api.utils.utils import get_current_date_iso_string
from api.utils.utils import get_uuid_str


class ChatRoom(Base, table=True):
    __tablename__ = "chats"

    id: str = Field(default_factory=get_uuid_str, primary_key=True)
    therapist_id: str = Field(foreign_key="therapists.id")
    military_id: str = Field(foreign_key="military.id")
    last_updated_at: str = Field(default_factory=get_current_date_iso_string)
    last_message_id: str | None = Field(None)


class ChatMessage(Base, table=True):
    __tablename__ = "chatmessages"

    id: str = Field(default_factory=get_uuid_str, primary_key=True)
    chat_id: str = Field(foreign_key="chats.id", ondelete="CASCADE")
    author_id: str
    content: str
    sent_at: str = Field(default_factory=get_current_date_iso_string)
