from typing import List

from sqlalchemy import String
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column

from server.core.models import Base
from server.core.models.order import Order


class User(Base):
    __tablename__ = "user"

    login: Mapped[str] = mapped_column(String(25))
    email: Mapped[str] = mapped_column(String(50))
    password: Mapped[str]
    favor_orders: Mapped[List["Order"]] = relationship(back_populates="user", cascade="all, delete-orphan")
