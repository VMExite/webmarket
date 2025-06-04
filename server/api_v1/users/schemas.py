from pydantic import BaseModel, ConfigDict, EmailStr


class BaseUser(BaseModel):
    login: str
    email: EmailStr
    password: str

class CreateUser(BaseUser):
    pass

class UpdateUser(BaseUser):
    pass

class ReadUser(BaseUser):
    model_config = ConfigDict(from_attributes=True)

    id: int