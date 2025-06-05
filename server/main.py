from contextlib import asynccontextmanager

from server.core.models import db_helper
from server.core.models import Base
from server.core.config import settings

from api_v1 import router as api_v1_router

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(api_v1_router, prefix=settings.api_v1_prefix)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],  # Только ваш фронтенд
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Content-Type", "Authorization"],
)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)