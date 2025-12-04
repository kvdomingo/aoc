from functools import lru_cache
from pathlib import Path

from pydantic import SecretStr
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    BASE_DIR: Path = Path(__file__).parent.parent

    AOC_SESSION: SecretStr


@lru_cache
def _get_settings() -> Settings:
    return Settings()


settings = _get_settings()
