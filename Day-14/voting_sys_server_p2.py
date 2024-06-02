import json
import socket
import random

import pymongo


class Myserver():
    def __init__(self):
        self.server_ip = "localhost"
        self.server_port = 9998
        self.gar_data: dict = {}
        self.gacdt_data: dict = {}

    def run_server(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.server_ip, self.server_port))
        server.listen()
        while True:
            client, address = server.accept()
            with client as sock:
                rec_data: list = []
                client_data = sock.recv(4096).decode("utf-8")
                client_data = client_data.split(" ")
                rec_data = client_data
                if rec_data[0] == "gat_user_data":
                    give_back_data = self.give_mdb_data(rec_data)
                elif rec_data[0] == "login":
                    give_back_data = self.check_login_form(rec_data)
                elif rec_data[0] == "cdt_reg":
                    give_back_data = self.cdt_register_form(rec_data)
                elif rec_data[0] == "vot_reg":
                    give_back_data = self.check_client_register(rec_data)
                elif rec_data[0] == "cdt_pass":
                    give_back_data = self.make_cdt_register_form(rec_data)
                elif rec_data[0] == "user_pass":
                    give_back_data = self.make_register_form(rec_data)
                elif rec_data[0] == "get_candidate":
                    give_back_data = self.voting_handle()
                elif rec_data[0] == "getMorePoints":
                    give_back_data = self.give_more_points(rec_data)
                elif rec_data[0] == "get_vote":
                    give_back_data = self.get_voting(rec_data)
                else:
                    pass

                # message: str = "hello We got your data:> " + client_data
                # to_send = bytes(message, "utf-8")
                sock.send(give_back_data)
                client.close()

    def connect_to_mongo_db(self):
        mdb_connection = pymongo.MongoClient("localhost", 27017)
        data_base = mdb_connection["my_db"]
        col = data_base["user_info"]
        return col

    def connect_to_mongo_db_cdt(self):
        mdb_connection = pymongo.MongoClient("localhost", 27017)
        data_base = mdb_connection["my_db"]
        cdts = data_base["candidate_info"]
        return cdts

    def give_mdb_data(self, sms):
        get_mdb = self.connect_to_mongo_db()
        mid = 0
        for i in get_mdb.find():
            data = {"name": i["name"], "email": i["email"], "points": i["points"]}
            self.gar_data.update({mid: data})
            # print(self.gar_data)
            mid += 1

        data_package = json.dumps(self.gar_data)
        data_package = bytes(data_package, "utf-8")
        return data_package

    def cdt_register_form(self, rec_data):
        get_mdb = self.connect_to_mongo_db_cdt()
        for i in get_mdb.find({}, {"_id": 0, "name": 1, "password": 1}):
            print(i["name"], rec_data[1])
            if i["name"] == rec_data[1]:
                rt_data = "cdt_fail"  # ##### This name or email is already register to candidate
                rt_data = bytes(rt_data, "utf-8")
                return rt_data
        rt_data = "cdt_pass"
        rt_data = bytes(rt_data, "utf-8")
        return rt_data

    def make_cdt_register_form(self, rec_data):
        get_mdb = self.connect_to_mongo_db_cdt()
        user_id = random.randint(0, 1000000)
        build = {"_id": user_id, "name": rec_data[1], "age": rec_data[2], "job_role": rec_data[3],
                 "height": rec_data[4],
                 "own_points": 0}
        get_mdb.insert_one(build)
        message = "Register Success !!" + rec_data[1]
        to_send = bytes(message, "utf-8")
        return to_send

    def check_client_register(self, rec_data):
        get_mdb = self.connect_to_mongo_db()
        for i in get_mdb.find({}, {"_id": 0, "name": 1, "email": 1, "password": 1}):
            if i["email"] == rec_data[1] or i['name'] == rec_data[3]:
                rt_data = "user_fail"
                rt_data = bytes(rt_data, "utf-8")
                return rt_data
        rt_data = "user_pass"
        rt_data = bytes(rt_data, "utf-8")
        return rt_data

    def make_register_form(self, rec_data):
        get_mdb = self.connect_to_mongo_db()
        user_id = random.randint(0, 1000000)
        build = {"_id": user_id, "name": rec_data[3], "email": rec_data[1], "password": int(rec_data[2]), "points": 0}
        get_mdb.insert_one(build)
        message = "Register Success !!" + rec_data[3]
        to_send = bytes(message, "utf-8")
        return to_send

    def check_login_form(self, rec_data):
        get_mdb = self.connect_to_mongo_db()
        for i in get_mdb.find({}, {"_id": 0, "name": 1, "email": 1, "password": 1, "points": 1}):
            if i["email"] == rec_data[1] and i['password'] == int(rec_data[2]):
                u_info = {"name": i["name"], "email": i["email"], "password": i["password"], "points": i["points"]}
                data_package = json.dumps(u_info)
                data_package = bytes(data_package, "utf-8")
                return data_package
                # message = "User cannot find. Please try again!"
                # to_send = bytes(message, "utf-8")
                # sock.send(to_send)
        message = "User cannot find. Please try again!"
        to_send = bytes(message, "utf-8")
        return to_send

    def voting_handle(self):
        get_mdb = self.connect_to_mongo_db_cdt()
        mid = 0
        for i in get_mdb.find({}, {"_id": 0, "name": 1, "age": 1, "job_role": 1, "height": 1, "own_points": 1}):
            data = {"name": i["name"], "age": i["age"], "job_role": i["job_role"], "height": i["height"],
                    "own_points": i["own_points"]}
            self.gacdt_data.update({mid: data})
            mid += 1
        data_package = json.dumps(self.gacdt_data)
        data_package = bytes(data_package, "utf-8")
        return data_package

    def give_more_points(self, rec_data):
        get_mdb = self.connect_to_mongo_db()
        for i in get_mdb.find():
            if i["name"] == rec_data[1]:
                change_points: int = i["points"] + 10
                get_mdb.update_one({"name": rec_data[1]}, {"$set": {"points": change_points}})
                data_package = bytes("True", "utf-8")
                return data_package
        data_package = bytes("False", "utf-8")
        return data_package

    def get_voting(self, rec_data):
        get_mdb = self.connect_to_mongo_db()
        get_cdt = self.connect_to_mongo_db_cdt()
        for i in get_cdt.find():
            print(i["name"], rec_data[1])
            if i["name"] == rec_data[1]:
                ud_points = i["own_points"] + 10
                get_cdt.update_one({"name": rec_data[1]}, {"$set": {"own_points": ud_points}})

                for j in get_mdb.find():
                    if j["name"] == rec_data[2]:
                        decrease_points = j["points"] - 10
                        get_mdb.update_one({"name": rec_data[2]}, {"$set": {"points": decrease_points}})

                rt_data = self.voting_handle()
                return rt_data
        rt_data = self.voting_handle()
        return rt_data


if __name__ == '__main__':
    myserver = Myserver()
    myserver.run_server()
