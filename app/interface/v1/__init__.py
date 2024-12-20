from fastapi import FastAPI

from app.interface.v1.todo import todo_api
from app.interface.v1.user import user_api


def mount(app: FastAPI) -> None:
    app.include_router(
        router=todo_api.router,
        prefix="/api/todo",
        tags=["Todo"],
    )

    app.include_router(
        router=user_api.router,
        prefix="/api/user",
        tags=["User"],
    )
