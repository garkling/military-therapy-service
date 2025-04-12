from sqlmodel import Field

from api.base.model import Base


class TherapistExpertiseMap(Base, table=True):
    __tablename__ = "therapist_expertise"
    expertise_code: int = Field(foreign_key='expertise.code', primary_key=True)
    therapist_id: str = Field(foreign_key='therapist.id', primary_key=True)
