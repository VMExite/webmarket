from fastapi import APIRouter
from fastapi_users import fastapi_users, FastAPIUsers

from .auth.auth import jwt_authentication
from .auth.user_manager import get_user_manager
from .products.views import router as product_router
from .users.schemas import ReadUser, CreateUser, BaseUser
from .users.views import router as user_router
from ..core.models import User

router = APIRouter()
fastapi_users = FastAPIUsers[User, int] (
    get_user_manager,
    [jwt_authentication])

router.include_router(product_router, prefix="/products")
router.include_router(user_router, prefix="/users")

router.include_router(
    fastapi_users.get_register_router(
        user_schema=BaseUser,
        user_create_schema=CreateUser
    ),
    prefix="/register",)

router.include_router(
    fastapi_users.get_auth_router(jwt_authentication),
    prefix="/auth",)

router.include_router(
    fastapi_users.get_users_router(),
    prefix="/users",)