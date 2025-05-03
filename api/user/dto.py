from pydantic import BaseModel
from pydantic import TypeAdapter

from api.base.model import FromORMDto
from api.user.models import UserRole


class MilitaryUserCreate(BaseModel):
    first_name: str
    last_name: str
    phone: str | None = None

    age: int
    location: str
    rank: str | None = None


class UserReadBase(FromORMDto):
    created_at: str
    updated_at: str | None

    id: str
    first_name: str
    last_name: str
    email: str
    phone: str | None
    age: int
    location: str
    role: UserRole


class MilitaryUserRead(UserReadBase):
    rank: str | None


class TherapistUserRead(UserReadBase):
    education: str
    experience: int
    verified: bool
    location: str

    expertises: list[str]


UserReadType = MilitaryUserRead | TherapistUserRead
UserRead = TypeAdapter(UserReadType)


class UserUpdateBase(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    age: int | None = None
    location: str | None = None

    def extract(self):
        return self.model_dump(exclude_unset=True)


class MilitaryUserUpdate(UserUpdateBase):
    rank: str | None = None


class TherapistUserUpdate(UserUpdateBase):
    education: str
    experience: int

    expertises: list[str] | None


UserUpdate = MilitaryUserUpdate | TherapistUserUpdate
