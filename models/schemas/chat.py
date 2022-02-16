from pydantic import BaseModel, Json

class ChatCreate(BaseModel):
    initializer: str
    item_id: str

class ChatUpdate(BaseModel):
    initializer: str
    item_id: str
    messages: Json