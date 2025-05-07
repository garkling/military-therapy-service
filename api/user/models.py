from enum import StrEnum
from functools import cached_property

from pydantic import computed_field
from sqlmodel import Field
from sqlmodel import Relationship

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
    email: str | None = Field(default=None, unique=True)
    phone: str | None = Field(default=None, unique=True)

    role: UserRole = Field(nullable=False)

    @computed_field
    @cached_property
    def name(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Therapist(User, table=True):
    __tablename__ = "therapists"

    age: int
    education: str
    experience: int
    verified: bool = Field(default=False)
    location: str
    bio: str

    expertises: list['TherapistExpertise'] = Relationship(
        back_populates="therapists",
        link_model=TherapistExpertiseMap,
        sa_relationship_kwargs={"lazy": "selectin"}
    )

    role: UserRole = UserRole.THERAPIST


class Military(User, table=True):
    __tablename__ = "military"

    age: int | None = None
    location: str | None = None
    rank: str | None = None

    role: UserRole = UserRole.MILITARY
