from enum import StrEnum
from functools import cached_property

from pydantic import computed_field
from sqlmodel import Field

from api.base.model import Base


class UserRole(StrEnum):
    MILITARY = "Military"
    THERAPIST = "Therapist"
    ADMIN = "Admin"


class User(Base):
    id: str = Field(primary_key=True)
    first_name: str
    last_name: str
    email: str | None = Field(default=None)
    phone: str | None = Field(default=None)

    role: UserRole

    @computed_field
    @cached_property
    def name(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Therapist(User, table=True):
    age: int
    experience: int
    verified: bool = Field(default=False)
    expertise: str
    location: str
    role: UserRole = UserRole.THERAPIST


class Military(User, table=True):
    age: int
    location: str
    position: str

    role: UserRole = UserRole.MILITARY


class Admin(User, table=True):
    pass
