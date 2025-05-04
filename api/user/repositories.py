from sqlalchemy import select

from api.base.repository import BaseRepository
from api.profiles.models import TherapistExpertise
from api.user.models import Military
from api.user.models import Therapist


class MilitaryRepository(BaseRepository[Military]):

    def batch_get(self, ids: list[str]):
        stmt = (
            select(Military)
            .where(Military.id.in_(ids))
        )
        items = self.session.exec(stmt).scalars().all()
        return items


class TherapistRepository(BaseRepository[Therapist]):

    def get_therapists_by_expertise(self, expertise_codes: list[int]) -> list[Therapist]:
        stmt = (
            select(Therapist)
            .join(Therapist.expertises)
            .where(TherapistExpertise.code.in_(expertise_codes))
            .distinct()
        )
        items = self.session.exec(stmt).scalars().all()
        return items

    def batch_get(self, ids: list[str]):
        stmt = (
            select(Therapist)
            .where(Therapist.id.in_(ids))
        )
        items = self.session.exec(stmt).scalars().all()
        return items
