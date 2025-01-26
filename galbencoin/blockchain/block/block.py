from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Block(BaseModel):
    id: int
    timestamp: Optional[datetime]
    previous_hash: Optional[str]
    hash: Optional[str]
    merkle_root: Optional[str]
    def __init__(self, **data):
        super().__init__(**data)
"""
data = {
    "id": 123,
    "timestamp": datetime.now(),
    "previous_hash": None,
    "hash": None,
    "merkle_root": None
}

block = Block(**data)
"""