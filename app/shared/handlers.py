import logging

from fastapi import Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.shared.errors import BaseError

logger = logging.getLogger(__name__)


async def base_error_handler(_: Request, exc: BaseError):
    return JSONResponse(
        status_code=exc.status_code,
        content={"code": exc.status_code, "message": str(exc)},
    )


async def validation_error_handler(_: Request, exc: RequestValidationError):
    message = ", ".join(
        [str({key: e.get(key) for key in e if key != "url"}) for e in exc.errors()]
    )

    logger.warning(message)

    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"code": status.HTTP_422_UNPROCESSABLE_ENTITY, "message": message},
    )
