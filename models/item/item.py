from sqlalchemy import Column, String
from dataclasses import dataclass
from dataclasses import field
from core.database import mapper_registry

@mapper_registry.mapped
@dataclass
class Item:
    __tablename__ = "item"
    __sa_dataclass_metadata_key__ = "sa"

    id: str = field(metadata={"sa": Column('id', String, primary_key=True, nullable=False)})
    admin_id: str = field(metadata={"sa": Column('admin_id', String, nullable=False)})



