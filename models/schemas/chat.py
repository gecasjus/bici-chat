from pydantic import BaseModel

class ChatCreate(BaseModel):
    initializer: str
    item_id: str