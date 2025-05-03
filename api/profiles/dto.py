from pydantic import BaseModel

from api.base.model import FromORMDto
from api.profiles.models import Gender
from api.profiles.models import MarriageStatus


class MilitaryProfileCreate(BaseModel):
    gender: Gender | None = None
    about: str
    marriage_status: MarriageStatus | None = None
    kids: int = 0
    hobbies: str = ''
    complains: str
    insecures: str
    anxieties: str


class MilitaryProfileRead(FromORMDto):
    created_at: str
    updated_at: str | None

    user_id: str
    gender: Gender | None
    about: str
    marriage_status: MarriageStatus | None
    kids: int = 0
    hobbies: str = ''
    complains: str
    insecures: str
    anxieties: str


class MilitaryProfileUpdate(BaseModel):
    gender: Gender | None = None
    about: str | None = None
    marriage_status: MarriageStatus | None = None
    kids: int | None = None
    hobbies: str | None = None
    complains: str | None = None
    insecures: str | None = None
    anxieties: str | None = None

    def extract(self):
        return self.model_dump(exclude_unset=True)


class TherapistProfileView(BaseModel):
    id: str
    first_name: str
    last_name: str
    email: str | None
    phone: str | None

    age: int
    education: str
    experience: str
    location: str

    expertises: list[str]
