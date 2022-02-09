from repositories.base import BaseRepository

class ItemRepository(BaseRepository):
   
    def get_item_by_id(self, id):
        print('called item repo', self.id)
        return 'dasdas'
