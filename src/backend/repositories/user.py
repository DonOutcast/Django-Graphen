from typing import List

from sqlalchemy.future import select

from base import BaseRepository
from models import User
from schemas import UserCreate
from utils import get_password_hash


class UserRepository(BaseRepository[User]):
    async def get(self, id: int) -> User | None:
        result = await self.db.execute(select(User).filter(User.user_id == id))
        return result.scalars().first()

    async def get_all(self, skip: int = 0, limit: int = 10) -> List[User]:
        result = await self.db.execute(select(User).offset(skip).limit(limit))
        return result.scalars().all()

    async def create(self, user: UserCreate, role_id: int) -> User | None:
        hashed_password = get_password_hash(user.password)
        db_user = User(username=user.username, hashed_password=hashed_password, role_id=role_id)
        self.db.add(db_user)
        await self.db.commit()
        await self.db.refresh(db_user)
        return db_user

    async def update(self, id: int, user: UserCreate) -> User:
        result = await self.db.execute(select(User).filter(User.user_id == id))
        db_user = result.scalars().first()
        if db_user:
            db_user.username = user.username
            db_user.hashed_password = get_password_hash(user.password)
            db_user.role_id = user.role_id
            await self.db.commit()
            await self.db.refresh(db_user)
        return db_user

    async def delete(self, id: int) -> None:
        result = await self.db.execute(select(User).filter(User.user_id == id))
        db_user = result.scalars().first()
        if db_user:
            await self.db.delete(db_user)
            await self.db.commit()

    async def get_user_by_username(self, username: str) -> User | None:
        result = await self.db.execute(select(User).filter(User.username == username))
        return result.scalars().first()
