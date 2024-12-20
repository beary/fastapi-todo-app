from sqlalchemy import URL
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from app.settings import settings


class Base(AsyncAttrs, DeclarativeBase):
    pass


url_object = URL.create(
    drivername="postgresql+asyncpg",
    username=settings.PG_USERNAME,
    password=settings.PG_PASSWORD,
    host=settings.PG_HOST,
    port=settings.PG_PORT,
    database=settings.PG_DBNAME,
)

engine = create_async_engine(url=url_object, echo=True)
AsyncSessionLocal = async_sessionmaker(autocommit=False, autoflush=False, bind=engine)
