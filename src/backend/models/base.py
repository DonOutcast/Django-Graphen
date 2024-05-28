from sqlalchemy.orm import DeclarativeBase, mapped_column
from typing_extensions import Annotated


int_pk = Annotated[int, mapped_column(primary_key=True, autoincrement=True)]


class Base(DeclarativeBase):
    pass