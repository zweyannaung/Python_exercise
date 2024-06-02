import json
import socket

domain_key = ["@gmail.com", "@mail.com", "@facebook.com", "@yahoo.com", "@apple.com", "@mail.com"]
chr_special = [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 58, 59, 60, 61, 62, 63, 91, 92, 93, 94,
               95, 96, 123, 124, 125, 126]


class Myclinet:
    def __init__(self, sms):
        self.join_ip = "localhost"
        self.join_port = 9998
        self.user_login_data: dict = {}
        self.check_sms(sms)

    def check_sms(self, sms):
        if sms == "gad":
            self.gat_all_data(sms)
        elif sms == "login":
            self.login_form(sms)
        elif sms == "register":
            chk_cdt_vtr = input("Press : 1 for candidate\n Press : 2 for voter\n :> ")
            if chk_cdt_vtr == str(1):
                print("hello cdt")
                self.cdt_register_form("cdt_reg")
            elif chk_cdt_vtr == str(2):
                print("hello vot")
                self.register_form("vot_reg")

    def connect_server(self):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((self.join_ip, self.join_port))
        return client

    def gat_all_data(self, sms):
        get_connect = self.connect_server()
        go_sms = bytes(sms, "utf-8")
        get_connect.send(go_sms)

        receive_form_server = get_connect.recv(4096).decode("utf-8")
        my_data = json.loads(receive_form_server)
        print(my_data)
        print(type(my_data))

    def checking_domain(self, e):
        check_name = "pass"
        check_domain = "fail"
        leng = len(e)
        for i in range(leng):
            if e[i] == '@':
                domain_name = e[0:i]
                domain_form = e[i:]
                for j in domain_name:
                    for k in chr_special:
                        if k == ord(j):
                            check_name: str = "fail"
                            break
                for k in domain_key:
                    if k == domain_form:
                        check_domain = "pass"
        if check_domain == "pass" and check_name == "pass":
            return "pass"
        else:
            return "fail"

    def cdt_register_form(self, e):
        print("your are in Candidate Register-form")
        cdt_name: str = input("Enter your Candidate name :> ")
        while True:
            cdt_email: str = input("Enter your Candidate email :> ")
            email_check = self.checking_domain(cdt_email)
            if email_check == "pass":
                break
            elif email_check == "fail":
                print("##### your email is wrong, Try again!!! ")
                continue
        cdt_age: str = input("Enter your Candidate age :> ")
        cdt_job_role: str = input("Enter your Candidate job_role :> ")
        cdt_height: str = input("Enter your Candidate height :> ")
        data: str = e + " " + cdt_name + " " + cdt_email + " " + cdt_age + " " + cdt_job_role + " " + cdt_height
        get_connect = self.connect_server()
        go_sms = bytes(data, "utf-8")
        get_connect.send(go_sms)
        receive_form_server = get_connect.recv(4096).decode("utf-8")

        if receive_form_server == "cdt_fail":
            print("##### Your name or email is already register to candidate")
        elif receive_form_server == "cdt_pass":
            print("##### Your registration is in progressing!!!")
            data: str = receive_form_server + " " + cdt_name + " " + cdt_age + " " + cdt_job_role + " " + cdt_height
            go_rg = bytes(data, "utf-8")
            get_connect = self.connect_server()
            get_connect.send(go_rg)

            receive_form_server = get_connect.recv(4096).decode("utf-8")
            print(receive_form_server)

    def register_form(self, e):
        print("##### Your are in Voter Register-Form")
        reg_name: str = input("Enter your register name :> ")
        while True:
            reg_email: str = input("Enter your register email :> ")
            email_check = self.checking_domain(reg_email)
            if email_check == "pass":
                break
            elif email_check == "fail":
                print("##### your email is wrong, Try again!!! ")
                continue
        reg_password: str = input("Enter your password :>  ")
        data: str = e + " " + reg_email + " " + reg_password + " " + reg_name

        get_connect = self.connect_server()
        go_sms = bytes(data, "utf-8")
        get_connect.send(go_sms)

        receive_form_server = get_connect.recv(4096).decode("utf-8")

        if receive_form_server == "user_fail":
            print("##### Your name or email is already exit !!")
        elif receive_form_server == "user_pass":
            print("##### Your registration is in progressing!!!")
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

        user_choice = False
        receive_form_server = get_connect.recv(4096).decode("utf-8")
        if receive_form_server == "User cannot find. Please try again!":
            print("##### User cannot find. Please try again!")
        else:
            my_data = json.loads(receive_form_server)
            self.user_login_data: dict = my_data
            user_choice = True
            # print(self.user_login_data)
            print("##### Name :> {0} \n #### remaining points :> {1}".format(self.user_login_data["name"],
                                                                             self.user_login_data["points"]))
        while user_choice:
            try:
                user_chose_num: int = int(input("Press Enter >>\n 1: get user option \n 2: get main option\n 3: "
                                                "exit\n :>> "))
                if user_chose_num == 1:
                    self.user_option()
                elif user_chose_num == 2:
                    break
                elif user_chose_num == 3:
                    exit(1)
                else:
                    print(type(user_choice))
                    print("##### Plz! Enter> 1,2,3")
                    continue
            except Exception as err:
                print("##### Plz! Enter> 1,2,3")
                continue

    def user_option(self):
        print("##### User Option #####")
        try:
            option: int = int(input("Press Enter >>\n 1: to vote\n 2: get more points\n 3: voting "
                                    "ranking\n 4: transfer points\n 5: user info edit\n 6: delete account\n 0: back\n "
                                    ":> "))
            if option == 1:
                pass
            elif option == 2:
                pass
            elif option == 3:
                pass
            elif option == 4:
                pass
            elif option == 5:
                pass
            elif option == 6:
                pass
            elif option == 0:
                pass
            else:
                print("##### Plz! enter:> 1,2,3,4,5,6,0")
        except Exception as err:
            print("##### Plz! enter:> 1,2,3,4,5,6,0")


if __name__ == '__main__':
    while True:
        sms: str = input("Input some data to server:> ")
        my_client = Myclinet(sms)
