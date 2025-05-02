
import re
from wsgiref.validate import validator
from datetime import date
from pydantic import EmailStr, Field
from pydantic.v1 import BaseModel




# Roles
class RoleBase(BaseModel):
    name: str

class RoleCreate(RoleBase):
    pass

class RoleRead(RoleBase):
    id: int

    class Config:
        orm_mode = True

# Users
class UserBase(BaseModel):
    login: str
    email: EmailStr
    balance: int = Field(ge=0)

    @validator('login')
    def login(self, value):
        if ' ' in value or not re.match(r'^[a-zA-Z]+$', value):
            raise ValueError('Login contains invalid characters')
        return value


class UserCreate(UserBase):
    role: int

class UserRead(UserBase):
    id: int
    role: RoleRead

    class Config:
        orm_mode = True

# Types
class TypeBase(BaseModel):
    name: str

class TypeCreate(TypeBase):
    pass

class TypeRead(TypeBase):
    id: int

    class Config:
        orm_mode = True

# Products
class ProductBase(BaseModel):
    name: str
    description: str
    price: int
    quantity: int
    rating: int
    rating_quantity: int
    views: int
    pic: str

class ProductCreate(ProductBase):
    pass

class ProductRead(ProductBase):
    id: int

    class Config:
        orm_mode = True

# Comments
class CommentBase(BaseModel):
    grade: bool
    text: str
    likes: int
    date: str

    @validator('date')
    def date(self, value):
        if not re.fullmatch(r'^\d{2}\.\d{2}\.\d{4}$', value):
            raise ValueError('Data must have a format: DD.MM.YYYY')

        try:
            date.strftime(value, '%d.%m.%Y')
        except ValueError:
            raise ValueError('Invalid data value')

class CommentCreate(BaseModel):
    user: int
    product: int

class CommentRead(BaseModel):
    id: int
    user: UserRead
    product: ProductRead

    class Config:
        orm_mode = True