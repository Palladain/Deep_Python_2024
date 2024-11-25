from fastapi import FastAPI

from src.presentation.api.v1.factory import create_api_v1


def create_app() -> FastAPI:
    """Фабрика веб-сервера."""
    app = FastAPI()

    api_v1 = create_api_v1()
    app.include_router(api_v1)

    return app
