from dataclasses import dataclass
from typing import Annotated

import jwt
from fastapi import Depends, HTTPException, Request, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer, SecurityScopes

from app.infrastructure.database import AsyncSessionLocal
from app.settings import settings
from app.shared.enums import UserRole


async def get_db():
    db = AsyncSessionLocal()
    try:
        yield db
    finally:
        await db.close()


auth_schema = HTTPBearer(auto_error=False)
token_cookie_name = "access_token"


@dataclass
class JWTClaims:
    user_id: str
    scopes: list[UserRole]


async def get_jwt_claims(
    scopes: SecurityScopes,
    request: Request,
    cred: Annotated[HTTPAuthorizationCredentials | None, Depends(auth_schema)],
) -> JWTClaims:
    try:
        credentials = (
            cred.credentials
            if cred is not None
            else request.cookies.get(token_cookie_name)
        )
        if not credentials:
            raise jwt.InvalidTokenError()

        payload = jwt.decode(
            jwt=credentials,
            key=settings.JWT_SECRET,
            algorithms=["HS256"],
        )

        user_id: str = payload.get("sub", "")
        payload_scopes: list[UserRole] = payload.get("scopes", [])

        if all(scope not in scopes.scopes for scope in payload_scopes):
            raise jwt.InvalidTokenError()

        return JWTClaims(
            user_id=user_id,
            scopes=payload_scopes,
        )
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
