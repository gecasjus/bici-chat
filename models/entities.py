from sqlalchemy.sql.expression import text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, TIMESTAMP, ForeignKey
import uuid

class Message(declarative_base()):
    __tablename__ = 'message'
    id = Column(String, primary_key=True, default=str(uuid.uuid4()))
    sender_id = Column(String, nullable=False)
    chat_id = Column(String, ForeignKey('chat.id', ondelete="CASCADE"), nullable=False)
    content = Column(String,  nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False, server_default=text('now()'))

class Chat(declarative_base()):
    __tablename__ = 'chat'
    id = Column(String, primary_key=True, default=str(uuid.uuid4()))
    initializer = Column(String, nullable=False)
    item_id = Column(String, ForeignKey('item.id', ondelete="CASCADE"), nullable=False)

class Item(declarative_base()):
    __tablename__ = 'item'
    id = Column(String ,nullable=False, primary_key=True)
    admin_id = Column(String, nullable=False)