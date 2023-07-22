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


def get_top_ips(mongo_collection, limit: int = 10):
    """_summary_

    Args:
        mongo_collection (_type_): _description_
        limit (int, optional): _description_. Defaults to 10.

    Returns:
        _type_: _description_
    """
    grouped_ips = list(mongo_collection.aggregate([
        {
            "$group": {
                "_id": "$ip",
                "total": {"$sum": 1}
            }
        },
        {"$sort": {"total": -1}},
        {"$limit": limit},
        {
            "$project": {
                "_id": 0,
                "ip": "$_id",
                "total": 1
            }
        }
    ]))

    return grouped_ips


if __name__ == "__main__":
    methods_count(ngix_collection)
    top_10_ips = get_top_ips(ngix_collection)

    print(f"{doc_len} logs")

    print("Methods:")
    for k, v in methods.items():
        print(f"\tmethod {k}: {v}")

    print(f"{status_check_len} status check")

    print("IPs:")
    for ip in top_10_ips:
        print(f"\t{ip['ip']}: {ip['total']}")
