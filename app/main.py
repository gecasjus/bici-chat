import models
from fastapi import FastAPI
from app.database.database import engine
from app.api.api import router as api_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(api_router)