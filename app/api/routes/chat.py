from fastapi import status, HTTPException, APIRouter, Depends
import app.models.tables as models
from app.models.schemas.message import (MessageInResponse, Message, ListOfMessagesInResponse)
from app.models.schemas.chat import Chat
from app.models.schemas.item import Item
from app.models.schemas.user import User
import app.crud.crud as crud

router = APIRouter()


@router.get("/item/{itemId}", response_model=ListOfMessagesInResponse)
def retrieve_chat_content_by_user(chat: Chat = Depends(), user: User):

#    return comments = await comments_repo.get_comments_for_article(article=article, user=user)
    # return ListOfCommentsInResponse(comments=comments)

#    if not messages:
#        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Message not found")

   return messages

# get_chat => brings back id, if not id => POST

# update chat.message
@router.post("/message/{chat_id}/create", status_code=status.HTTP_201_CREATED)
def create_message(message: message.Message, chat_id: str):
    try:
       crud.insert(models.Message(**message.dict(), chat_id = chat_id))
    except Exception:
        raise HTTPException(status_code=404, detail="Cannot post message")

    return crud.get_messages(chat_id)

# first, check how to update an existing messages
@router.post("/chat/{id}/create", status_code=status.HTTP_201_CREATED)
def create_chat(chat: chat.Chat, id: str):
    try:
       crud.insert(models.Chat(**chat.dict(), item_id = id))
    except Exception:
        raise HTTPException(status_code=404, detail="An error occured")

    return models.Chat(**chat.dict(), item_id = id).id

@router.post("/item/create", status_code=status.HTTP_201_CREATED)
def create_item(item: chat_schemas.Item):
    try:
       crud.insert(models.Item(**item.dict()))
    except:
        raise HTTPException(status_code=404, detail="Cannot create an item")

    return "Item content created"


