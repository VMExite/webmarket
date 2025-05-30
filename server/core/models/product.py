from sqlalchemy import DATETIME
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base_model import Base

class Product(Base):
    __tablename__ = "product"
    name: Mapped[str]
    description: Mapped[str]
    price: Mapped[int]
    type: Mapped["Type"] = relationship(back_populates="user")
    material: Mapped["Material"]
    color: Mapped["Color"]
    assay: Mapped[int]
    karat: Mapped[float]
    data: Mapped[DATETIME]
    popularity: Mapped[int] = mapped_column(default=0)
    image: Mapped[str]

class Type(Base):
    __tablename__ = "type"
    name: Mapped[str]

class Material(Base):
    __tablename__ = "material"
    name: Mapped[str]

class Color(Base):
    __tablename__ = "color"
    name: Mapped[str]