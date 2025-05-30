from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, HTTPException, Depends

from . import crud
from .schemas import Product, CreateProduct
from core.models import db_helper

router = APIRouter(tags=["Products"])


@router.get("/", response_model=list[Product])
async def get_products(session: AsyncSession = Depends(dependency=db_helper.session_dependency)):
    return await crud.get_products(session=session)


@router.get("/{product_id}", response_model=Product)
async def get_product(product_id: int, session: AsyncSession = Depends(dependency=db_helper.session_dependency)):
    product = await crud.get_product(session=session, _id=product_id)
    if not product:
        raise HTTPException(status_code=404, detail=f"Product with {product_id} id not found")
    return product


@router.post("/", response_model=Product)
async def create_router(product_in: CreateProduct, session: AsyncSession = Depends(dependency=db_helper.session_dependency)):
    return await crud.create_product(session=session, product=product_in)
