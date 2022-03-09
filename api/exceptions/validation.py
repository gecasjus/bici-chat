from typing import Callable
from starlette.responses import JSONResponse
from starlette.requests import Request
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi import HTTPException
from sqlalchemy import exc

def validation_exception_handler(_: Request, exc: RequestValidationError) -> Callable:
    return JSONResponse(
        status_code=HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
    )

def database_error(func):
    def handler(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except exc.SQLAlchemyError as err:
            raise HTTPException(status_code=500, detail=str(err.__dict__['orig']))

    return handler