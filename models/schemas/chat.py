from pydantic import BaseModel, Json

class ChatCreate(BaseModel):
    content: str

class Chat(BaseModel):
    initializer: str
    item_id: str
    messages: Json