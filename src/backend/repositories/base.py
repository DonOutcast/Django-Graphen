from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List

from sqlalchemy.ext.asyncio import AsyncSession

T = TypeVar("T")


class BaseRepository(ABC, Generic[T]):
    def __init__(self, db: AsyncSession):
        self.db = db

    @abstractmethod
    async def get(self, id: int) -> T:
        pass

    @abstractmethod
    async def get_all(self, skip: int = 0, limit: int = 10) -> List[T]:
        pass

    @abstractmethod
    async def create(self, obj: T) -> T:
        pass

    @abstractmethod
    async def update(self, id: int, obj: T) -> T:
        pass

    @abstractmethod
    async def delete(self, id: int) -> None:
        pass
