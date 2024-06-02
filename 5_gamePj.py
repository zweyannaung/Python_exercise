import secrets
while True:
    print('Please, Press:1 - for read rules , Press:2 - for play game')
    pressValue = int(input('Enter 1 and 2 :> '))
    if pressValue < 3:
        if pressValue == 1:
            print('Player age is must be over 18 ')
            print('Player must be have money over 1000$')
            print('Player must bet at least 1000$ for each time')
        if pressValue == 2 :
            print('Welcome , you must enter your name and age')
            pName = input('Enter your name :> ')
            pAge = int(input('Enter your age :> '))
            while (len(pName)>2) and (pAge > 17) :
                print('Hello ',pName)
                print('you can play game .. now')
                pMoney = 0
                while True :
                    playerMoney = int(input('Add your current money for using --> '))
                    pMoney += playerMoney
                    print("Now ,you have {}$ ".format(pMoney))
                    while pMoney>999 :
                        
                        playerBet = int(input("Enter your betting amount --> "))
                        while playerBet <= pMoney:
                            if playerBet < 1000 :
                                print("you must bet at least 1000$") 
                                break  
                            else:
                                pMoney -= playerBet
                                secretNumber = secrets.SystemRandom()
                                setSecretNumber = secretNumber.randint(1,5)
                                playerLuckyNum = int(input("Enter your lucky number in 1 to 5 --> "))
                                if playerLuckyNum == setSecretNumber :
                                    print("Lucky Number Is ({})".format(setSecretNumber))
                                    print("Congratulations , Your Are Winner...")
                                    pMoney += playerBet *2
                                    print('your money have now {}'.format(pMoney))
                                else:
                                    print("Lucky Number Is ({})".format(setSecretNumber))
                                    print("Your Are Lose , Try Again..")
                                print('you only have {} money left'.format(pMoney))
                                if pMoney<1000 :
                                    break
                                else:
                                    playerBet = int(input("Enter your betting amount --> "))
  
                    print('your money must be have over 1000$')
                    playerQuite = input("if you want exit , Enter >> (yes or no) --> ")
                    if playerQuite == 'yes' :
                        pName= ""
                        pAge= ""
                        break
                        
            print('Please, read rule again!')        
    else:
        print('### Please enter 1 and 2')
        