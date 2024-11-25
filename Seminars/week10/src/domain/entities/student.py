from uuid import UUID

from pydantic import BaseModel

from src.domain.dtypes import Name, Surname


class Student(BaseModel):
    """Сущность студента."""

    id: UUID
    name: Name
    surname: Surname
