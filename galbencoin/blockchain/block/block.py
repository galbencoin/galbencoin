from enum import Enum

class Block:
    id: int
    hash: str
    is_bigbang: bool
    def __init__(self, id: int, hash:str=None, is_bigbang: bool = False):
        """
        None hash means it will be recalculated
        """
        if not isinstance(id, int):
            raise TypeError(f"Expected 'id' to be 'int', got {type(id).__name__}")
        if not isinstance(hash, str) or not isinstance(hash, None):
            raise TypeError(f"Expected 'hash' to be 'str' or 'None', got {type(hash).__name__}")
        if not isinstance(is_bigbang, bool):
            raise TypeError(f"Expected 'is_bigbang' to be 'bool', got {type(is_bigbang).__name__}")
        
        self.id = id
        self.hash = hash
        self.is_bigbang = is_bigbang