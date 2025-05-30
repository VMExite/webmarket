from sqlalchemy import ForeignKey, DATETIME
from sqlalchemy.orm import Mapped, mapped_column

from server.core.models import Base, Product
from server.core.models.user import User


class Order(Base):
    user_id: Mapped["User"] = mapped_column(ForeignKey("user.id"))
    product_id: Mapped["Product"] = mapped_column(ForeignKey("product.id"))
    order_time: Mapped[DATETIME]