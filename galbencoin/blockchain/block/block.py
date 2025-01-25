from enum import Enum
from builtins import type as typeof

class BlockType(Enum):
    BIGBANG = 0
    TRANSACTION = 1

class Block:
    id: int
    type: BlockType
    def __init__(self, id: int, type: BlockType):
        if not isinstance(id, int):
            raise TypeError(f"Expected 'id' to be 'int', got {typeof(id).__name__}")
        if not isinstance(type, BlockType):
            raise TypeError(f"Expected 'type' to be 'BlockType', got {typeof(type).__name__}")
        
        self.id = id
        self.type = type