# my_data:dict = {}
# 0: {"email": "zwe", "password": 123}
class Voting:
    def __init__(self):
        self.my_data: dict = {}
        self.user_login: dict = {}
        self.v_student: dict = {
            0: {"name": "Ronaldo", "v_mark": 0,"voter": []},
            1: {"name": "Messi", "v_mark": 0,"voter": []},
            2: {"name": "Rooney", "v_mark": 0,"voter": []},
            3: {"name": "Naymar", "v_mark": 0,"voter": []},
        }
        self.build_id = 0

    # #### main option
    def main_option(self):
        # global option
        option = 0
        try:
            option = int(input("Press: 1 to Register/ Press: 2 to Login/ Press: 3 to Exit/ "))
        except Exception as err:
            print("##### Please enter number")
            self.main_option()

        if option == 1:
            self.register()
        elif option == 2:
            self.login()
        elif option == 3:
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
                    while True:
                        try:
                            re_register = int(input("New register press: 1 / exit to option press: 2 :> "))
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
                    r_password = int(input("Enter your account password :> "))
                    r_re_password = int(input("Enter retype password :> "))
                    if r_password == r_re_password:
                        self.build_id = len(self.my_data)
                        build_account: dict = {self.build_id: {"email": r_email, "password": r_password}}
                        self.my_data.update(build_account)
                        print("##### Register Successfully !!!", self.my_data[self.build_id]["email"])
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
            while True:
                try:
                    user_request = int(input("Press: 1 to get voting / Press: 2 to logout / Press: 3 to Exit :> "))
                    if user_request == 1:
                        self.student_voting(self.user_login["email"])
                        break
                    elif user_request == 2:
                        self.user_login = {}
                        print("Your account is logout now !!")
                        self.main_option()
                        break
                    elif user_request == 3:
                        exit(1)
                    else:
                        print("##### You must press 1 or 2 !!")
                        continue
                except Exception as err:
                    print("##### You must press 1 or 2 !!")
                    continue
        if not login_exit:
            try:
                check_acc = False
                l_email = input("Enter Your Email :> ")
                l_password = int(input("Enter Your Password :> "))

                for i in range(len(self.my_data)):
                    if l_email == self.my_data[i]["email"] and l_password == self.my_data[i]["password"]:
                        check_acc = True
                        break
                if check_acc:
                    login_build = {"email": l_email, "password": l_password}
                    self.user_login = login_build
                    print("##### welcome", l_email)
                    self.student_voting(l_email)
                else:
                    print("##### your account doesn't exit")
                    self.main_option()

            except Exception as err:
                print("##### Invalid your input text !!!")
                self.main_option()

    def student_voting(self, l_email):
        while True:
            print("##### Please chose student voting number for your voting")
            for i in range(len(self.v_student)):
                assing_num = i + 1
                print("Student: {} ,voting number is ({}) ".format(self.v_student[i]["name"], assing_num))
            try:
                user_vote = int(input("Please chose your voting number 1/2/3/4 :> "))
                if user_vote == 1:
                    self.add_vote(0)
                    break
                elif user_vote == 2:
                    self.add_vote(1)
                    break
                elif user_vote == 3:
                    self.add_vote(2)
                    break
                elif user_vote == 4:
                    self.add_vote(3)
                    break
                else:
                    print("##### student voting number are 1/2/3/4 !!!, Please chose one of them !!")
            except Exception as err:
                print("##### student voting number are 1/2/3/4 !!!, Please chose one of them !!")

    def add_vote(self,e):
        for i in range(len(self.v_student)):
            if e == i:
                self.v_student[e]["v_mark"] += 1
                print("##### Voting Success , Thank for your vite")
        print(self.v_student[e])
        print(self.user_login)
        try:
            user_leave = int(input("Exit to main option for press: 1 / logout and exit to main option for press: 2 :> "))
            if user_leave == 1:
                self.main_option()
            elif user_leave == 2:
                self.user_login = {}
                print("##### Your account is logout now !!")
                self.main_option()
        except Exception as err:
            print(err)
