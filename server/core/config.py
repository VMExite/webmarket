from os import getenv
from pydantic_settings import BaseSettings
from pathlib import Path

MAIN_PATH = Path(__file__).parent.parent.parent

class Settings(BaseSettings):
    api_v1_prefix: str = "/api/v1"

    db_url: str = f"sqlite+aiosqlite:///{MAIN_PATH}/database.sqlite3"
    echo: bool = False

settings = Settings()