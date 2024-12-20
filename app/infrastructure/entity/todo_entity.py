from datetime import datetime

from sqlalchemy import TIMESTAMP, SmallInteger, String, func
from sqlalchemy.orm import Mapped, mapped_column

from app.domain.todo.enums import TodoStatus
from app.infrastructure.database import Base
from app.shared.utils import guid


class TodoEntity(Base):
    __tablename__ = "todo"

    id: Mapped[str] = mapped_column(String, primary_key=True, insert_default=guid)
    user_id: Mapped[str] = mapped_column(String)
    title: Mapped[str] = mapped_column(String)
    status: Mapped[TodoStatus] = mapped_column(
        SmallInteger,
        insert_default=TodoStatus.TODO,
    )
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        insert_default=func.current_timestamp(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        insert_default=func.current_timestamp(),
        onupdate=func.current_timestamp(),
    )
