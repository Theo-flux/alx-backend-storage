#!/usr/bin/env python3
"""
exercise file
"""
from typing import Union, Optional, Callable
import redis
import uuid
from functools import wraps


def count_calls(method: Callable) -> Callable:

    @wraps(method)
    def counter(*args, **kwds):
        db = args[0]
        qual_name = method.__qualname__

        if db._redis.get(qual_name):
            db._redis.incr(qual_name, 1)
        else:
            db._redis.set(qual_name, 1)
    
        return method(*args, **kwds)
    return counter


class Cache():
    """
    cache class

    Returns:
        _type_: _description_
    """

    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)

        return key

    def get(self, key: str, fn: Optional[Callable] = None):
        val = self._redis.get(key)
        if fn:
            return fn(val)
        return val

    def get_str(self, key: str):
        return self.get(key, fn=lambda d: d.decode("utf-8") if d else None)

    def get_int(self, key: str):
        return self.get(key, fn=lambda d: int(d) if d else None)
        

if __name__ == '__main__':
    cache = Cache()

    TEST_CASES = {
        b"foo": None,
        123: int,
        "bar": lambda d: d.decode("utf-8")
    }

    for value, fn in TEST_CASES.items():
        key = cache.store(value)
        assert cache.get(key, fn=fn) == value

    
        
