import secrets

while True:
    print("####### Press : (1) to play the game , Press : (2) for read the rule")
    userNumber = int(input("Enter the number 1 & 2 :>> "))
    if userNumber == 2:
        print("### You must be over 18years old")
        print("### You must have money at least 100$ ")
        print("### you must be bet at least 100$ for each time")
    elif userNumber == 1:
        pQuit = 0
        while pQuit == 0:
            playName = input("Enter your name (## your name should be over one word ##) :>> ")
            playAge = int(input("Enter your age :>> "))
            if len(playName) > 2 and playAge >= 18:
                pMoney = 0
                print("### Welcome to our game player ;> {} !!!!".format(playName))
                print("### Enjoy the game now")
                while pQuit == 0:
                    pMoney = int(input("Please fill your money ($) :>> "))
                    while pQuit == 0 and pMoney >= 100:
                        print("### your money have now {}$".format(pMoney))
                        playerGuess = int(input("Enter Your guess number of 1 to 6 :>> "))
                        if 1 <= playerGuess <= 6:
                            playerBet = int(input("Enter Your Bet Price :>> "))
                            if playerBet >= 100:
                                pMoney -= playerBet
                                secretNumber = secrets.SystemRandom().randint(1, 6)
                                if playerGuess == secretNumber:
                                    print("### Congratulation !!!!. Your are the winner !!!!")
                                    print("### Your get 2times of your bet")
                                    pMoney += playerBet * 2
                                    while pQuit == 0:
                                        print("### If you want to exit press(3) or keep play press(1)")
                                        pQuit2 = int(input("exit(3) or play(1) :>> "))
                                        if pQuit2 == 3:
                                            print("your can exchange your {}$".format(pMoney))
                                            pQuit = 1
                                            break
                                        elif pQuit2 == 1:
                                            break
                                        else:
                                            print("### you must enter (1) or (3)")
                                            continue
                                else:
                                    print("### Sorry !!!!. Secret Number is {} , Try again!!".format(secretNumber))
                                    if pMoney < 100:
                                        print("### Your money have now :>> {}".format(pMoney))
                                    while True:
                                        print("### If you want to exit press(3) or keep play press(1)")
                                        pQuit2 = int(input("exit(3) or play(1) :>> "))
                                        if pQuit2 == 3:
                                            print("your can exchange your {}$".format(pMoney))
                                            pQuit = 1
                                            break
                                        elif pQuit2 == 1:
                                            break
                                        else:
                                            print("### you must enter (1) or (3)")
                                            continue
                            else:
                                print("### Your betting value must be 100$ at least")
                        else:
                            print("You must chose number of 1 to 6")
                    print("### player money should be over 100$")
                    # 

            elif len(playName) < 2:
                print("### your name must be more than two word !!!")
                continue
            elif playAge < 18:
                print("### your age must be over 18")
                print("### Do you want ot exit !! Press (3) or keep play !! Press (1)")
                pQuit1 = int(input("exit(3) or play(1) :>> "))
                if pQuit1 == 1:
                    continue
                else:
                    break

    else:
        print("### You must be enter (1) or (2) ")
