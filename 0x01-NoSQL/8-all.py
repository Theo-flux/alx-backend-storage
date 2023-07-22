#!/usr/env python3
"""
list all function module
"""
import pymongo
from typing import List


def list_all(mongo_collection) -> List:
    """
    lists all documents in a collection

    Args:
        mongo_collection (_type_): _description_

    Returns:
        List: _description_
    """
    return list(mongo_collection.find())
