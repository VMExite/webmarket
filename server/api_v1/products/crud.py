"""
    Create
    Read
    Update
    Delete
"""


from sqlalchemy import select
from server.core.models import Product
from server.api_v1.products.schemas import CreateProduct
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from server.core.models.product import Material, Color, Type

async def get_products(session: AsyncSession) -> list[Product]:
    statement = select(Product).order_by(Product.id)
    res: Result = await session.execute(statement)
    products = res.scalars().all()
    return list(products)


async def get_product(session: AsyncSession, _id: int) -> Product | None:
    return await session.get(Product, _id)


async def create_product(session: AsyncSession, product_in: CreateProduct) -> Product:
    product = Product(**product_in.model_dump(by_alias=True))

    session.add(product)
    await session.commit()
    # await session.refresh(product)
    return product

