from fastapi import FastAPI
from api import router
import uvicorn
from services.context import context_service

app = FastAPI(middleware=context_service)

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)