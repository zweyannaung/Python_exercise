import json
import socket


class Myclinet:
    def __init__(self, sms):
        self.join_ip = "localhost"
        self.join_port = 9998
        self.gar_data: dict = {}
        self.check_sms(sms)

    def check_sms(self, sms):
        if sms == "gad":
            self.gat_all_data(sms)
        elif sms == "login":
            self.login_form(sms)
        elif sms == "register":
            self.register_form(sms)

    def connect_server(self):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((self.join_ip, self.join_port))
        return client
        # go_sms = bytes(sms, "utf-8")
        # client.send(go_sms)
        #
        # receive_form_server = client.recv(4096).decode("utf-8")
        # print(receive_form_server)

    def gat_all_data(self, sms):
        get_connect = self.connect_server()
        go_sms = bytes(sms, "utf-8")
        get_connect.send(go_sms)

        receive_form_server = get_connect.recv(4096).decode("utf-8")
        my_data = json.loads(receive_form_server)
        print(my_data)
        print(type(my_data))

    def register_form(self, sms):
        print("Your are in Register-Form")
        reg_name: str = input("Enter your register name :> ")
        reg_email: str = input("Enter your register email :> ")
        reg_password: str = input("Enter your password :>  ")
        data: str = sms + " " + reg_email + " " + reg_password + " " + reg_name

        get_connect = self.connect_server()
        go_sms = bytes(data, "utf-8")
        get_connect.send(go_sms)

        receive_form_server = get_connect.recv(4096).decode("utf-8")

        if receive_form_server == "user_fail":
            print("Your name or email is already exit !!")
        elif receive_form_server == "user_pass":
            print("Your registration is in progressing!!!")
            data: str = receive_form_server + " " + reg_email + " " + reg_password + " " + reg_name
            go_rg = bytes(data, "utf-8")
            get_connect = self.connect_server()
            get_connect.send(go_rg)

            receive_form_server = get_connect.recv(4096).decode("utf-8")
            print(receive_form_server)

    def login_form(self, sms):
        print("Your are in Login-From !!!!")
        login_email: str = input("Enter your email :> ")
        login_password: str = input("Enter your password :>  ")
        data: str = sms + " " + login_email + " " + login_password

        get_connect = self.connect_server()
        go_sms = bytes(data, "utf-8")
        get_connect.send(go_sms)

        receive_form_server = get_connect.recv(4096).decode("utf-8")
        if receive_form_server == "User cannot find. Please try again!":
            print("User cannot find. Please try again!")
        else:
            my_data = json.loads(receive_form_server)
            print(my_data)
            print(type(my_data))
        # print(receive_form_server)


if __name__ == '__main__':
    while True:
        sms: str = input("Enter some value to server:> ")
        my_client = Myclinet(sms)
