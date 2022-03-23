from fastapi import status, APIRouter, Depends
from models.chat.chat import Chat
from models.chat.chat_create import ChatCreate
from sqlalchemy.orm import Session
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

    response = chats_repo.get_by_role(item, db)

    return response

@router.post("/{id}/create", status_code=status.HTTP_201_CREATED)
def create_chat(
    chat: ChatCreate, 
    id: str, 
    chats_repo: ChatRepository = Depends(ChatRepository),
    db: Session = Depends(get_db) 
    ) -> Chat:
    response = chats_repo.save(id, chat.content, db)

    return response



