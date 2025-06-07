from pydantic import BaseModel, ConfigDict, EmailStr
from fastapi_users import schemas

class BaseUser(schemas.BaseUser[int]):
    login: str
    email: EmailStr
    password: str

class CreateUser(schemas.BaseUserCreate):
    pass

class UpdateUser(schemas.BaseUserUpdate):
    pass

class ReadUser(BaseUser):
    model_config = ConfigDict(from_attributes=True)

    id: int