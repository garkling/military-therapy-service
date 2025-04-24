from sqlalchemy.orm import registry
from sqlalchemy.orm import sessionmaker
from sqlmodel import create_engine
from sqlmodel import Session
from sqlmodel import SQLModel

from api.config import conf

mapper_registry = registry()
engine = create_engine(conf.postgresql_url)
LocalSession = sessionmaker(
    class_=Session,
    bind=engine,
    autocommit=False,
    autoflush=True,
    expire_on_commit=False,
)


def get_db_session():
    with LocalSession() as session:
        yield session


def init_db():
    print("Tables:", SQLModel.metadata.tables.keys())
    from api.user.models import Military, Therapist
    from api.profiles.models import MilitaryProfile, TherapistExpertise
    from api.profiles.common import TherapistExpertiseMap
    from api.assessment.models import TestAssessmentResult

    SQLModel.metadata.create_all(engine)


def destroy_db():
    from api.user.models import Military, Therapist
    from api.profiles.models import MilitaryProfile, TherapistExpertise
    from api.profiles.common import TherapistExpertiseMap
    from api.assessment.models import TestAssessmentResult

    SQLModel.metadata.drop_all(engine)
