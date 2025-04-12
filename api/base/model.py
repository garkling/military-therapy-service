from pydantic import BaseModel
from pydantic import ConfigDict
from sqlmodel import Field
from sqlmodel import SQLModel

from api.utils.utils import get_current_date_iso_string


class Base(SQLModel):
    created_at: str = Field(default_factory=get_current_date_iso_string)
    updated_at: str | None = Field(default=None)


class FromORMDto(BaseModel):
    model_config = ConfigDict(from_attributes=True)
