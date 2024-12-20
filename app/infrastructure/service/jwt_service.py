from datetime import UTC, datetime, timedelta

import jwt

from app.settings import settings
from app.shared.enums import UserRole


class JwtService:
    def get_token(self, user_id: str, scope: UserRole) -> str:
        claims = {
            "exp": datetime.now(UTC) + timedelta(days=7),
            "sub": user_id,
            "scopes": [scope],
        }
        return jwt.encode(
            payload=claims,
            key=settings.JWT_SECRET,
            algorithm="HS256",
        )
