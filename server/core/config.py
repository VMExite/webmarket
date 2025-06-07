import os
from os import getenv
from pathlib import Path

from pydantic.v1 import BaseSettings

MAIN_PATH = Path(__file__).parent.parent.parent
SECRET = str(os.getenv("SECRET_KEY"))
JWT_EXPIRE_TIME = os.getenv("JWT_EXPIRE_TIME")

class Settings(BaseSettings):
    api_v1_prefix: str = "/api/v1"

    db_url: str = f"sqlite+aiosqlite:///{MAIN_PATH}/database.sqlite3"
    echo: bool = False

settings = Settings()