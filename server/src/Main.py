from sqlalchemy.orm import DeclarativeBase, sessionmaker
from server.src.model.Database import SessionLocal, User
from server.src.model.Database import Base, engine


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    Base.metadata.create_all(bind=engine)



def main():
    # Получаем сессию через генератор
    db = next(get_db())

    # Получаем первого пользователя
    user = db.query(User).first()

    # Проверяем, есть ли пользователь
    if user and user.role_data:
        print(f"User: {user.login}, Role: {user.role_data.name}")
    else:
        print("No user or role found")


if __name__ == "__main__":
    main()
