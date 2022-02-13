import models as models
from fastapi import status, HTTPException, APIRouter, Depends
from models.schemas.message import ListOfMessagesInResponse
from models.schemas.chat import Chat
from repositories.chat import ChatRepository
from repositories.item import ItemRepository
from services.auth import auth_service

router = APIRouter()

@router.get("/{id}", response_model=ListOfMessagesInResponse, name="chats:retrieve-chats")
def retrieve_chats(id, item_repo: ItemRepository = Depends(ItemRepository), chat_repo: ChatRepository = Depends(ChatRepository)):
    # pass item
    print(auth_service._authId)

    # chat_ids = chat_repo.get_chats_by_role(item_repo.get_item_by_id(id))

    # get chat messages => message_repo
    return


@router.post("/{id}/create", status_code=status.HTTP_201_CREATED)
def create_chat(chat: Chat, id: str):
    try:
       crud.insert(models.Chat(**chat.dict(), item_id = id))
    except Exception:
        raise HTTPException(status_code=404, detail="An error occured")

    return models.Chat(**chat.dict(), item_id = id).id



