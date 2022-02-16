from fastapi import status, APIRouter, Depends
from models.schemas.item import ItemCreate
from dependencies.db import get_db
from sqlalchemy.orm import Session
from repositories.item import ItemRepository 

router = APIRouter()

@router.post("/create", status_code=status.HTTP_201_CREATED)
def create_item(
    item: ItemCreate,
    item_repo: ItemRepository = Depends(ItemRepository),
    db: Session = Depends(get_db),
    ):
    new_item = item_repo.save(item, db)
    return new_item
  