import os
from uuid import uuid4

from asyncpg import Connection
from sqlalchemy import NullPool, create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, Session

""" Настройки БД """

DB_USER = os.environ.get('DB_USER', "username")
DB_PASS = os.environ.get('DB_PASS', "password")
DB_NAME = os.environ.get('DB_NAME', "postgres")
DB_HOST = os.environ.get('DB_HOST', "localhost")
DB_PORT = str(os.environ.get('DB_PORT', 5432))


class CConnection(Connection):
    def _get_unique_id(self, prefix):
        return f"__asyncpg_{prefix}_{uuid4()}__"


DATABASE_URL2 = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

sync_db = create_engine(DATABASE_URL2)

sync_session = sessionmaker(bind=sync_db, class_=Session, expire_on_commit=False, autoflush=False)

""" Асинхронные сессии"""


def get_sync_session() -> Session:
    with sync_session() as session:
        return session
