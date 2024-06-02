db = []


def get_data():
    idx = 0
    with open("my_data.txt", 'r') as file:
        get_recData = file.readlines()
        for i in get_recData:
            rec_data = i.split(" ")
            add_data = {'id': idx, "email": rec_data[0], "password": rec_data[1]}
            db.append(add_data)
            idx += 1
            # print(db)


        # db.extend(my_rec)
        # file.readline()
        # for line in file:
        #     x = line[:-1]
        #     db.append(x)
        # my_rec = file.readlines()
        # # res = my_rec.strip('][').split(', ')
        # db.append(my_rec)


email_exit = -1


def main_sector():
    main_option = int(input("Press 1 to Register:\nPress 2 to Login\nPress 3 Exit:"))
    if main_option == 1:
        registration()
    elif main_option == 2:
        login()
    elif main_option == 3:
        my_exit()
    else:
        print("Invalid Option")
        main_sector()


def registration():
    user_email = input("Enter your email:")
    email_get = email_exit(user_email)

    if email_get != None:
        print("Email already exit:")
        main_sector()
    else:
        # user_name = input("Enter your username:")
        user_password = input("Enter your password:")
        # user_phone = int(input("Enter your phone:"))
        # user_age = int(input("Enter your age:"))

        id = len(db)

        to_insert = {
            "id": id,
            "email": user_email,
            "password": user_password,
            # "u_name":user_name,
            # "phone":user_phone,
            # "age":user_age
        }

        db.append(to_insert)
        rec(db)


def login():
    user_found = -1;
    print("This is login sector")
    l_user_email = input("Enter your email to login:")
    l_user_password = input("Enter your password to login:")

    for i in range(len(db)):
        if db[i]["email"] == l_user_email and db[i]["password"] == l_user_password:
            user_found = i
    if user_found != -1:
        print("Login Success!")
        user_profile(user_found)
    else:
        print("### User Not Found ")


def my_exit():
    # rec(db)
    exit(1)


def user_profile(user_found):
    print("Welcome:", db[user_found]["email"])

    l_out = int(input("Press 1 for logOut :: "))
    if l_out == 1:
        # rec(db)
        print("hello")


def email_exit(e):
    length = len(db)
    for i in range(length):
        if db[i]["email"] == e:
            return i


def rec(e):
    with open("my_data.txt", 'w') as myFile:
        for i in range(len(e)):
            rec_email = e[i]["email"]
            rec_password = e[i]["password"]
            rec_data = rec_email + ' ' + rec_password + ' ' + '\n'
            myFile.write(rec_data)


1

if __name__ == '__main__':
    get_data()
    while True:
        main_sector()
