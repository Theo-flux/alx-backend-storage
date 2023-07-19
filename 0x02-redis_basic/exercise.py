#!/usr/bin/env python3
"""
exercise file
"""
from typing import Union, Optional, Callable, Awaitable, Any
import redis
import uuid
from functools import wraps


def count_calls(method: Callable) -> Callable:

    @wraps(method)
    def counter(self, *args):
        qual_name = method.__qualname__

        if self._redis.get(qual_name):
            self._redis.incr(qual_name, 1)
        else:
            self._redis.set(qual_name, 1)

        return method(self, *args)

    return counter


def call_history(method: Callable) -> Callable:

    @wraps(method)
    def call(self, *args):
        qual_name = method.__qualname__

        self._redis.rpush(f"{qual_name}:inputs",  str(args))

        res = method(self, *args)
        self._redis.rpush(f"{qual_name}:outputs", res)

        return res

    return call


def replay(method: Callable):
    db = redis.Redis()
    fun_name = method.__qualname__

    if db.get(f"{fun_name}"):
        count = int(db.get(f"{fun_name}").decode('utf-8'))
        inputs = db.lrange(f"{fun_name}:inputs", 0, -1)
        outputs = db.lrange(f"{fun_name}:outputs", 0, -1)

        zipped_res = list(zip((inputs), outputs))

        print(f"{fun_name} was called {count} times:")
        for i in range(len(zipped_res)):
            left = zipped_res[i][0].decode('utf-8')
            right = zipped_res[i][1].decode('utf-8')

            print(f"{fun_name}(*{left}) -> {right}")


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
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)

        return key

    def get(
        self,
        key: str,
        fn: Optional[Callable] = None
    ) -> Union[Awaitable, Any]:
        val = self._redis.get(key)
        if fn:
            return fn(val)
        return val

    def get_str(self, key: str) -> Union[Awaitable, str]:
        return self.get(key, fn=lambda d: d.decode("utf-8") if d else None)

    def get_int(self, key: str) -> Union[Awaitable, int]:
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

    cache = Cache()
    cache.store("foo")
    cache.store("bar")
    cache.store(42)
    replay(cache.store)
