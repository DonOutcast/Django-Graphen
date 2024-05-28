from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

from models.base import Base, int_pk


class Role(Base):
    role_id: Mapped[int_pk]
    name: Mapped[str] = mapped_column(String(256))
