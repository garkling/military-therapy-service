from typing import Annotated
from typing import Generic
from typing import get_args
from typing import Optional
from typing import TypeVar

from fastapi import Depends
from sqlmodel import select
from sqlmodel import Session
from sqlmodel import SQLModel

from api.base.db import get_db_session
from api.base.errors import handle_db_errors
from api.base.errors import ItemDoesNotExistError
from api.logger import get_logger

logger = get_logger(__name__)
ModelType = TypeVar("ModelType", bound=SQLModel)


class BaseRepository(Generic[ModelType]):
    _model: ModelType

    def __init__(self, session: Annotated[Session, Depends(get_db_session)]):
        self.session = session

    @handle_db_errors
    def create(self, instance: ModelType) -> ModelType:
        self.session.add(instance)
        self.session.commit()
        self.session.refresh(instance)
        return instance

    def get(self, pk: str | tuple[str, str]) -> Optional[ModelType]:
        return self.session.get(self._model, pk)

    def get_or_raise(self, pk: str) -> ModelType:
        item = self.get(pk)
        if item is None:
            raise ItemDoesNotExistError(self._model.__name__, pk)

        return item

    def update(self, instance: ModelType) -> ModelType:
        self.session.add(instance)
        self.session.commit()
        self.session.refresh(instance)
        return instance

    def delete(self, instance: ModelType) -> None:
        self.session.delete(instance)
        self.session.commit()

    def list(self) -> list[ModelType]:
        items = self.session.exec(select(self._model)).all()
        return [self._model.model_validate(item) for item in items]

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
