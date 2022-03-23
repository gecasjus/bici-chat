import dataclasses
from datetime import datetime
from services.auth_service import auth_service

@dataclasses.dataclass
class Message:
    content: str
    sender_id: str
    created_at: str = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def _toDict(self):
        return dataclasses.asdict(self)