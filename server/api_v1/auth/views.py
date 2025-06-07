from fastapi.routing import APIRouter
from fastapi_users import FastAPIUsers

from server.api_v1 import get_user_manager, jwt_authentication
from server.api_v1.users.schemas import BaseUser, CreateUser
from server.core.models import User

auth_router = APIRouter(tags=["Auth"])
user_app = FastAPIUsers[User, int] (
    get_user_manager,
    [jwt_authentication]
)


auth_router.include_router(
    user_app.get_register_router(
        user_schema=BaseUser,
        user_create_schema=CreateUser,
    ),
    prefix="/register")


auth_router.include_router(
    user_app.get_auth_router(jwt_authentication),
    prefix="/auth")

