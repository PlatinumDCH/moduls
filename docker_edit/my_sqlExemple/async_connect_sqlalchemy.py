import contextlib
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import text
import asyncio

url = "mysql+aiomysql://root:root@127.0.0.1:3306/test_db"

class DatabaseSessionManager:
    def __init__(self, url: str):
        self._engine: AsyncEngine | None = create_async_engine(url)
        self._session_maker: async_sessionmaker = async_sessionmaker(
            autoflush=False, autocommit=False, bind=self._engine
        )

    @contextlib.asynccontextmanager
    async def session(self):
        if self._session_maker is None:
            raise Exception("Session is not initialized")
        session = self._session_maker()
        try:
            yield session
        except Exception as err:
            await session.rollback()
            raise
        finally:
            await session.close()

    async def __aenter__(self) -> AsyncSession:
        """
        async method for enter in context manager.

        Returns:
            AsyncSession: async session .
        """
        return await self.session().__aenter__()

    async def __aexit__(self, exc_type, exc_value, traceback):
        """
        async method for exit in context manager.

        Args:
            exc_type: type connect (if yet).
            exc_value: value excpetion (if yet).
            traceback: trace back exception (if yet).
        """
        await self.session().__aexit__(exc_type, exc_value, traceback)


sessionmanager = DatabaseSessionManager(url)


async def get_connection():
    """
    Асинхронный генератор для получения сессии базы данных.

    Yields:
        AssyncSession: асинхронная сессия базы данных.
    """
    async with sessionmanager.session() as session:
        yield session



async def show_tables():
    async for session in get_connection():
        result = await session.execute(text("SHOW TABLES"))  # Выполняем SQL-запрос
        tables = result.scalars().all()  # Получаем список таблиц
        print("Таблицы в базе данных:", tables)


loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(show_tables())