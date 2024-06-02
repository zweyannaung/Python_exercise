import pymongo

connection = pymongo.MongoClient('localhost', 27017)
data_base = connection["test_db"]
collection = data_base["test_info"]

for i in collection.find():
    collection.update_one({"name": "kai1"}, {"$set": {"points": 10}})
