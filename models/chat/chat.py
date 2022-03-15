from sqlalchemy import Column, String, ForeignKey
from sqlalchemy_json import mutable_json_type
from sqlalchemy.dialects.postgresql import JSONB
import uuid
from pydantic import Json
from sqlalchemy import Column, String
from dataclasses import dataclass
from dataclasses import field
from core.database import mapper_registry

@mapper_registry.mapped
@dataclass
class Chat:
    __tablename__ = "chat"
    __sa_dataclass_metadata_key__ = "sa"

    item_id: str = field(metadata={"sa": Column('item_id', String, ForeignKey('item.id', ondelete="CASCADE"), nullable=False)})
    initializer: str = field(metadata={"sa": Column('initializer', String, nullable=False)})
    messages: Json = field(metadata={"sa": Column('messages', mutable_json_type(dbtype=JSONB, nested=True), nullable=True)})
    id: str = field(default=str(uuid.uuid4()), metadata={"sa": Column('id', String, primary_key=True, nullable=False)})