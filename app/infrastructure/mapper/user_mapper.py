from app.domain.user.models import User
from app.infrastructure.entity.user_entity import UserEntity
from app.shared.utils import calculate_age


class UserMapper:
    @staticmethod
    def to_domain(user_entity: UserEntity) -> User:
        return User(
            id=user_entity.id,
            username=user_entity.username,
            nickname=user_entity.nickname,
            gender=user_entity.gender,
            birthday=user_entity.birthday,
            email=user_entity.email,
            phone=user_entity.phone,
            avatar=user_entity.avatar or "/static/default-avatar.png",
            description=user_entity.description,
            createdAt=user_entity.created_at,
            updatedAt=user_entity.updated_at,
            age=(
                None
                if user_entity.birthday is None
                else calculate_age(user_entity.birthday)
            ),
        )
