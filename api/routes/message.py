from urllib import response
from fastapi import Depends, status, APIRouter
from models.message.message_create import MessageCreate
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

    response = chat_repo.append_message(id, message, db)
    
    return response
