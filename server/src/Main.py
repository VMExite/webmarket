import uvicorn

from contextlib import asynccontextmanager
from server.src import database_helper as db_helper
from server.src.model.Database import Base, engine


from fastapi import FastAPI

from server.src.routers.products.views import product_router
from server.src.routers.users.views import user_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    with db_helper.engine.begin() as connection:
        connection.execute(Base.metadata.create_all(bind=engine))
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(product_router, prefix="/products")
app.include_router(user_router, prefix="/users")




if __name__ == "__main__":
    uvicorn.run("Main:app", reload=True)
