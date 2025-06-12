from typing import TYPE_CHECKING

from sqlalchemy import DATETIME, ForeignKey
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base_model import Base

if TYPE_CHECKING:
    from server.core.models.order import Order

class Product(Base):
    __tablename__ = "product"
    name: Mapped[str]
    description: Mapped[str]
    price: Mapped[int]
    type_id: Mapped[int] = mapped_column(ForeignKey("type.id"))
    material_id: Mapped[int] = mapped_column(ForeignKey("material.id"))
    assay: Mapped[int]
    karat: Mapped[float]
    data: Mapped[datetime] = mapped_column(DATETIME)
    popularity: Mapped[int] = mapped_column(default=0)
    image: Mapped[str]

    type: Mapped["Type"] = relationship()
    material: Mapped["Material"] = relationship()

    orders: Mapped["Order"] = relationship(back_populates="product", cascade="all, delete-orphan")

class Type(Base):
    __tablename__ = "type"
    name: Mapped[str]

class Material(Base):
    __tablename__ = "material"
    name: Mapped[str]
