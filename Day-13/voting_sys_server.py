import json
import socket
import random

import pymongo


class Myserver:
    def __init__(self):
        self.server_ip = "localhost"
        self.server_port = 9998
        self.gar_data: dict = {}

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
                if rec_data[0] == "gad":
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
        for i in get_mdb.find({}, {"_id": 0}):
            data = {"name": i["name"], "email": i["email"], "password": i["password"]}
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
        build = {"_id": user_id, "name": rec_data[1], "age": rec_data[2], "job_role": rec_data[3], "height": rec_data[4]}
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
        build = {"_id": user_id, "name": rec_data[3], "email": rec_data[1], "password": rec_data[2]}
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


if __name__ == '__main__':
    myserver = Myserver()
    myserver.run_server()
