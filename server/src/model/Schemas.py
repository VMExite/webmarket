
import re
from wsgiref.validate import validator
from datetime import datetime
from pydantic import EmailStr, Field, field_validator
from pydantic import BaseModel


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
        # orm_mode = True
        from_attributes = True


# Comments
class CommentBase(BaseModel):
    grade: bool
    text: str
    likes: int
    date: str

    @field_validator('date')
    @classmethod
    def date(cls, value):
        if not re.fullmatch(r'^\d{2}\.\d{2}\.\d{4}$', value):
            raise ValueError('Data must have a format: DD.MM.YYYY')

        try:
            datetime.strftime(value, '%d.%m.%Y')
        except ValueError:
            raise ValueError('Invalid data value')

        return value

class CommentCreate(CommentBase):
    user: int
    product: int

class CommentRead(CommentBase):
    id: int
    user: UserRead
    product: ProductRead

    class Config:
        # orm_mode = True
        from_attributes = True


