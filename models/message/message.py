import dataclasses
from datetime import datetime

@dataclasses.dataclass
class Message:
    content: str
    sender_id: str
    created_at: str = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def toDict(self):
        return dataclasses.asdict(self)