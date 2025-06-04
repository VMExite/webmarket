from asyncio import current_task

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession, async_scoped_session

from server.core.config import settings


class DatabaseHelper:
    def __init__(self, db_url: str = None, echo: bool = False):
        self.engine = create_async_engine(
            url=db_url,
            echo=echo
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            expire_on_commit=False,
            autocommit=False,
            autoflush=False
        )

    def get_scoper_session(self) -> async_scoped_session:
        scoped_session = async_scoped_session(
            session_factory=self.session_factory,
            scopefunc=current_task
        )
        return scoped_session


    async def session_dependency(self) -> AsyncSession:
        session = self.get_scoper_session()
        yield session
        await session.close()


db_helper = DatabaseHelper(
    db_url=settings.db_url,
    echo=settings.echo,
)