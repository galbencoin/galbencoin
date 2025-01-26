from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Block(BaseModel):
    id: int
    timestamp: Optional[datetime]
    previous_hash: Optional[str]
    hash: Optional[str]
    merkle_root: Optional[str]