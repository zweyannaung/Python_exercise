import email

my_Data = {}
get_pass = True

def goRegister():
    r_user_gmail = input("Enter your gmail =:> ")
    data_exit(r_user_gmail)
    global get_pass
    print(get_pass)
    if get_pass:
        r_user_password = input("Enter your password =:>")
        myId = len(my_Data)
        new_data = {myId: {"gmail": r_user_gmail, "password": r_user_password}}
        my_Data.update(new_data)
        print(my_Data)

    else:
        print("#####Email already exit !! ")
        get_pass = True



def data_exit(e):
    my_len = len(my_Data)
    for i in range(my_len):
        if my_Data[i]["gmail"] == e:
            global get_pass
            get_pass = False



def goLogin():
    result = 0
    print("Login page")
    l_user_gmail = input("Enter your gmail =:> ")
    l_user_password = input("Enter your password =:> ")
    for i in range(len(my_Data)):
        if my_Data[i]["gmail"] == l_user_gmail and my_Data[i]["password"] == l_user_password:
            result = 1

    if result == 1:
        print("##### Welcome chief!!", l_user_gmail)
    else:
        print("####user not found", l_user_gmail)


def signIn():
    user_Input = int(input("Please press (1) for Register \n press (2) for Login \n press (3) for Exit :>> "))
    if user_Input == 1:
        goRegister()
    elif user_Input == 2:
        goLogin()
    elif user_Input == 3:
        exit(1)
    else:
        signIn()


if __name__ == '__main__':
    while True:
        signIn()
