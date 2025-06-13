from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field

from server.api_v1.users.schemas import ReadUser


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
class CreateMaterial(BaseMaterial):
    pass
class UpdateMaterial(BaseMaterial):
    pass
class ReadMaterial(BaseMaterial):
    model_config = ConfigDict(from_attributes=True)

    id: int

class BaseProduct(BaseModel):
    name: str
    description: str
    price: int
    assay: int
    karat: float
    data: datetime
    popularity: int
    image: str

class CreateProduct(BaseProduct):
    type: int = Field(alias="type_id")
    material: int = Field(alias="material_id")

class UpdateProduct(BaseProduct):
    type: int = Field(alias="type_id")
    material: int = Field(alias="material_id")

class ReadProduct(BaseProduct):
    model_config = ConfigDict(from_attributes=True, populate_by_name=True)
    id: int

    type: int = Field(alias="type_id")
    material: int = Field(alias="material_id")


class BaseOrder(BaseModel):
    order_time: datetime

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


class FilterData(BaseModel):
    type: ReadType | None = None
    material: ReadMaterial | None = None
    max_cost: int
    min_cost: int = Field(ge=8500)