import uvicorn

from contextlib import asynccontextmanager
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from server.src.model.Database import User
from server.src import database_helper as db_helper
from server.src.model.Database import Base, engine


from fastapi import FastAPI
from server.src.routers.comments.views import comment_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    with db_helper.engine.begin() as connection:
        connection.execute(Base.metadata.create_all(bind=engine))
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(comment_router, prefix="/comments")




def main():
    # Получаем сессию через генератор
    db = next(db_helper.get_db())

    # Получаем первого пользователя
    user = db.query(User).first()

    # Проверяем, есть ли пользователь
    if user and user.role_data:
        print(f"User: {user.login}, Role: {user.role_data.name}")
    else:
        print("No user or role found")


if __name__ == "__main__":
    uvicorn.run("Main:app", reload=True)
    main()
