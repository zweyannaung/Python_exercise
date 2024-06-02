# 0: {"email": "zwe", "password": 123}
class Voting:
    def __init__(self):
        self.my_data: dict = {}
        # 0: {"email": "zwe@gmail.com", "username": "zwe", "password": 111},
        # 1: {"email": "yan@gmail.com", "username": "yan", "password": 222},
        # 2: {"email": "naung@gmail.com", "username": "naung", "password": 333},
        # 3: {"email": "zyn@gmail.com", "username": "zyn", "password": 444}

        self.user_login: dict = {}
        self.v_student: dict = {
            0: {"name": "Ronaldo", "v_mark": 0, "voter": []},
            1: {"name": "Messi", "v_mark": 0, "voter": []},
            2: {"name": "Rooney", "v_mark": 0, "voter": []},
            3: {"name": "Naymar", "v_mark": 0, "voter": []},
        }
        self.build_id = 0

    def get_saving_data(self):
        reg_id = 0
        f = open("day_8_data.txt", 'r')
        getting_data = f.readlines()
        for i in getting_data:
            rec_data = i.split(" ")
            if rec_data[0] == "register":
                b_reg_data = {
                    int(rec_data[1]): {"email": rec_data[2], "username": rec_data[3], "password": int(rec_data[4])}}
                self.my_data.update(b_reg_data)
                reg_id += 1
            elif rec_data[0] == "login":
                b_login_data = {"email": rec_data[1], "username": rec_data[2], "password": int(rec_data[3])}
                self.user_login.update(b_login_data)
            elif rec_data[0] == "v_student":
                for j in range(len(self.v_student)):
                    if self.v_student[j]["name"] == rec_data[2]:
                        self.v_student[j]["v_mark"] = int(rec_data[3])
                        for x in getting_data:
                            rec_data_2 = x.split(" ")
                            if rec_data_2[0] == self.v_student[j]["name"]:
                                self.v_student[j]["voter"].append(rec_data_2[1])



    # #### main option
    def main_option(self):
        # global option
        option = 0
        try:
            option = int(input("Press: 1 to Register/ Press: 2 to Login/ Press: 3 to Exit/ :>  "))
            print("\n")
        except Exception as err:
            print("##### Please enter number")
            self.main_option()

        if option == 1:
            self.register()
        elif option == 2:
            self.login()
        elif option == 3:
            self.saving_all_data()
            exit(1)
        else:
            print("##### you must be press 1/2/3")
            self.main_option()

    def register(self):
        print("##### Register Option")
        while True:
            r_email = input("Enter register email :> ")
            for i in range(len(self.my_data)):
                if r_email == self.my_data[i]["email"]:
                    print("##### your email already exit !!")
                    print("\n")
                    while True:
                        try:
                            re_register = int(input("New register press: 1 / exit to option press: 2 :> "))
                            print("\n")
                            if re_register == 1:
                                self.register()
                                break
                            elif re_register == 2:
                                self.main_option()
                                break
                            else:
                                print("##### you must enter number 1 or 2")
                        except Exception as err:
                            print("##### you must enter number 1 or 2 !!")

            while True:
                try:
                    r_username = input("Enter user name :> ")
                    r_password = int(input("Enter your account password :> "))
                    r_re_password = int(input("Enter retype password :> "))
                    if r_password == r_re_password:
                        self.build_id = len(self.my_data)
                        build_account: dict = {
                            self.build_id: {"email": r_email, "username": r_username, "password": r_password}}
                        self.my_data.update(build_account)
                        print("##### Register Successfully !!!", self.my_data[self.build_id]["email"])
                        print("\n")
                        break
                    else:
                        print("##### your password incorrect : try again! ")
                except Exception as err:
                    print("### invalid password: try again!!")
                    continue
            break
        self.main_option()

    def login(self):
        print("#### Login Option !!! ")
        login_exit = False
        if len(self.user_login) != 0:
            login_exit = True

            print("Your are already login to ", self.user_login["email"])
            print("\n")
            while True:
                try:
                    user_request = int(input("Press: 1 to get student info / Press: 2 to get voting / Press: 3 to "
                                             "logout / Press: 4 to Exit :> "))
                    print("\n")
                    if user_request == 1:
                        self.check_v_mark()
                    elif user_request == 2:
                        is_user_voted = 0
                        is_user_voted = self.check_user_vote(self.user_login['username'])
                        if is_user_voted == 0:
                            self.student_voting(self.user_login["email"], self.user_login['username'])
                        else:
                            print("user - ,'{}' is already voted !!".format(self.user_login['username']))
                            while True:
                                try:
                                    user_esk = int(input("Press: 1 to logout / Press: 2 to main_option :> "))
                                    if user_esk == 1:
                                        self.user_login = {}
                                        print("##### Your account is logout now !!")
                                        print("\n")
                                        self.main_option()
                                        break
                                    elif user_esk == 2:
                                        self.main_option()
                                        break
                                    else:
                                        print("##### you must press 1/2")
                                        break
                                except Exception as err:
                                    print("##### you must press 1/2")
                        break
                    elif user_request == 3:
                        self.user_login = {}
                        print("##### Your account is logout now !!")
                        print("\n")
                        self.main_option()
                        break
                    elif user_request == 4:
                        self.saving_all_data()
                        exit(1)
                    else:
                        print("##### You must press 1/2/3/4 !!")
                        continue
                except Exception as err:
                    print("##### You must press 1/2/3/4 !!")
                    continue
        if not login_exit:
            try:
                check_acc = False
                l_username = ""
                l_email = input("Enter Your Email :> ")
                l_password = int(input("Enter Your Password :> "))

                for i in range(len(self.my_data)):
                    if l_email == self.my_data[i]["email"] and l_password == self.my_data[i]["password"]:
                        l_username = self.my_data[i]["username"]
                        check_acc = True
                        break
                if check_acc:
                    login_build = {"email": l_email, "username": l_username, "password": l_password}
                    self.user_login = login_build
                    print("##### welcome", l_username)
                    self.student_voting(l_email, l_username)
                else:
                    print("##### your account doesn't exit")
                    self.main_option()

            except Exception as err:
                print("##### Invalid your input text !!!")
                self.main_option()

    def student_voting(self, l_email, l_username):
        while True:
            print("\n")
            print("##### Please chose student voting number for your voting")
            for i in range(len(self.v_student)):
                assing_num = i + 1
                print("Student: {} ,voting number is ({}) ".format(self.v_student[i]["name"], assing_num))
            try:
                user_vote = int(input("Please chose your voting number 1/2/3/4 :> "))
                if user_vote == 1:
                    self.add_vote(0, l_username)
                    break
                elif user_vote == 2:
                    self.add_vote(1, l_username)
                    break
                elif user_vote == 3:
                    self.add_vote(2, l_username)
                    break
                elif user_vote == 4:
                    self.add_vote(3, l_username)
                    break
                else:
                    print("##### student voting number are 1/2/3/4 !!!, Please chose one of them !!")
            except Exception as err:
                print("##### student voting number are 1/2/3/4 !!!, Please chose one of them !!")

    def add_vote(self, e, j):
        for i in range(len(self.v_student)):
            if e == i:
                self.v_student[e]["v_mark"] += 1
                self.v_student[e]["voter"].append(j)
                print("##### Voting Success , Thank for your voting to {}".format(self.v_student[e]["name"]))
                print("\n")

        try:
            user_leave = int(
                input("Exit to main option for press: 1 / logout and exit to main option for press: 2 :> "))
            print("\n")
            if user_leave == 1:
                self.main_option()
            elif user_leave == 2:
                self.user_login = {}
                print("##### Your account is logout now !!")
                self.main_option()
        except Exception as err:
            print(err)

    def check_v_mark(self):
        for i in range(len(self.v_student)):
            name = self.v_student[i]["name"]
            vote_mark = self.v_student[i]["v_mark"]
            voter = self.v_student[i]["voter"]
            print("{}:{}, voting quantity - {}, voter - {}".format(i, name, vote_mark, voter))

    def check_user_vote(self, e):
        for i in range(len(self.v_student)):
            for j in range(len(self.v_student[i]["voter"])):
                if self.v_student[i]["voter"][j] == e:
                    return 1

    def saving_all_data(self):
        my_saving_data = open("day_8_data.txt", 'w')
        for i in range(len(self.my_data)):
            r_type = "register"
            r_id = i
            r_email = self.my_data[i]["email"]
            r_username = self.my_data[i]["username"]
            r_password = self.my_data[i]["password"]
            rec_data_built_1 = r_type + " " + str(r_id) + " " + r_email + " " + r_username + " " + str(
                r_password) + "\n"
            my_saving_data.write(rec_data_built_1)
        if len(self.user_login) != 0:
            rec_data_built_2 = "login" + " " + self.user_login["email"] + " " + self.user_login["username"] + " " + str(
                self.user_login["password"]) + "\n"
            my_saving_data.write(rec_data_built_2)
        for i in range(len(self.v_student)):
            v_type = "v_student"
            v_id = i
            v_name = self.v_student[i]["name"]
            v_vote_mark = self.v_student[i]["v_mark"]
            rec_data_built_3 = v_type + " " + str(v_id) + " " + v_name + " " + str(v_vote_mark) + "\n"
            my_saving_data.write(rec_data_built_3)
            # for voter list________
            length = len(self.v_student[i]["voter"])
            for j in range(length):
                vtr_type = self.v_student[i]["name"]
                rec_data_built_4 = vtr_type + " " + self.v_student[i]["voter"][j] + " " + "\n"
                my_saving_data.write(rec_data_built_4)
