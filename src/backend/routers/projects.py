from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from schemas import ProjectCreate, Project, User
from repositories import ProjectRepository, UserRepository
from utils import decode_access_token, get_user_id_from_token, refresh_token, get_session
from repositories import get_project_repository

router = APIRouter()


async def get_current_user(session: AsyncSession = Depends(get_session),
                           token: str = Depends(OAuth2PasswordBearer(tokenUrl="auth/token"))):
    payload = decode_access_token(token)
    if not payload:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials")
    user_id = get_user_id_from_token(token)
    if not user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Session expired")
    user_repo: UserRepository = UserRepository(session)
    user = await user_repo.get(user_id)
    refresh_token(token)
    return user


@router.post("/", response_model=Project)
async def create_project(
        project: ProjectCreate,
        current_user: User = Depends(get_current_user),
        project_repo: ProjectRepository = Depends(get_project_repository)
):
    if current_user.role.name != "admin":
        raise HTTPException(status_code=403, detail="Operation not permitted")
    db_project = await project_repo.create(project)
    return db_project
