from typing import TYPE_CHECKING
from datetime import datetime

from sqlalchemy import ForeignKey, DATETIME
from sqlalchemy.orm import Mapped, mapped_column, relationship
from server.core.models.base_model import Base

if TYPE_CHECKING:
    from server.core.models.product import Product
    from server.core.models.user import User


class Order(Base):
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    product_id: Mapped[int] = mapped_column(ForeignKey("product.id"))
    order_time: Mapped[datetime] = mapped_column(DATETIME)

    user: Mapped["User"] = relationship(back_populates="orders")
    product: Mapped["Product"] = relationship(back_populates="orders")
