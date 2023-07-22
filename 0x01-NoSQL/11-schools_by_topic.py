#!/usr/bin/env python3
"""
module for schools ny topic function
"""
from typing import List


def schools_by_topic(mongo_collection, topic: str) -> List:
    """
    find schools with a particular topic

    Args:
        mongo_collection (_type_): _description_
        topic (str): _description_

    Returns:
        List: _description_
    """
    res = mongo_collection.find({"topics": topic})

    return list(res)
