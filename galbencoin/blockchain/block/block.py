from enum import Enum

class Block:
    id: int
    is_bigbang: bool
    def __init__(self, id: int, is_bigbang: bool):
        if not isinstance(id, int):
            raise TypeError(f"Expected 'id' to be 'int', got {type(id).__name__}")
        if not isinstance(is_bigbang, bool):
            raise TypeError(f"Expected 'is_bigbang' to be 'bool', got {type(is_bigbang).__name__}")
        
        self.id = id
        self.is_bigbang = is_bigbang