from fastapi import Depends
from models.domain import Chat, Item
from models.schemas.chat import ChatCreate
from repositories.base import BaseRepository
from services.auth import auth_service
from sqlalchemy.orm import Session
from dependencies.db import get_db

class ChatRepository(BaseRepository[Chat, ChatCreate]):
    def __init__(self):
        self.model = Chat

    def get_by_role(
        self, 
        item: Item,
        db: Session = Depends(get_db)
        ):
        if item.admin_id == auth_service._authId:
            return db.query(self.model).filter(self.model.item_id == item.id).all()
        else:     
            return db.query(self.model).filter(self.model.initializer == auth_service._authId).first()


    def save_chat(self, payload, id, db: Session):
        db_obj = self.model(**payload.dict(), item_id = id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
        