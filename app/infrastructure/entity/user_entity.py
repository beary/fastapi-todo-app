from datetime import date, datetime

from sqlalchemy import TIMESTAMP, Date, SmallInteger, String, func
from sqlalchemy.orm import Mapped, mapped_column

from app.domain.user.enums import Gender, UserStatus
from app.infrastructure.database import Base
from app.shared.utils import guid


class UserEntity(Base):
    __tablename__ = "user"

    id: Mapped[str] = mapped_column(String, primary_key=True, insert_default=guid)
    username: Mapped[str] = mapped_column(String)
    nickname: Mapped[str] = mapped_column(String)
    password: Mapped[str | None] = mapped_column(String, nullable=True)
    gender: Mapped[Gender | None] = mapped_column(SmallInteger, nullable=True)
    birthday: Mapped[date | None] = mapped_column(Date, nullable=True)
    email: Mapped[str | None] = mapped_column(String, nullable=True)
    phone: Mapped[str | None] = mapped_column(String, nullable=True)
    avatar: Mapped[str | None] = mapped_column(String, nullable=True)
    status: Mapped[UserStatus] = mapped_column(
        SmallInteger,
        insert_default=UserStatus.ACTIVE,
    )
    description: Mapped[str | None] = mapped_column(String, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        insert_default=func.current_timestamp(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        insert_default=func.current_timestamp(),
        onupdate=func.current_timestamp(),
    )
