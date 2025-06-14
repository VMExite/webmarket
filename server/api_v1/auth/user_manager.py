from typing import Optional

from fastapi_users import BaseUserManager, IntegerIDMixin

from fastapi import Request, Depends

from server.api_v1.users.crud import get_user_db
from server.core.config import SECRET
from server.core.models import User


class UserManager(IntegerIDMixin,BaseUserManager[User, int]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")

    async def on_after_forgot_password(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        print(f"User {user.id} has forgot their password. Reset token: {token}")

    async def on_after_request_verify(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        print(f"Verification requested for user {user.id}. Verification token: {token}")

async def get_user_manager(user_db = Depends(get_user_db)):
    yield UserManager(user_db)