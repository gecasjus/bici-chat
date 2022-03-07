from sqlalchemy import Column, String
from core.database import Base

class Item(Base):
    __tablename__ = 'item'
    id = Column(String ,nullable=False, primary_key=True)
    admin_id = Column(String, nullable=False)

