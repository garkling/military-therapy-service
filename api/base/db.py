from sqlalchemy.orm import sessionmaker
from sqlmodel import create_engine
from sqlmodel import Session
from sqlmodel import SQLModel

from api.config import conf


engine = create_engine(conf.postgresql_url)
LocalSession = sessionmaker(
    class_=Session,
    bind=engine,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
)


def get_db_session():
    with LocalSession() as session:
        yield session


def init_db():
    from api.user.models import Military, Therapist, Admin      # type: ignore
    SQLModel.metadata.create_all(engine)
