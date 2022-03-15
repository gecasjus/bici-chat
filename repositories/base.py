from typing import  Type, TypeVar, Generic
from api.exceptions.db_exception import database_error
from sqlalchemy.orm import Session

ModelType = TypeVar("ModelType")
CreateSchemaType = TypeVar("CreateSchemaType")
UpdateSchemaType = TypeVar("UpdateSchemaType")

class BaseRepository(Generic[ModelType, CreateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    def get(self, id: str, db: Session,):
        return db.query(self.model).filter(self.model.id == id).first()
    
    def get(self, id: str, db: Session,):
        return db.query(self.model).filter(self.model.id == id).first()

    @database_error
    def save(self, payload: CreateSchemaType, db: Session) -> ModelType:
        db.add(payload)
        db.commit()
        db.refresh(payload)
        
        return payload

    def remove(self, id: str, db: Session) -> ModelType:
        obj = db.query(self.model).get(id)
        db.delete(obj)
        db.commit()
        return obj