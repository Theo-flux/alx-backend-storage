#!/usr/bin/env python3
"""_summary_
"""
import requests
import redis
from typing import Callable
from functools import wraps


db = redis.Redis()


def count_url(method: Callable):
    @wraps(method)
    def counter(*args):
        count_key = f"count:{args}"
        method(*args)

        if (db.get(count_key)):
            db.incr(count_key)
        else:
            db.setex(count_key, 10, 1)

        # print(db.get(count_key))
        return db.get(count_key)

    return counter


def cache_url(method: Callable):
    @wraps(method)
    def counter(*args):
        cache_key = f"cache:{args}"
        cache = method(*args)

        if (db.get(cache_key)):
            db.set(cache_key, cache)
        else:
            db.set(cache_key, cache)

        # print(cache)
        return cache

    return counter


@count_url
@cache_url
def get_page(url: str) -> str:
    """_summary_

    Args:
        url (str): url

    Returns:
        str: _description_
    """
    res = requests.get(url)
    return res.text


if __name__ == "__main__":
    get_page('http://slowwly.robertomurray.co.uk')
