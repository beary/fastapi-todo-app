from app.domain.todo.models import Todo
from app.infrastructure.entity.todo_entity import TodoEntity


class TodoMapper:
    @staticmethod
    def to_domain(todo_entity: TodoEntity) -> Todo:
        return Todo(
            id=todo_entity.id,
            title=todo_entity.title,
            status=todo_entity.status,
            createdAt=todo_entity.created_at,
            updatedAt=todo_entity.updated_at,
        )
