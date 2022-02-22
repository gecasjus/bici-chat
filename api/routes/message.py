from fastapi import Depends, status, APIRouter
from models.schemas.message import MessageCreate, Message
from datetime import datetime
from services.auth import auth_service
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
    new_message = Message(
        content=message.content,
        sender_id=auth_service._authId, 
        created_at=datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        )
    
    # get chat_id, 
    # encode message json or check mutable_json_type.append

    # decode again
    # update 


    return {**new_message.dict()}
