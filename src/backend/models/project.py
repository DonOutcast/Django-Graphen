from sqlalchemy import ForeignKey, String, Text, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship

from base import Base, int_pk


class Project(Base):
    id: Mapped[int_pk]
    name: Mapped[str] = mapped_column(String(60))
    description: Mapped[str] = mapped_column(Text)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.user_id"))
    users = relationship("User", secondary="user_projects")

    user_projects = Table(
        "user_projects", Base.metadata,
        Column("user_id", ForeignKey("users.user_id"), primary_key=True),
        Column("project_id", ForeignKey("projects.id"), primary_key=True)
    )
