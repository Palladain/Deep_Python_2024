from typing import Final

from fastapi import APIRouter

from src.presentation.api.v1.routers import students

PREFIX: Final[str] = "/api/v1"


def create_api_v1() -> APIRouter:
    """Фабрика первой версии API."""
    router = APIRouter(prefix=PREFIX)

    router.include_router(students.router)

    return router
