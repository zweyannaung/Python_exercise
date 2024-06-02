import json

# File in python

# for read
# f = open("../my_data2.txt", 'r')
# print(f.read())
# f = open("../my_data2.txt",'a')
# f.write("Hello Mingalarpar")
# f.write("\n")
# f.close()
# f = open("../my_data2.txt",'r')
# print(f.read())

# over write
my_dOne = "Myanmar Pyi Gyi Nyein Chan Par Zay"
my_dTwo = "Kyang Mar Shyin Lang Kay Par Zay"
my_dThree: dict = {
    0: {"name": "zwe@gmail.com", "username": "zwe", "password": 111},
    1: {"name": "yan@gmail.com", "username": "yan", "password": 222},
    2: {"name": "naung@gmail.com", "username": "naung", "password": 333},
    3: {"name": "zyn@gmail.com", "username": "zyn", "password": 444},
}
f = open("../my_data2.txt", 'w')
# f.write(my_dOne)
# f.write("\n")
# f.write(my_dTwo)
# f.write(str(my_dThree))
# f.close()
# f = open("../my_data2.txt", 'r')
# my-data = json.load(f)
# print(my-data)

with open("../my_data2.txt", 'r') as file:
    #     file.read()
    #     print(file.read())
    # my_data = json.load(file)
    # print(my_data)
