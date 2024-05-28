from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from role import RoleRepository
from user import UserRepository
from project import ProjectRepository
from utils import get_session


async def get_role_repository(session: AsyncSession = Depends(get_session)):
    return RoleRepository(session)


async def get_user_repository(session: AsyncSession = Depends(get_session)):
    return UserRepository(session)


async def get_project_repository(session: AsyncSession = Depends(get_session)):
    return ProjectRepository(session)


__all__ = [
    "get_role_repository",
    "get_user_repository",
    "get_project_repository",
    "ProjectRepository",
    "UserRepository"
]
