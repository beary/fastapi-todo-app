from typing import Annotated

from fastapi import APIRouter, Depends, Security

from app.application.todo_service import TodoService
from app.dependencies import JWTClaims, get_jwt_claims
from app.domain.todo.models import Todo
from app.interface.v1.todo.todo_request import CreateTodoRequest, ProcessTodoRequest
from app.shared.enums import UserRole
from app.shared.types import ListResult, Result

router = APIRouter()


@router.post(path="/create", response_model=Result[Todo])
async def create_todo(
    request: CreateTodoRequest,
    jwt_claims: Annotated[JWTClaims, Security(get_jwt_claims, scopes=[UserRole.USER])],
    todo_service: Annotated[TodoService, Depends(TodoService)],
) -> Result[Todo]:
    todo = await todo_service.create_todo(
        title=request.title,
        user_id=jwt_claims.user_id,
    )

    return Result.new(todo)


@router.post(path="/process/{todo_id}", response_model=Result[bool])
async def process_todo(
    todo_id: str,
    request: ProcessTodoRequest,
    jwt_claims: Annotated[JWTClaims, Security(get_jwt_claims, scopes=[UserRole.USER])],
    todo_service: Annotated[TodoService, Depends(TodoService)],
) -> Result[bool]:
    await todo_service.process_todo(todo_id, jwt_claims.user_id, request.status)
    return Result.new(True)


@router.delete(path="/delete/{todo_id}", response_model=Result[bool])
async def delete_todo(
    todo_id: str,
    jwt_claims: Annotated[JWTClaims, Security(get_jwt_claims, scopes=[UserRole.USER])],
    todo_service: Annotated[TodoService, Depends(TodoService)],
) -> Result[bool]:
    await todo_service.delete_finished_todo(todo_id, jwt_claims.user_id)
    return Result.new(True)


@router.get(path="/list", response_model=Result[ListResult[Todo]])
async def get_todos(
    jwt_claims: Annotated[JWTClaims, Security(get_jwt_claims, scopes=[UserRole.USER])],
    todo_service: Annotated[TodoService, Depends(TodoService)],
) -> Result[ListResult[Todo]]:
    todos = await todo_service.get_todos(jwt_claims.user_id)
    return ListResult.new(todos)
