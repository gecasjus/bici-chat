from fastapi import status, HTTPException, APIRouter, Depends
import models as models
from models.schemas.message import (MessageInResponse, Message, ListOfMessagesInResponse)
from models.schemas.chat import Chat
from models.schemas.item import Item
from models.schemas.user import User

router = APIRouter()


# update chat.message
@router.post("/message/{chat_id}/create", status_code=status.HTTP_201_CREATED)
def create_message(message: Message, chat_id: str):
    try:
       crud.insert(models.Message(**message.dict(), chat_id = chat_id))
    except Exception:
        raise HTTPException(status_code=404, detail="Cannot post message")

    return crud.get_messages(chat_id)

# first, check how to update an existing messages