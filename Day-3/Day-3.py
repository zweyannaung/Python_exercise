# Function &  Array
# def apple():
#     print("hello Python")
#
#
# apple()

# my_list = [10, 30, 50, [1, 2, 3, 4], 70, 60]
# my_list += [100]
# my_list += [200]
# print(my_list)
# my_listTwo = [70, 80, 90]
# my_list.extend(my_listTwo)
# print(my_list)
# ______________________________

db = {}


def addingData():
    user_Email = input("Enter Email => ")
    user_Password = input("Enter password => ")
    myId = len(db)
    print(myId)
    addData = {myId: {"Email": user_Email, "Password": user_Password}}
    db.update(addData)


if __name__ == '__main__':
    for i in range(3):
        addingData()
        print(db)
