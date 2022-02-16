from pydantic import BaseModel

class Message(BaseModel):
    content: str
    sender_id: str
    chat_id: str
    created_at: str

class MessageCreate(BaseModel):
    content: str