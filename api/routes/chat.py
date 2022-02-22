from datetime import datetime
import json

from fastapi.encoders import jsonable_encoder
from fastapi import status, APIRouter, Depends, HTTPException
from models.schemas.chat import ChatCreate, Chat
from models.schemas.message import Message
from sqlalchemy.orm import Session
from repositories.chat import ChatRepository
from repositories.item import ItemRepository
from dependencies.db import get_db
from services.auth import auth_service
from resources.response import CHAT_EXISTS

router = APIRouter()

# item and chats join => into single query
@router.get("/{id}", name="chats:retrieve-chats")
def retrieve_chats(
    id, 
    item_repo: ItemRepository = Depends(ItemRepository),
    chats_repo: ChatRepository = Depends(ChatRepository), 
    db: Session = Depends(get_db),
):
    item = item_repo.get(id, db)

    chat_ids = chats_repo.get_by_role(item)

    # get chat messages => message_repo
    return

@router.post("/{id}/create", status_code=status.HTTP_201_CREATED)
def create_chat(
    chat: ChatCreate, 
    id: str, 
    chats_repo: ChatRepository = Depends(ChatRepository),
    db: Session = Depends(get_db) 
    ) -> Chat:

    chat_exists = chats_repo.check_existence(id, db)

    if chat_exists:
        raise HTTPException(status_code=404, detail=CHAT_EXISTS)

    message = Message(
        content = chat.content,
        sender_id = auth_service._authId,
        created_at=datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    )

    new_chat = Chat(
        initializer = auth_service._authId,
        item_id = id,
        messages = json.dumps([message.dict()]),
    )

    response = chats_repo.save(new_chat, db)

    return response



