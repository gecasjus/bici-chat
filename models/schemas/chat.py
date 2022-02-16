from typing import Optional
from pydantic import BaseModel, Json

class ChatCreate(BaseModel):
    initializer: str

class Chat(BaseModel):
    initializer: str
    item_id: str
    messages: Optional[Json]