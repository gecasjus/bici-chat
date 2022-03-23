from fastapi import status, APIRouter, Depends
from dependencies.db import get_db
from sqlalchemy.orm import Session
from repositories.item import ItemRepository

router = APIRouter()

@router.post("/create/{id}", status_code=status.HTTP_201_CREATED)
def create_item(
    id: str,
    item_repo: ItemRepository = Depends(ItemRepository),
    db: Session = Depends(get_db),
    ):
 
    response = item_repo.save(id, db)

    return response
  