import pymongo

connection = pymongo.MongoClient("localhost", 27017)
data_base = connection["my_db"]
collection = data_base["user_info"]

# print(collection.find())
for i in collection.find({}, {"_id": 0, "name": 1}):
    print(i["name"])