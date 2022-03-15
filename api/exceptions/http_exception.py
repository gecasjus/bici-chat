from typing import Callable
from starlette.responses import JSONResponse
from starlette.requests import Request
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError

def http_error_handler(_: Request, exc: RequestValidationError) -> Callable:
    return JSONResponse(
        status_code=exc.status_code,
        content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
    )