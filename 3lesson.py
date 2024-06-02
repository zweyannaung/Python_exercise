print('press 1 : for add')
print ('press 2 : for subtract')
print ('press 3 : for multiply')
print ('press 4 : for divide')
data = int(input('please press something'))
# print(int(data))

if data <5:
    firstNumber = int(input('press first number'))
    secondNumber = int(input('press second number'))
    if data == 1:
        result = firstNumber + secondNumber
    elif data == 2:
        result = firstNumber - secondNumber
    elif data == 3:
        result = firstNumber * secondNumber
    else:
        result = firstNumber / secondNumber    
    print('the result is :',result)
else:
    print('Try again , you must press 1/2/3/4')