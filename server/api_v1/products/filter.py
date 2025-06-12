from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.engine import Result
from server.api_v1.products.schemas import FilterData
from server.core.models import Product


async def filter_products(filter_factors: FilterData, session: AsyncSession) -> list[Product]:
    products = select(Product)
    excluding_filter : FilterData = FilterData(**filter_factors.model_dump(exclude_none=True, exclude_unset=True))

    if excluding_filter.type and filter_factors.type.id is not None:
        products = products.where(Product.type_id == filter_factors.type.id)

    if excluding_filter.material and filter_factors.material.id is not None:
        products = products.where(Product.material_id == filter_factors.material.id)

    if filter_factors.min_cost is not None:
        products = products.where(Product.price >= filter_factors.min_cost)

    if filter_factors.max_cost is not None:
        products = products.where(Product.price <= filter_factors.max_cost)

    result : Result = await session.execute(products)
    filtered_products = result.scalars().all()
    return list(filtered_products)