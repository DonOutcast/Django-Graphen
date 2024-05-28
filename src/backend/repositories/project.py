from typing import List

from sqlalchemy.future import select
from base import BaseRepository
from models import Project, User
from schemas import ProjectCreate, ProjectUpdate


class ProjectRepository(BaseRepository[Project]):
    async def get(self, id: int) -> Project | None:
        result = await self.db.execute(select(Project).filter(Project.id == id))
        return result.scalars().first()

    async def get_all(self, skip: int = 0, limit: int = 10) -> List[Project]:
        result = await self.db.execute(select(Project).offset(skip).limit(limit))
        return result.scalars().all()

    async def create(self, project: ProjectCreate) -> Project:
        db_project = Project(name=project.name, description=project.description)
        self.db.add(db_project)
        await self.db.commit()
        await self.db.refresh(db_project)
        return db_project

    async def update(self, id: int, project_update: ProjectUpdate) -> Project:
        result = await self.db.execute(select(Project).filter(Project.id == id))
        db_project = result.scalars().first()
        if db_project:
            for key, value in project_update.dict().items():
                setattr(db_project, key, value)
            await self.db.commit()
            await self.db.refresh(db_project)
        return db_project

    async def delete(self, id: int) -> None:
        result = await self.db.execute(select(Project).filter(Project.id == id))
        db_project = result.scalars().first()
        if db_project:
            await self.db.delete(db_project)
            await self.db.commit()

    async def assign_project_to_user(self, user: User, project: Project):
        user.projects.append(project)
        await self.db.commit()
        return user
