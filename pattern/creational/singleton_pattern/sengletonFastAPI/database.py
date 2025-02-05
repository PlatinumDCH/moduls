from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker,declarative_base
from enum import Enum

class URLDatabase(str, Enum):
    database_url = "sqlite+aiosqlite:///:memory:"

base = declarative_base()

class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance.init_db()
        return cls._instance
    
    def init_db(self):
        self.engine = create_async_engine(
            URLDatabase.database_url,
            connect_args={"check_same_thread": False}
        )
        self.async_session = sessionmaker(
            class_=AsyncSession, expire_on_commit=False
        )
    
    async def get_session(self):
        async with self.async_session(bind=self.engine) as session:
            yield session

    async def crate_tables(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(base.metadata.create_all)

db = Database()