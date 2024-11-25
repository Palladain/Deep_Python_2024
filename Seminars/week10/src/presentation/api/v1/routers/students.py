from typing import Final
from uuid import UUID

from fastapi import APIRouter

from src.domain.entities.student import Student

TAG: Final[str] = "students"
PREFIX: Final[str] = f"/{TAG}"


router = APIRouter(prefix=PREFIX, tags=[TAG])


@router.post("")
async def register_student(student: Student) -> UUID:
    """Зарегистрировать студента в системе."""
    raise NotImplementedError
