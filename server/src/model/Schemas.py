
import re
from pydantic import EmailStr, Field, field_validator
from pydantic import BaseModel
from pydantic_core.core_schema import DatetimeSchema


# Roles
class RoleBase(BaseModel):
    name: str

class RoleCreate(RoleBase):
    pass

class RoleRead(RoleBase):
    id: int

    class Config:
        # orm_mode = True
        from_attributes = True


# Users
class UserBase(BaseModel):
    login: str
    email: EmailStr
    balance: int = Field(ge=0)

    @field_validator('login')
    @classmethod
    def login(cls, value):
        if ' ' in value or not re.fullmatch(r'^[a-zA-Z]+$', value):
            raise ValueError('Login contains invalid characters')
        return value

class UserCreate(UserBase):
    role: int

class UserRead(UserBase):
    id: int
    role: RoleRead

    class Config:
        # orm_mode = True
        from_attributes = True




# Types
class TypeBase(BaseModel):
    name: str

class TypeCreate(TypeBase):
    pass

class TypeRead(TypeBase):
    id: int

    class Config:
        # orm_mode = True
        from_attributes = True


# Products
class ProductBase(BaseModel):
    name: str
    description: str
    price: int
    fineness: int
    carat: int
    type: str
    material: str
    color: str
    size: int
    popularity: int
    date: DatetimeSchema
    image: str

class ProductCreate(ProductBase):
    pass

class ProductRead(ProductBase):
    id: int

    class Config:
        # orm_mode = True
        from_attributes = True


