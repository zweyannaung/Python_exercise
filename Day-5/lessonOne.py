setNumber = 1


def myFunOne():
    global setNumber
    setNumber = 2
    print(setNumber)

def myFunTwo():
    setNumber = 3
    print(setNumber)


if __name__ == '__main__':
    myFunOne()
    print(setNumber)
    myFunTwo()
    print(setNumber)
