from fastapi import Depends, status, APIRouter
from models.message.message import Message
from models.message.message_create import MessageCreate
from datetime import datetime
from services.auth_service import auth_service
from sqlalchemy.orm import Session
from repositories.chat import ChatRepository
from dependencies.db import get_db

router = APIRouter()
 
@router.put("/{id}/create", status_code=status.HTTP_201_CREATED)
def create_message(
    message: MessageCreate,
    id: str,
    chat_repo: ChatRepository = Depends(ChatRepository),
    db: Session = Depends(get_db)
    ):

    updated_chat = chat_repo.save_message(
        id,
        Message(
        content=message.content,
        sender_id=auth_service._authId, 
        created_at=datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        ),
        db
        )
    
    return updated_chat
