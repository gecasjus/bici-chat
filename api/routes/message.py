from fastapi import Depends, status, APIRouter, HTTPException
from models.schemas.message import MessageCreate, Message
from datetime import datetime
from services.auth import auth_service
from sqlalchemy.orm import Session
from repositories.chat import ChatRepository
from dependencies.db import get_db
from resources.response import NOT_FOUND

router = APIRouter()

@router.put("/{id}/create", status_code=status.HTTP_201_CREATED)
def create_message(
    message: MessageCreate,
    id: str,
    chat_repo: ChatRepository = Depends(ChatRepository),
    db: Session = Depends(get_db)
    ):
    
    new_message = Message(
        content=message.content,
        sender_id=auth_service._authId, 
        created_at=datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        )
    
    chat = chat_repo.get(id)

    if not chat:
       raise HTTPException(status_code=404, detail=NOT_FOUND)

    updated_chat = chat_repo.add_content(new_message, chat, db)
    
    return updated_chat
