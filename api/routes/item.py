from fastapi import status, HTTPException, APIRouter
import models as models
from models.schemas.chat import Chat
from models.schemas.item import Item

router = APIRouter()

@router.post("/item/create", status_code=status.HTTP_201_CREATED)
def create_item(item: Item):
  