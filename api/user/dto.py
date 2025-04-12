from pydantic import BaseModel

from api.base.model import FromORMDto


class MilitaryUserCreate(BaseModel):
    first_name: str
    last_name: str
    phone: str | None = None

    age: int
    location: str
    position: str


class MilitaryUserRead(FromORMDto):
    id: str
    first_name: str
    last_name: str
    email: str
    phone: str
    age: int
    location: str
    position: str
