from typing import Literal

from pydantic import BaseModel

from app.domain.todo.enums import TodoStatus


class CreateTodoRequest(BaseModel):
    title: str


class ProcessTodoRequest(BaseModel):
    status: Literal[TodoStatus.IN_PROGRESS, TodoStatus.DONE]
