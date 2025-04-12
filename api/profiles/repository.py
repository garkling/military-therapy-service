from api.base.repository import BaseRepository
from api.profiles.models import MilitaryProfile


class MilitaryProfileRepository(
    BaseRepository[MilitaryProfile],
):
    pass
