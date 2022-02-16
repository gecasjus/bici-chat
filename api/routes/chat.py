from fastapi import status, APIRouter, Depends
from models.schemas.message import ListOfMessagesInResponse
from models.schemas.chat import ChatCreate
from sqlalchemy.orm import Session
from repositories.chat import ChatRepository
from repositories.item import ItemRepository
from dependencies.db import get_db

router = APIRouter()

@router.get("/{id}", response_model=ListOfMessagesInResponse, name="chats:retrieve-chats")
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
def create_chat(chat: ChatCreate, id: str):
    pass



