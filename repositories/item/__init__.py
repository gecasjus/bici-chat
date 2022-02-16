from repositories.base import BaseRepository
from models.domain import Item
from models.schemas.item import ItemCreate

class ItemRepository(BaseRepository[Item, ItemCreate]):
    def __init__(self):
        self.model = Item
