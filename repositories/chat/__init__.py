from models import Chat
from models.schemas.chat import ChatCreate
from repositories.base import BaseRepository


class ChatRepository(BaseRepository[Chat, ChatCreate]):

    def get_chats_by_role(self):     
        return

chats = ChatRepository(Chat)
        