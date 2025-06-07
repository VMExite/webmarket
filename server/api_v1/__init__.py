from fastapi import APIRouter
from fastapi_users import fastapi_users, FastAPIUsers

from .auth.auth import jwt_authentication
from .auth.user_manager import get_user_manager
from .auth.views import auth_router
from .products.views import router as product_router
from .users.schemas import ReadUser, CreateUser, BaseUser, UpdateUser
from .users.views import router as user_router

router = APIRouter()

router.include_router(product_router, prefix="/products")
router.include_router(user_router, prefix="/users")
router.include_router(auth_router, prefix="")

