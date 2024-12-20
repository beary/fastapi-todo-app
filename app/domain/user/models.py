from dataclasses import dataclass
from datetime import date, datetime

from app.domain.user.enums import Gender


@dataclass
class User:
    id: str
    username: str
    nickname: str
    gender: Gender | None
    birthday: date | None
    age: int | None
    email: str | None
    phone: str | None
    avatar: str
    description: str | None
    createdAt: datetime
    updatedAt: datetime
