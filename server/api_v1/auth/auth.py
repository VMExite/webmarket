from fastapi_users import FastAPIUsers

from fastapi_users.authentication import AuthenticationBackend, BearerTransport, JWTStrategy

from server.api_v1.auth.user_manager import UserManager, get_user_manager
from server.core.config import SECRET, JWT_EXPIRE_TIME
from server.core.models import User

bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")

def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=JWT_EXPIRE_TIME)

jwt_authentication = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)

