from pydantic import BaseModel

from api.profiles.models import Gender
from api.profiles.models import MarriageStatus


class MilitaryProfileCreate(BaseModel):
    gender: Gender | None = None
    age: int
    position: str
    about: str
    marriage_status: MarriageStatus | None = None
    kids: int = 0
    hobbies: str = ''
    complains: str
    insecures: str
    anxieties: str


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
