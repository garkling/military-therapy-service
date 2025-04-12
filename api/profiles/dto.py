from pydantic import BaseModel

from api.profiles.models import Gender, MarriageStatus


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
