my_Data = []
def get_my_data():
    idx = 0
    rec_data = open("../my_data2.txt",'r').readlines()
    for i in rec_data:
        myRec_data = i.split(" ")
        add_data = {'id':idx , "email": myRec_data[0] , "password": myRec_data[1]}
        my_Data.append(add_data)
        idx += 1



if __name__ == '__main__':
    get_my_data()
    print(my_Data[0]['email'])