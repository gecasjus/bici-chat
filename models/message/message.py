from pydantic import BaseModel

class Message(BaseModel):
    content: str
    sender_id: str
    created_at: str
