from sqlmodel import Field
from sqlmodel import Relationship

from api.base.model import Base
from api.profiles.common import TherapistExpertiseMap
from api.profiles.const import Gender
from api.profiles.const import MarriageStatus
from api.profiles.const import TherapistExpertiseEnum


class TherapistExpertise(Base, table=True):
    __tablename__ = "expertise"
    code: int = Field(primary_key=True)
    name: TherapistExpertiseEnum

    therapists: list['Therapist'] = Relationship(back_populates="expertises", link_model=TherapistExpertiseMap)


class MilitaryProfile(Base, table=True):
    user_id: str = Field(foreign_key="military.id", primary_key=True)
    gender: Gender | None = Field(default=None)
    about: str
    marriage_status: MarriageStatus = Field(default=MarriageStatus.SINGLE)
    kids: int = Field(default=0)
    hobbies: str
    complains: str
    insecures: str
    anxieties: str
