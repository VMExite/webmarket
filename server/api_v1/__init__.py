from fastapi import APIRouter

from .products.views import router as product_router
from .users.views import router as user_router

router = APIRouter()
router.include_router(product_router, prefix="/products")
router.include_router(user_router, prefix="/users")