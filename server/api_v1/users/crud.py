from fastapi.params import Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy import select
from server.core.models.user import User
from .schemas import CreateUser
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession


async def get_users(session: AsyncSession) -> list[User]:
    statement = select(User).order_by(User.id)
    res: Result = await session.execute(statement)
    users = res.scalars().all()
    return list(users)


async def get_user(session: AsyncSession, _id: int) -> User | None:
    return await session.get(User, _id)

async def create_user(session: AsyncSession, user_in: CreateUser) -> User:
    user = User(**user_in.model_dump())
    session.add(user)
    await session.commit()
    # await session.refresh(user)
    return user

async def get_user_db(session: AsyncSession):
    yield SQLAlchemyUserDatabase(session, User)