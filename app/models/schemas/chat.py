from pydantic import BaseModel

class Chat(BaseModel):
    initializer: str
    item_id: str