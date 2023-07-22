#!/usr/bin/env python3
"""
module for inserting new documents
into a collection
"""


def insert_school(mongo_collection, **kwargs) -> str:
    """
    inserts a new document in a collection based on kwargs

    Args:
        mongo_collection (_type_): _description_

    Returns:
        str: _description_
    """
    res = mongo_collection.insert_one(kwargs)
    return res.inserted_id
