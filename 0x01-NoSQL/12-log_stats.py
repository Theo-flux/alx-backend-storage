#!/usr/bin/env python3
"""
module for accessing nginx database
"""
from pymongo import MongoClient


client: MongoClient = MongoClient()
logsDB = client['logs']
ngix_collection = logsDB.nginx

doc_len = len(list(ngix_collection.find()))
status_check_len = len(list(ngix_collection.find({
    "method": "GET", "path": '/status'
})))
methods = {"GET": 0, "POST": 0, "PUT": 0, "PATCH": 0, "DELETE": 0}


def methods_count(mongo_collection) -> None:
    """
    updates the total count for every methods in the dictionary

    Args:
        mongo_collection (_type_): _description_
    """

    for key in methods.keys():
        methods[key] = len(list(mongo_collection.find({"method": key})))


if __name__ == "__main__":
    methods_count(ngix_collection)
    print(doc_len)
    print("Methods:")
    for k, v in methods.items():
        print(f"\tmethod {k}: {v}")
    print(f"{status_check_len} status check")
