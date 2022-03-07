from pydantic import BaseModel

class ItemCreate(BaseModel):
    id: str

class Item(BaseModel):
    id: str
    admin_id: str