from datetime import datetime
from fastapi import Depends, HTTPException
from api.exceptions.db_exception import database_error
from models.chat.chat import Chat
from models.item.item import Item
from models.message.message_create import MessageCreate
from models.message.message import Message
from repositories.base import BaseRepository
from services.auth_service import auth_service
from sqlalchemy.orm import Session
from dependencies.db import get_db
from resources.response import CHAT_EXISTS, NOT_FOUND
from services.auth_service import auth_service

class ChatRepository(BaseRepository[Chat]):
    def __init__(self):
        self.model = Chat

    def save(self, id, message_create, db):
        chat_exists = self.check_existence(id, db)

        if chat_exists:
            raise HTTPException(status_code=404, detail=CHAT_EXISTS)

        return super().save(
            Chat(
                initializer = auth_service._authId,
                item_id = id,
                messages = [Message(message_create, auth_service._authId)._toDict()]),
            db)

    @database_error
    def append_message(self, id: str, message_create: MessageCreate, db: Session):
        chat = self.get(id, db)

        if not chat:
            raise HTTPException(status_code=404, detail=NOT_FOUND)

        chat.messages.append(Message(message_create, auth_service._authId)._toDict())

        return super().save(chat, db)


    def get_by_role(
        self, 
        item: Item,
        db: Session
        ):
        if item.admin_id == auth_service._authId:
            return db.query(self.model).filter(self.model.item_id == item.id).all()
        else:     
            return db.query(self.model).filter(self.model.initializer == auth_service._authId).first()

    
    def check_existence(self, id: str, db: Session = Depends(get_db)):
        chat = db.query(self.model).filter(self.model.item_id == id, self.model.initializer == auth_service._authId).first()
        
        if chat:
            return True

        return False