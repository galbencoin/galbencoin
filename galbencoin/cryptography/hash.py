import hashlib

HASH_ALGO = "sha512"

ENCODING = "utf-8"

def string(input_string: str, encoding:str=ENCODING):
    hasher = hashlib.new(HASH_ALGO)
    hasher.update(input_string.encode(encoding))
    return hasher.hexdigest()