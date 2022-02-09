from typing import List, Optional
from pydantic import BaseModel

class Message(BaseModel):
    content: str
    sender_id: str

class MessageInResponse(Message):
    created_at: str

class ListOfMessagesInResponse(BaseModel):
    messages: Optional[List[MessageInResponse]]