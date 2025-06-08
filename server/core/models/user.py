from typing import List, TYPE_CHECKING

from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase, SQLAlchemyBaseUserTable
from sqlalchemy import String
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column
from server.core.models.base_model import Base

if TYPE_CHECKING:
    from server.core.models.order import Order


class User(SQLAlchemyBaseUserTable,Base):
    __tablename__ = "user"

    login: Mapped[str] = mapped_column(String(25))
    orders: Mapped[List["Order"]] = relationship(back_populates="user", cascade="all, delete-orphan")
