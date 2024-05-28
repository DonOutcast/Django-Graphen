from datetime import timedelta
from typing import AsyncGenerator
import logging

import redis
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker, AsyncEngine, AsyncConnection
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import DBAPIError

from settings import settings

logger = logging.getLogger(__name__)
DATABASE_URL = ""
Base = declarative_base()


def create_engine() -> AsyncEngine:
    return create_async_engine(DATABASE_URL, class_=AsyncSession, expire_on_commit=False, echo=True)


def create_async_sessionmaker(bind_engine: AsyncEngine | AsyncConnection) -> async_sessionmaker:
    return async_sessionmaker(bind=bind_engine, class_=AsyncSession, expire_on_commit=False)


async def get_session() -> AsyncGenerator:
    async with async_sessionmaker() as session:
        try:
            yield session
        except DBAPIError as db_exc:
            logger.exception(f"ERROR {db_exc}")
        finally:
            await session.rollback()


def store_token(token: str, user_id: int):
    redis_client.setex(token, timedelta(minutes=access_token_expires_minutes), user_id)


def get_user_id_from_token(token: str):
    return redis_client.get(token)


def refresh_token(token: str):
    redis_client.expire(token, timedelta(minutes=access_token_expires_minutes))


engine: AsyncEngine = create_engine()
async_sessionmaker = create_async_sessionmaker(engine)

redis_client = redis.StrictRedis.from_url(settings.get_redis_url)
access_token_expires_minutes = settings.access_token_expire_minutes
