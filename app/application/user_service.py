from typing import Annotated

from fastapi import Depends
from sqlalchemy import exists, select
from sqlalchemy.ext.asyncio.session import AsyncSession

from app.dependencies import get_db
from app.domain.user.errors import UnauthorizedError, UserNameExistsError
from app.domain.user.models import User
from app.infrastructure.entity.user_entity import UserEntity
from app.infrastructure.mapper.user_mapper import UserMapper
from app.infrastructure.service.bcrypt_service import BcryptService
from app.shared.errors import NotFoundError


class UserService:
    db: AsyncSession
    bcrypt_service: BcryptService

    def __init__(
        self,
        db: Annotated[AsyncSession, Depends(get_db)],
        bcrypt_service: Annotated[BcryptService, Depends(BcryptService)],
    ) -> None:
        self.db = db
        self.bcrypt_service = bcrypt_service

    async def register(self, username: str, password: str) -> User:
        if await self.db.scalar(
            exists(UserEntity).where(UserEntity.username == username).select()
        ):
            raise UserNameExistsError()
        user_entity = UserEntity()
        user_entity.username = username
        user_entity.nickname = username
        user_entity.password = self.bcrypt_service.hash_password(password)
        self.db.add(user_entity)
        await self.db.commit()
        await self.db.refresh(user_entity)
        return UserMapper.to_domain(user_entity)

    async def login(self, username: str, password: str) -> User:
        user_entity = await self.db.scalar(
            select(UserEntity).where(UserEntity.username == username)
        )
        if not user_entity:
            raise NotFoundError(message="User not exists")
        if (
            user_entity.password is not None
            and not self.bcrypt_service.verify_password(password, user_entity.password)
        ):
            raise UnauthorizedError(message="Invalid password")
        return UserMapper.to_domain(user_entity)

    async def get_user_by_id(self, user_id: str) -> User:
        user_entity = await self.db.scalar(
            select(UserEntity).where(UserEntity.id == user_id)
        )
        if not user_entity:
            raise NotFoundError(message="User not exists")
        return UserMapper.to_domain(user_entity)
