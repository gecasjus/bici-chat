import json
from fastapi import Depends
from models.domain import Chat, Item
from models.schemas.chat import Chat as ChatSchema
from models.schemas.chat import ChatCreate
from models.schemas.message import MessageCreate
from repositories.base import BaseRepository
from services.auth import auth_service
from sqlalchemy.orm import Session
from dependencies.db import get_db

class ChatRepository(BaseRepository[Chat, ChatCreate]):
    def __init__(self):
        self.model = Chat

    def add_content(self, payload: MessageCreate, db_obj: ChatSchema, db: Session):
        content = db_obj.dict(exclude_unset=True).get('messages')
        content_list = json.loads(content)
        new_content = content_list.append(payload)

        setattr(db_obj, 'messages', json.dumps(new_content))

        db.add(db_obj)
        db.commit()
        db.refresh()

        return db_obj


    def get_by_role(
        self, 
        item: Item,
        db: Session = Depends(get_db)
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