# mini project -- Guess The Number

import random
target= random.randint(1,100)
while True:
    userchoice=input("Guess the Number or Press (Q) to Quit : ")
    if(userchoice=="Q" or userchoice=="q"):
        print("You Are Out of Game")
        break
    userchoice=int(userchoice)
    if(userchoice==target):
        print("success : Currect Guess!!")
        break
    if(userchoice>=target):
        print("The number is Bigger then the target !!")
    if(userchoice<=target):
        print("the number is Smaller then the target !!")
    else:
        print(userchoice)


print("----game over----")    