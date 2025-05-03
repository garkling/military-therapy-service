from faker import Faker

from api.base.db import destroy_db
from api.base.db import init_db
from api.base.db import LocalSession
from api.base.repository import BaseRepository
from api.profiles.common import TherapistExpertiseMap
from api.profiles.const import EXPERTISE_CODES
from api.profiles.models import TherapistExpertise
from api.profiles.repository import TherapistExpertiseRepository
from api.user.models import Therapist
from api.user.repositories import TherapistRepository

fake = Faker()


def create_expertises():
    expertises = []
    for code, entity in EXPERTISE_CODES.items():
        with LocalSession() as session:

            i = TherapistExpertise(
                code=code,
                name=entity
            )
            TherapistExpertiseRepository(session).create(i)
            expertises.append(i)

    return expertises


def create_therapists():
    with LocalSession() as session:
        therapist_repo = TherapistRepository(session)

        TherapistExpertiseRepository(session).list()
        t1 = Therapist(
            id=fake.uuid4(),
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email(),
            phone=None,
            age=25,
            experience=4,
            education="12345",
            location=fake.city(),
            verified=True,
        )
        therapist_repo.create(t1)
        user = TherapistRepository(session).get(t1.id)
        print(user)
        m2m = TherapistExpertiseMap(expertise_code=1, therapist_id=t1.id)
        BaseRepository(session).create(m2m)
        return t1


def init():
    create_expertises()
    create_therapists()


if __name__ == '__main__':
    destroy_db()
    init_db()

    init()
