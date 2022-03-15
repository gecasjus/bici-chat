from pydantic import BaseModel

class ChatCreate(BaseModel):
    content: str