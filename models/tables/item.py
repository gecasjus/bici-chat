from sqlalchemy import Column, String
from models.tables.base import Base

class Item(Base):
    id = Column(String, nullable=False, primary_key=True)
    admin_id = Column(String, nullable=False)

