from datetime import UTC, datetime

from fastapi import APIRouter

from app.interface.system.sys_response import HealthResponse
from app.shared.types import Result

router = APIRouter()


@router.get(path="/health", response_model=Result[HealthResponse])
async def health() -> Result[HealthResponse]:
    return Result.new(
        data=HealthResponse(status="ok", datetime=datetime.now(UTC)),
    )
