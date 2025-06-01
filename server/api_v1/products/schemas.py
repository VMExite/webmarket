from pydantic import BaseModel, ConfigDict, EmailStr
from pydantic_core.core_schema import DatetimeSchema


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


class BaseType(BaseModel):
    name: str
class CreateType(BaseType):
    pass
class UpdateType(BaseType):
    pass
class ReadType(BaseType):
    model_config = ConfigDict(from_attributes=True)

    id: int

class BaseMaterial(BaseModel):
    name: str
class CreateMaterial(BaseType):
    pass
class UpdateMaterial(BaseType):
    pass
class ReadMaterial(BaseType):
    model_config = ConfigDict(from_attributes=True)

    id: int

class BaseColor(BaseModel):
    name: str
class CreateColor(BaseType):
    pass
class UpdateColor(BaseType):
    pass
class ReadColor(BaseType):
    model_config = ConfigDict(from_attributes=True)

    id: int

class BaseProduct(BaseModel):
    name: str
    description: str
    price: int
    assay: int
    karat: float
    data: DatetimeSchema
    popularity: int
    image: str

class CreateProduct(BaseProduct):
    type: int
    material: int
    color: int

class UpdateProduct(BaseProduct):
    type: int
    material: int
    color: int

class ReadProduct(BaseProduct):
    model_config = ConfigDict(from_attributes=True)

    id: int
    type: ReadType
    material: ReadMaterial
    color: ReadColor

class BaseOrder(BaseModel):
    order_time: DatetimeSchema

class CreateOrder(BaseOrder):
    user_id: int
    product_id: int

class UpdateOrder(BaseOrder):
    user_id: int
    product_id: int

class ReadOrder(BaseOrder):
    model_config = ConfigDict(from_attributes=True)

    user: ReadUser
    product: ReadProduct


