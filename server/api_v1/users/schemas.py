from pydantic import BaseModel, ConfigDict, EmailStr
from fastapi_users import schemas

class BaseUser(schemas.BaseUser[int]):
    login: str

class CreateUser(schemas.BaseUserCreate):
    login: str

class UpdateUser(schemas.BaseUserUpdate):
    login: str

class ReadUser(BaseUser):
    model_config = ConfigDict(from_attributes=True)

    id: int