from typing import List

from sqlalchemy.future import select

from base import BaseRepository
from models import Role
from schemas import RoleCreate


class RoleRepository(BaseRepository[Role]):
    async def get(self, id: int) -> Role | None:
        result = await self.db.execute(select(Role).filter(Role.role_id == id))
        return result.scalars().first()

    async def get_all(self, skip: int = 0, limit: int = 10) -> List[Role]:
        result = await self.db.execute(select(Role).offset(skip).limit(limit))
        return result.scalars().all()

    async def create(self, role: RoleCreate) -> Role:
        db_role = Role(name=role.name)
        self.db.add(db_role)
        await self.db.commit()
        await self.db.refresh(db_role)
        return db_role

    async def update(self, id: int, role: RoleCreate) -> Role:
        result = await self.db.execute(select(Role).filter(Role.role_id == id))
        db_role = result.scalars().first()
        if db_role:
            db_role.name = role.name
            await self.db.commit()
            await self.db.refresh(db_role)
        return db_role

    async def delete(self, id: int) -> None:
        result = await self.db.execute(select(Role).filter(Role.role_id == id))
        db_role = result.scalars().first()
        if db_role:
            await self.db.delete(db_role)
            await self.db.commit()
