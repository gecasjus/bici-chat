from fastapi.encoders import jsonable_encoder
from fastapi import Depends, HTTPException
from api.exceptions.db_exception import database_error
from models.chat.chat import Chat
from models.item.item import Item
from models.chat.chat_create import ChatCreate
from models.message.message import Message
from repositories.base import BaseRepository
from services.auth_service import auth_service
from sqlalchemy.orm import Session
from dependencies.db import get_db
from resources.response import NOT_FOUND

class ChatRepository(BaseRepository[Chat, ChatCreate]):
    def __init__(self):
        self.model = Chat

    @database_error
    def save_message(self, id: str, payload: Message, db: Session):

        chat = self.get(id, db)

        if not chat:
            raise HTTPException(status_code=404, detail=NOT_FOUND)

        messages = jsonable_encoder(chat).get('messages')
        
        messages.append(payload.dict(exclude_unset=True))

        setattr(chat, 'messages', messages)

        db.add(chat)
        db.commit()
        db.refresh(chat)

        return chat


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