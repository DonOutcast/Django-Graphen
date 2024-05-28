from pydantic import BaseModel
from typing import List, Optional


class RoleBase(BaseModel):
    name: str


class RoleCreate(RoleBase):
    pass


class Role(RoleBase):
    role_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    user_id: int
    role: Role

    class Config:
        orm_mode = True


class ProjectBase(BaseModel):
    name: str
    description: Optional[str] = None


class ProjectCreate(ProjectBase):
    pass


class ProjectUpdate(ProjectBase):
    pass


class Project(ProjectBase):
    id: int
    users: List[User] = []

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


class ProjectLogBase(BaseModel):
    action: str


class ProjectLogCreate(ProjectLogBase):
    pass


class ProjectLog(ProjectLogBase):
    log_id: int
    project_id: int
    user_id: int
    timestamp: str

    class Config:
        orm_mode = True
