from typing import Callable
from starlette.responses import JSONResponse
from starlette.requests import Request
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError

def validation_exception_handler(_: Request, exc: RequestValidationError) -> Callable:
    return JSONResponse(
        status_code=HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
    )
