from typing import Annotated

from fastapi import APIRouter, Depends, Query

from server.src.database_helper import get_db
from server.src.model.Schemas import ProductRead, ProductCreate

from sqlalchemy.orm import Session

from server.src.routers.users.User import create_user, read_users, update_user

user_router = APIRouter(tags=['users'])



@user_router.post('/', response_model=ProductRead)
def post_user(user_id: ProductCreate, db: Session = Depends(get_db())):
    return create_user(db, user=user_id)


@user_router.get('/', response_model=list[ProductRead])
def get_users(limit: Annotated[int | None, Query()], db: Session = Depends(get_db)):
    return read_users(db, limit=limit)


@user_router.get('/{id}', response_model=ProductRead)
def get_user(product_id: int, db: Session = Depends(get_db)):
    return get_user(db, user=product_id)


@user_router.put('/{id}', response_model=ProductRead)
def put_user(user_id: int, new_user_id: ProductCreate, db: Session = Depends(get_db)):
    return update_user(user_id, new_user_id, db)


@user_router.delete('/{id}', response_model=ProductRead)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return delete_user(user_id, db)
