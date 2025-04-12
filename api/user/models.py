from enum import StrEnum
from functools import cached_property

from pydantic import computed_field
from sqlmodel import Field, Relationship

from api.base.model import Base
from api.profiles.models import TherapistExpertiseMap


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
    education: str
    experience: int
    verified: bool = Field(default=False)
    location: str

    expertises: list['TherapistExpertise'] = Relationship(back_populates="therapists", link_model=TherapistExpertiseMap)

    role: UserRole = UserRole.THERAPIST


class Military(User, table=True):
    age: int
    location: str

    role: UserRole = UserRole.MILITARY
