from fastapi import status, APIRouter
from models.schemas.message import MessageCreate, Message
from datetime import datetime
from services.auth import auth_service

router = APIRouter()

@router.put("/{id}/create", status_code=status.HTTP_201_CREATED)
def create_message(message: MessageCreate, id: str):
    new_message = Message(
        content=message.content,
        sender_id=auth_service._authId, 
        chat_id=id,
        created_at=datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        )

    # try:
    #    crud.insert(models.Message(**message.dict(), chat_id = chat_id))
    # except Exception:
    #     raise HTTPException(status_code=404, detail="Cannot post message")

    # return crud.get_messages(chat_id)
    return {**new_message.dict()}

# first, check how to update an existing messages