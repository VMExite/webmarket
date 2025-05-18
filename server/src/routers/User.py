from http.client import responses, HTTPException

import router
from fastapi.params import Depends
from sqlalchemy.orm import Session

from server.src.database_helper import get_db
from server.src.model.Database import User
from server.src.model.Schemas import UserRead, UserCreate


# Создать нового пользователя
@router.post('/', response_model=UserRead)
def create_user(user: UserCreate, db: Session = Depends(get_db())):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# Получить список всех пользователей
@router.get('/', response_model=list[UserRead])
def read_users(db: Session = Depends(get_db())):
    return db.query(User).all()


# Получить пользователя по id
@router.get('/{user_id}', response_model=UserRead)
def read_user(user_id: int, db: Session = Depends(get_db())):
    user = db.query(User).get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    else: return user


# Обновить пользователя по id
@router.put('/{user_id}', response_model=UserRead)
def update_user(user_id:int, user_data: UserCreate, db: Session = Depends(get_db())):
    user = read_user(user_id,db)

    for key, value in user_data.dict().items():
        setattr(user, key, value)

    db.commit()
    db.refresh(user)
    return user


# Удалить пользователя по id
@router.delete('/{user_id}', response_model=UserRead)
def delete_user(user_id: int, db: Session = Depends(get_db())):
    user = read_user(user_id, db)

    db.delete(user)
    db.commit()

    return {"detail": "User deleted"}

