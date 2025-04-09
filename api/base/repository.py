from typing import Annotated
from typing import Generic
from typing import get_args
from typing import Optional
from typing import TypeVar

from fastapi import Depends
from sqlmodel import Session
from sqlmodel import SQLModel

from api.base.db import get_db_session
from api.logger import get_logger

logger = get_logger(__name__)
ModelType = TypeVar("ModelType", bound=SQLModel)


class BaseRepository(Generic[ModelType]):
    _model: ModelType | None = None

    def __init__(self, session: Annotated[Session, Depends(get_db_session)]):
        self.session = session

    def create(self, instance: ModelType) -> ModelType:
        self.session.add(instance)
        self.session.commit()
        self.session.refresh(instance)
        return instance

    def get(self, pk: str) -> Optional[ModelType]:
        return self.session.get(self._model, pk)

    def update(self, instance: ModelType) -> ModelType:
        self.session.add(instance)
        self.session.commit()
        self.session.refresh(instance)
        return instance

    def delete(self, instance: ModelType) -> None:
        self.session.delete(instance)
        self.session.commit()

    def __init_subclass__(cls, **kwargs):
        base = [
            b
            for b in cls.__orig_bases__  # type: ignore
            if getattr(b, "__origin__", None) == BaseRepository
        ]
        if not base:
            raise Exception("Generic type must be directly provided "
                            "to the class while inherited from BaseRepository")

        cls._model = get_args(base[0])[0]
