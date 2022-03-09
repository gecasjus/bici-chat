from repositories.base import BaseRepository
from models.tables import Item

class ItemRepository(BaseRepository[Item, Item]):
    def __init__(self):
        self.model = Item
