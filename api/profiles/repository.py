from sqlmodel import select

from api.base.repository import BaseRepository
from api.profiles.models import MilitaryProfile
from api.profiles.models import TherapistExpertise


class MilitaryProfileRepository(
    BaseRepository[MilitaryProfile],
):
    pass


class TherapistExpertiseRepository(
    BaseRepository[TherapistExpertise],
):

    def get_by_codes(self, codes: list[int]) -> list[TherapistExpertise]:
        stmt = (
            select(TherapistExpertise)
            .where(TherapistExpertise.code.in_(codes))
        )

        return self.session.exec(stmt).all()
