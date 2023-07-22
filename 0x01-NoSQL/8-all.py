#!/usr/env python3
"""
list all function
"""
from typing import List


def list_all(mongo_collection) -> List:
    """_summary_

    Args:
        mongo_collection (_type_): _description_

    Returns:
        List: _description_
    """
    return list(mongo_collection.find())
