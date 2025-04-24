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
    pass
