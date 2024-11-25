from uuid import UUID

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.domain.constants import NAME_MAX_LENGTH, SURNAME_MAX_LENGTH
from src.infrastructure.models.base import BaseModel


class StudentModel(BaseModel):
    """Модель студента для БД."""

    __tablename__ = "student"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(NAME_MAX_LENGTH))
    surname: Mapped[str] = mapped_column(String(SURNAME_MAX_LENGTH))
