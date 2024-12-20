from typing import Annotated

from fastapi import Depends
from sqlalchemy import delete, exists, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import get_db
from app.domain.todo.enums import TodoStatus
from app.domain.todo.models import Todo
from app.infrastructure.entity.todo_entity import TodoEntity
from app.infrastructure.mapper.todo_mapper import TodoMapper
from app.shared.errors import NotFoundError


class TodoService:
    db: AsyncSession

    def __init__(self, db: Annotated[AsyncSession, Depends(get_db)]):
        self.db = db

    async def create_todo(self, title: str, user_id: str) -> Todo:
        todo_entity = TodoEntity()
        todo_entity.title = title
        todo_entity.user_id = user_id
        self.db.add(todo_entity)
        await self.db.commit()
        await self.db.refresh(todo_entity)
        return TodoMapper.to_domain(todo_entity)

    async def process_todo(
        self, todo_id: str, user_id: str, status: TodoStatus
    ) -> None:
        if not await self.db.scalar(
            exists()
            .where(TodoEntity.id == todo_id, TodoEntity.user_id == user_id)
            .select()
        ):
            raise NotFoundError("Todo not found")
        await self.db.execute(
            update(TodoEntity)
            .where(TodoEntity.id == todo_id, TodoEntity.user_id == user_id)
            .values(status=status)
        )
        await self.db.commit()

    async def delete_finished_todo(self, todo_id: str, user_id: str) -> None:
        if not await self.db.scalar(
            exists()
            .where(
                TodoEntity.id == todo_id,
                TodoEntity.user_id == user_id,
                TodoEntity.status == TodoStatus.DONE,
            )
            .select()
        ):
            raise NotFoundError("Todo not found")
        await self.db.execute(delete(TodoEntity).where(TodoEntity.id == todo_id))
        await self.db.commit()

    async def get_todos(self, user_id: str) -> list[Todo]:
        todos = await self.db.scalars(
            select(TodoEntity)
            .where(TodoEntity.user_id == user_id)
            .order_by(TodoEntity.status.asc(), TodoEntity.created_at.desc())
        )
        return [TodoMapper.to_domain(todo) for todo in todos]
