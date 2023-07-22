#!/usr/bin/env python3
"""
update_topics function
"""
from typing import List


def update_topics(mongo_collection, name: str, topics: List[str]) -> None:
    """
    changes all topics of a school document based on the nam

    Args:
        mongo_collection (pymongo object): mongodb collection
        name (str): name of school to update
        topics (List[str]): list of topics approcahed in school
    """
    mongo_collection.update_many({'name': name}, {'$set': {'topics': topics}})
