from dataclasses import dataclass
from datetime import datetime

from app.domain.todo.enums import TodoStatus


@dataclass
class Todo:
    id: str
    title: str
    status: TodoStatus
    createdAt: datetime
    updatedAt: datetime
