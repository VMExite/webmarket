from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, HTTPException, Depends

from server.api_v1 import BaseUser, UpdateUser
from server.api_v1.auth.views import user_app

router = APIRouter(tags=["Users"])

router.include_router(
    user_app.get_users_router(
        user_schema=BaseUser,
        user_update_schema=UpdateUser
    ),
    prefix="/users")
