from repositories.base import BaseRepository
from models.item.item import Item
from services.auth_service import auth_service

class ItemRepository(BaseRepository[Item]):
    def __init__(self):
        self.model = Item

    def save(self, id, db):
       return super().save(Item(
        id = id,
        admin_id = auth_service.authId
        ), db)


