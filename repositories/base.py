from typing import  Type, TypeVar, Generic

from pydantic import BaseModel
from core.database import Base
from sqlalchemy.orm import Session

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)

class BaseRepository(Generic[ModelType, CreateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    def get(self, id: str, db: Session,):
        return db.query(self.model).filter(self.model.id == id).first()

    def save(self, payload: CreateSchemaType, db: Session) -> ModelType:
        db_obj = self.model(**payload.dict())
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        
        return db_obj

    def remove(self, db: Session, *, id: str) -> ModelType:
        obj = db.query(self.model).get(id)
        db.delete(obj)
        db.commit()
        return obj