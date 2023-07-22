#!/usr/bin/env python3
"""
_summary_
"""
from typing import List


def top_students(mongo_collection) -> List:
    res = list(mongo_collection.aggregate([
        {
            "$addFields": {
                "averageScore": {
                    "$avg":  "$topics.score"
                }
            }
        },
        {
            "$sort": {
                "averageScore": -1
            }
        },
        {
            "$project": {
                "_id": 1,
                "name": 1,
                "averageScore": 1
            }
        }
    ]))

    return res
