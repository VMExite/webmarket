from typing import Annotated

from fastapi import Depends, Query, status, HTTPException

from server.src.database_helper import get_db
from server.src.model.Schemas import ProductCreate
from server.src.model.Database import Product

from sqlalchemy.orm import Session


def create_product(product_in: ProductCreate, db: Session = Depends(get_db())):
    db_product = Product(**product_in.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def read_products(limit: Annotated[int | None, Query()], db: Session = Depends(get_db)):
    if limit is None:
        return db.query(Product).all()

    return db.query(Product).limit(limit).all()


def read_product(product_in: int, db: Session = Depends(get_db)):
    if product := db.query(Product).get(product_in):
        return product

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Comment not found")


def update_product(product_id: int, product_in: ProductCreate, db: Session = Depends(get_db)):
    product = read_product(product_id, db)
    for key, value in product_in.dict().items():
        setattr(product, key, value)

    db.commit()
    db.refresh(product)
    return product


def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = read_product(product_id, db)
    db.delete(product)
    db.commit()
    return {"detail": "product deleted"}