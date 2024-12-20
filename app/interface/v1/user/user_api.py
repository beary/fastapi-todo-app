from typing import Annotated

from fastapi import APIRouter, Depends, Response, Security

from app.application.user_service import UserService
from app.dependencies import JWTClaims, get_jwt_claims, token_cookie_name
from app.domain.user.models import User
from app.infrastructure.service.jwt_service import JwtService
from app.interface.v1.user.user_request import UserLoginRequest, UserRegisterRequest
from app.interface.v1.user.user_response import LoginResponse, RegisterResponse
from app.shared.enums import UserRole
from app.shared.types import Result

router = APIRouter()


@router.post(path="/register", response_model=Result[RegisterResponse])
async def register(
    request: UserRegisterRequest,
    user_service: Annotated[UserService, Depends(UserService)],
    jwt_service: Annotated[JwtService, Depends(JwtService)],
    response: Response,
) -> Result[RegisterResponse]:
    user = await user_service.register(request.username, request.password)
    access_token = jwt_service.get_token(user.id, UserRole.USER)
    response.set_cookie(key=token_cookie_name, value=access_token)
    return Result.new(RegisterResponse(access_token=access_token))


@router.post(path="/login", response_model=Result[LoginResponse])
async def login(
    request: UserLoginRequest,
    user_service: Annotated[UserService, Depends(UserService)],
    jwt_service: Annotated[JwtService, Depends(JwtService)],
    response: Response,
) -> Result[LoginResponse]:
    user = await user_service.login(request.username, request.password)
    access_token = jwt_service.get_token(user.id, UserRole.USER)
    response.set_cookie(key=token_cookie_name, value=access_token)
    return Result.new(LoginResponse(access_token=access_token))


@router.get(path="/whoami", response_model=Result[User])
async def whoami(
    user_service: Annotated[UserService, Depends(UserService)],
    jwt_claims: Annotated[JWTClaims, Security(get_jwt_claims, scopes=[UserRole.USER])],
) -> Result[User]:
    user = await user_service.get_user_by_id(jwt_claims.user_id)
    return Result.new(user)
