#!/usr/bin/env python3
"""_summary_
"""
import requests
import redis
from typing import Callable
from functools import wraps


db = redis.Redis()


def count_url(method: Callable):
    """_summary_

    Args:
        method (Callable): _description_

    Returns:
        _type_: _description_
    """
    @wraps(method)
    def counter(arg):
        cached_url = f"cached:{arg}"
        data = db.get(cached_url)

        if data:
            return data.decode("utf-8")

        count_key = f"count:{arg}"
        res = method(arg)

        db.incr(count_key)
        db.set(cached_url, res)
        db.expire(cached_url, 10)
        return res

    return counter


@count_url
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
