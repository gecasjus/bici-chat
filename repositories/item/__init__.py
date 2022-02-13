from repositories.base import BaseRepository
from models import Item
from models.schemas.item import ItemCreate

class ItemRepository(BaseRepository[Item, ItemCreate]):
    def __init__(self):
        pass

item = ItemRepository(Item)