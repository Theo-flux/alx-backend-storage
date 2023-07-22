#!/usr/bin/env python3
"""
_summary_
"""
from typing import List


def update_topics(mongo_collection, name: str, topics: List[str]) -> None:
    mongo_collection.update_many({'name': name}, {'$set': {'topics': topics}})
