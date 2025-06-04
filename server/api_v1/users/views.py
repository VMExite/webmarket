from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, HTTPException, Depends

from . import crud
from .schemas import ReadUser, CreateUser
from server.core.models.database_helper import db_helper

router = APIRouter(tags=["Users"])


@router.get("/", response_model=list[ReadUser])
async def get_users(session: AsyncSession = Depends(dependency=db_helper.session_dependency)):
    return await crud.get_users(session=session)


@router.get("/{user_id}", response_model=ReadUser)
async def get_product(user_id: int, session: AsyncSession = Depends(dependency=db_helper.session_dependency)):
    user = await crud.get_user(session=session, _id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail=f"User with {user_id} id not found")
    return user


@router.post("/", response_model=ReadUser)
async def create_user(user_in: CreateUser, session: AsyncSession = Depends(dependency=db_helper.session_dependency)):
    return await crud.create_user(session=session, user_in=user_in)
