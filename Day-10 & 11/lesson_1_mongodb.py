import random

import pymongo

connection = pymongo.MongoClient("localhost", 27017)
data_base = connection["my_db"]
# collection = data_base["user_info"]  # for user
collection = data_base["candidate_info"]  # for candidate

# data: dict = {
#     "1": {"name": "Kai1", "email": "kai123@gmail.com"},
#     "2": {"name": "Kai2", "email": "kai123@gmail.com"},
#     "3": {"name": "Kai3", "email": "kai123@gmail.com"},
#     "4": {"name": "Kai4", "email": "kai123@gmail.com"},
#     "5": {"name": "Kai5", "email": "kai123@gmail.com"},
# }

# add_data = collection.insert_one(data)
# print("id:", add_data.inserted_id)

# ***** for user by input *****
# if __name__ == '__main__':
#     while True:
#         try:
#             user_name: str = input("Enter your name:> ")
#             user_email: str = input("Enter your email:> ")
#             password: str = input("Enter your password:> ")
#             user_id = random.randint(0, 1000000)
#
#             build = {"_id": user_id, "name": user_name, "email": user_email, "password": password}
#             collection.insert_one(build)
#             break
#         except Exception as err:
#             print(err)

# ***** for user ******
# if __name__ == '__main__':
#     for i in range(10):
#         user_id = random.randint(0, 1000000)
#         build = {"_id": user_id, "name": "zwe" + str(i), "email": "zwe" + str(i) + "@gmail.com", "password": 11111,
#                  "points": 0}
#         collection.insert_one(build)

# ****** for candidate *****
if __name__ == '__main__':
    while True:
        user_name: str = input("Enter cdt name:> ")
        cdt_age: str = input("Enter cdt age:> ")
        cdt_job: str = input("Enter cdt job:> ")
        cdt_height: str = input("Enter cdt height:> ")
        user_id = random.randint(0, 1000000)

        build = {"_id": user_id, "name": user_name, "age": cdt_age, "job_role": cdt_job, "height": cdt_height, "own_points": 0}
        collection.insert_one(build)
