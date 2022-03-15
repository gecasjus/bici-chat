from fastapi import status, APIRouter, Depends
from models.item.item import Item
from dependencies.db import get_db
from sqlalchemy.orm import Session
from repositories.item import ItemRepository
from services.auth_service import auth_service

router = APIRouter()

@router.post("/create/{id}", status_code=status.HTTP_201_CREATED)
def create_item(
    id: str,
    item_repo: ItemRepository = Depends(ItemRepository),
    db: Session = Depends(get_db),
    ):
 
    new_item = item_repo.save(
        Item(
        id = id,
        admin_id = auth_service._authId
        ), 
        db)

    return new_item
  