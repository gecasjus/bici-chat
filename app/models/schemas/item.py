from pydantic import BaseModel

class Item(BaseModel):
    id: str
    admin_id: str