import random

import pymongo

connection = pymongo.MongoClient("localhost", 27017)
data_base = connection["test_db"]
collection = data_base["test_info"]


if __name__ == "__main__":
    for i in range(10):
        user_id = random.randint(0, 1000000)
        build = {"_id": user_id, "name": "kai" + str(i), "email": "zwe" + str(i) + "@gmail.com", "password": 11111,
                 "points": 0}
        collection.insert_one(build)
        