from fastapi import FastAPI
from api import router
import uvicorn
from starlette_context import plugins
from starlette.middleware.cors import CORSMiddleware
from starlette_context.middleware import ContextMiddleware
from api.exceptions.validation import validation_exception_handler
from fastapi.exceptions import RequestValidationError
from core.database import init_db

def init() -> FastAPI:
    application = FastAPI()

    application.add_middleware(ContextMiddleware,
        plugins=(
            plugins.RequestIdPlugin(),
            plugins.CorrelationIdPlugin()
        ))

    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.include_router(router)

    application.add_exception_handler(RequestValidationError, validation_exception_handler)

    init_db()

    return application

app = init()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)