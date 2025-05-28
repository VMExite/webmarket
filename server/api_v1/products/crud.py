'''
    Create
    Read
    Update
    Delete
'''


from sqlalchemy import select
from core.models import Product
from .schemas import CreateProduct
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession


async def get_products(session: AsyncSession) -> list[Product]:
    statement = select(Product).order_by(Product.id)
    res: Result = await session.execute(statement)
    products = res.scalars().all()
    return list(products)


async def get_product(session: AsyncSession, _id: int) -> Product | None:
    return await session.get(Product, _id)


async def create_product(session: AsyncSession, product: CreateProduct) -> Product:
    product = Product(**product.model_dump())
    session.add(product)
    await session.commit()
    # await session.refresh(product)
    return product