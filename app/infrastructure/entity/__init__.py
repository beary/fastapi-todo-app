from app.infrastructure.database import Base
from app.infrastructure.entity.todo_entity import TodoEntity
from app.infrastructure.entity.user_entity import UserEntity

all_entities = [
    TodoEntity,
    UserEntity,
]

BaseEntity = Base
