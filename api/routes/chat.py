from fastapi import status, APIRouter, Depends
from models.chat.chat import Chat
from sqlalchemy.orm import Session
from models.message.message_create import MessageCreate
from repositories.chat import ChatRepository
from repositories.item import ItemRepository
from dependencies.db import get_db

router = APIRouter()

@router.get("/{id}", name="chats:retrieve-chats")
def retrieve_chats(
    id, 
    item_repo: ItemRepository = Depends(ItemRepository),
    chats_repo: ChatRepository = Depends(ChatRepository), 
    db: Session = Depends(get_db),
):
    item = item_repo.get(id, db)

    response = chats_repo.get(item, db)

    return response

@router.post("/{id}/create", status_code=status.HTTP_201_CREATED)
def create_chat(
    message: MessageCreate, 
    id: str, 
    chats_repo: ChatRepository = Depends(ChatRepository),
    db: Session = Depends(get_db) 
    ) -> Chat:
    response = chats_repo.save(id, message, db)

    return response



