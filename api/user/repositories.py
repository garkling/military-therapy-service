from sqlalchemy import select

from api.base.repository import BaseRepository
from api.profiles.common import TherapistExpertiseMap
from api.user.models import Military
from api.user.models import Therapist


class MilitaryRepository(BaseRepository[Military]):
    pass


class TherapistRepository(BaseRepository[Therapist]):

    def get_therapists_by_expertise(self, expertise_codes: list[int]) -> list[Therapist]:
        stmt = (
            select(Therapist)
            .join(TherapistExpertiseMap)
            .where(TherapistExpertiseMap.expertise_code.in_(expertise_codes))   # type: ignore
            .distinct()
        )

        items = self.session.exec(stmt).all()
        return [Therapist.model_validate(item) for item in items]
