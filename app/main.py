import logging

from fastapi import FastAPI
from fastapi.concurrency import asynccontextmanager
from fastapi.exceptions import RequestValidationError
from fastapi.staticfiles import StaticFiles

from app.interface import v1
from app.interface.system import sys_api
from app.shared.errors import BaseError
from app.shared.handlers import base_error_handler, validation_error_handler

logging.basicConfig(
    level=logging.INFO,
    format="[%(name)s] %(asctime)s.%(msecs)03d [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(_: FastAPI):
    logger.info("Start server")
    yield
    logger.info("Stop server")


app = FastAPI(
    lifespan=lifespan,
    exception_handlers={
        BaseError: base_error_handler,
        RequestValidationError: validation_error_handler,
    },
)

app.mount(
    path="/static",
    app=StaticFiles(directory="static"),
    name="static",
)


app.include_router(router=sys_api.router, prefix="/api/system", tags=["System"])
v1.mount(app)
