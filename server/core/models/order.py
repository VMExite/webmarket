from sqlalchemy import ForeignKey, DATETIME
from sqlalchemy.orm import Mapped, mapped_column, relationship

from server.core.models import Base, Product
from server.core.models.user import User


class Order(Base):
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    product_id: Mapped[int] = mapped_column(ForeignKey("product.id"))
    order_time: Mapped[DATETIME]

    user: Mapped["User"] = relationship()
    product: Mapped["Product"] = relationship()
