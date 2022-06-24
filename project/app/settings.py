import os

from functools import lru_cache

from loguru import logger
from pydantic import AnyUrl, BaseSettings


class Settigns(BaseSettings):
    database_url: AnyUrl = os.environ.get("DATABASE_URL")

@lru_cache
def get_settings() -> BaseSettings:
    return Settings()
