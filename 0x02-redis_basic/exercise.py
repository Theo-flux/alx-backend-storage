#!/usr/bin/env python3
"""
exercise file
"""
from typing import Union
import redis
import uuid


class Cache():
    """
    cache class

    Returns:
        _type_: _description_
    """

    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)

        return key
