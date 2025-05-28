from sqlalchemy.orm import Mapped

from .base_model import Base

class Product(Base):
    # __tablename__ = "product"

    name: Mapped[str]
    description: Mapped[str]
    price: Mapped[int]