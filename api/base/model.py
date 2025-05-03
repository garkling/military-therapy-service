from pydantic import BaseModel
from pydantic import ConfigDict
from sqlalchemy import inspect
from sqlmodel import Field
from sqlmodel import SQLModel

from api.utils.utils import get_current_date_iso_string


class Base(SQLModel):
    created_at: str = Field(default_factory=get_current_date_iso_string)
    updated_at: str | None = Field(default=None)

    def update_attributes(self, **attributes):
        for attr, value in attributes.items():
            if value is not None:
                setattr(self, attr, value)

    def get_primary_key(self):
        key = inspect(self.__class__).primary_key[0].name
        return getattr(self, key)


class FromORMDto(BaseModel):
    model_config = ConfigDict(from_attributes=True)
