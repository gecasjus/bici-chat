from sqlalchemy.sql.expression import text
from sqlalchemy import Column, String, TIMESTAMP, ForeignKey
from models.base_model import Base
import uuid

class Message(Base):
    id = Column(String, primary_key=True, default=str(uuid.uuid4()))
    sender_id = Column(String, nullable=False)
    chat_id = Column(String, ForeignKey('chat.id', ondelete="CASCADE"), nullable=False)
    content = Column(String,  nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False, server_default=text('now()'))

class Chat(Base):
    id = Column(String, primary_key=True, default=str(uuid.uuid4()))
    initializer = Column(String, nullable=False)
    item_id = Column(String, ForeignKey('item.id', ondelete="CASCADE"), nullable=False)

class Item(Base):
    id = Column(String ,nullable=False, primary_key=True)
    admin_id = Column(String, nullable=False)