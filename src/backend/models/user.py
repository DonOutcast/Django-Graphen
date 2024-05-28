from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from base import Base, int_pk


class User(Base):
    __tablename__ = "users"

    user_id: Mapped[int_pk]
    username: Mapped[str] = mapped_column(String(60))
    hashed_password: Mapped[str] = mapped_column(String(250))
    role_id: Mapped[int] = mapped_column(ForeignKey("role.role_id"))
    relationship("Role")
