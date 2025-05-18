from typing import Annotated

from fastapi import APIRouter, Depends, Query

from server.src.database_helper import get_db
from server.src.model.Schemas import ProductRead, ProductCreate

from sqlalchemy.orm import Session


product_router = APIRouter(tags=['product'])



@product_router.post('/', response_model=ProductRead)
def create_products(product_in: ProductCreate, db: Session = Depends(get_db())):
    return create_products(db, product_in=product_in)


@product_router.get('/', response_model=list[ProductRead])
def get_products(limit: Annotated[int | None, Query()], db: Session = Depends(get_db)):
    return get_products(db, limit=limit)


@product_router.get('/{id}', response_model=ProductRead)
def get_product(product_id: int, db: Session = Depends(get_db)):
    return get_product(db, product_id=product_id)


@product_router.put('/{id}', response_model=ProductRead)
def update_product(product_id: int, product_in: ProductCreate, db: Session = Depends(get_db)):
    return update_product(db, product_id=product_id, product_in=product_in)


@product_router.delete('/{id}', response_model=ProductRead)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    return delete_product(db, product_id=product_id)
