from sqlalchemy import Column, String, ForeignKey
from core.database import Base
from sqlalchemy_json import mutable_json_type
from sqlalchemy.dialects.postgresql import JSONB
import uuid

class Chat(Base):
    __tablename__ = 'chat'
    id = Column(String, primary_key=True, default=str(uuid.uuid4()))
    initializer = Column(String, nullable=False)
    item_id = Column(String, ForeignKey('item.id', ondelete="CASCADE"), nullable=False)
    messages = Column(mutable_json_type(dbtype=JSONB, nested=True), nullable=True)

