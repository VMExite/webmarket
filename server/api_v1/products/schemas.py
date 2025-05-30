from pydantic import BaseModel, ConfigDict, EmailStr


class BaseUser(BaseModel):
    login: str
    email: EmailStr
    password: str

class CreateUser(BaseUser):
    pass

class UpdateUser(BaseUser):
    pass

class User(BaseUser):
    model_config = ConfigDict(from_attributes=True)

    id: int

class BaseProduct(BaseModel):
    name: str
    description: str
    price: int

class CreateProduct(BaseProduct):
    pass

class UpdateProduct(BaseProduct):
    pass

class Product(BaseProduct):
    model_config = ConfigDict(from_attributes=True)

    id: int