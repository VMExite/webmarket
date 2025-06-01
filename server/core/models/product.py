from sqlalchemy import DATETIME, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base_model import Base

class Product(Base):
    __tablename__ = "product"
    name: Mapped[str]
    description: Mapped[str]
    price: Mapped[int]
    type_id: Mapped[int] = mapped_column(ForeignKey("type.id"))
    material_id: Mapped[int] = mapped_column(ForeignKey("material.id"))
    color_id: Mapped[int] = mapped_column(ForeignKey("color.id"))
    assay: Mapped[int]
    karat: Mapped[float]
    data: Mapped[DATETIME]
    popularity: Mapped[int] = mapped_column(default=0)
    image: Mapped[str]

    type: Mapped["Type"] = relationship()
    material: Mapped["Material"] = relationship()
    color: Mapped["Color"] = relationship()

class Type(Base):
    __tablename__ = "type"
    name: Mapped[str]

class Material(Base):
    __tablename__ = "material"
    name: Mapped[str]

class Color(Base):
    __tablename__ = "color"
    name: Mapped[str]