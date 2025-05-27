from http.client import responses, HTTPException

from fastapi import Query, status
from fastapi.params import Depends
from sqlalchemy.orm import Session
from sqlalchemy.sql.annotation import Annotated

from server.src.database_helper import get_db
from server.src.model.Database import User
from server.src.model.Schemas import UserRead, UserCreate, ProductCreate


# Создать нового пользователя

def create_user(user: UserCreate, db: Session = Depends(get_db())):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# Получить список всех пользователей
def read_users(limit: Annotated[int | None, Query()], db: Session = Depends(get_db)):
    if limit is None:
        return db.query(User).all()

    return db.query(User).limit(limit).all()

# Получить пользователя по id
def read_user(user_id: int, db: Session = Depends(get_db)):
    if product := db.query(User).get(user_id):
        return product

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Comment not found")

# Обновить пользователя по id
def update_user(user_id: int, new_user_id: ProductCreate, db: Session = Depends(get_db)):
    user = read_user(user_id, db)
    for key, value in user_id.dict().items():
        setattr(new_user_id, key, value)

    db.commit()
    db.refresh(user)
    return user


# Удалить пользователя по id
def delete_user(user_id: int, db: Session = Depends(get_db())):
    user = read_user(user_id, db)
    db.delete(user)
    db.commit()
    return {"detail": "User deleted"}

