from urllib import response
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
def append_message(
    message: MessageCreate,
    id: str,
    chat_repo: ChatRepository = Depends(ChatRepository),
    db: Session = Depends(get_db)
    ):

    response = chat_repo.append_message(id, message.content, db)
    
    return response
