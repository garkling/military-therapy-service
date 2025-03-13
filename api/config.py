from functools import lru_cache

from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


API_PREFIX = "/api/v1"


class Config(BaseSettings):
    model_config = SettingsConfigDict(extra="ignore")

    ENV: str
    CLIENT_ORIGIN: str = 'http://localhost:3000'


@lru_cache
def get_config():
    return Config()


conf = get_config()
