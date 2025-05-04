from functools import lru_cache

from pydantic import computed_field
from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


API_PREFIX = "/api/v1"


class Config(BaseSettings):
    model_config = SettingsConfigDict(extra="ignore")

    ENV: str
    CLIENT_ORIGIN: str = 'http://localhost:3000'

    # db
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str

    # auth0
    AUTH0_DOMAIN: str
    AUTH0_AUDIENCE: str

    # pusher
    PUSHER_APP_ID: str
    PUSHER_KEY: str
    PUSHER_SECRET: str
    PUSHER_CLUSTER: str = 'mt1'

    @computed_field
    @property
    def postgresql_url(self) -> str:
        return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:5432/{self.POSTGRES_DB}"


@lru_cache
def get_config():
    return Config()


conf = get_config()
