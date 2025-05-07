from pydantic import BaseModel
from pydantic import field_validator
from pydantic import TypeAdapter

from api.base.model import FromORMDto
from api.profiles.models import TherapistExpertise
from api.user.models import UserRole


class MilitaryUserCreate(BaseModel):
    first_name: str
    last_name: str
    phone: str | None = None

    age: int | None = None
    location: str | None = None
    rank: str | None = None


class UserReadBase(FromORMDto):
    created_at: str
    updated_at: str | None

    id: str
    first_name: str
    last_name: str
    name: str
    email: str
    phone: str | None
    age: int | None
    location: str | None
    role: UserRole


class MilitaryUserRead(UserReadBase):
    rank: str | None


class TherapistUserRead(UserReadBase):
    education: str
    experience: int
    verified: bool
    location: str
    bio: str

    expertises: list[int]

    @field_validator("expertises", mode="before")
    def validate_expertises(cls, expertises: list[TherapistExpertise]):
        return [e.code for e in expertises]


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
    education: str | None = None
    experience: int | None = None

    expertises: list[int] | None = None


UserUpdate = MilitaryUserUpdate | TherapistUserUpdate


class TherapistCreate(BaseModel):
    user_id: str
    first_name: str
    last_name: str
    email: str
    phone: str | None = None

    age: int
    location: str
    bio: str

    education: str
    experience: int
    verified: bool = True

    expertises: list[int] = []

    def extract(self):
        return self.model_dump(exclude_unset=True)
