'''
-1 : water 
0 : gun 
1 : snake 
'''

import random

computer = random.choice([-1,1,0])

youstr = input("Enter your choice : ")
youdict = {
    "s" : 1,
    "g" : 0,
    "w" : -1
}
you = youdict[youstr]

revDict = {
    1 : "Snake",
    0 : "Gun",
    -1 : "Water"
}

print (f"You chose {revDict[you]}\nComputer chose {revDict[computer]}.")

if (you == computer):
    print ("The match is draw")

else: 
    if (you == 1 and computer == -1):
        print("You Won !!")
    elif (you == 1 and computer == 0):
        print("You Lose !!")
    elif (you == -1 and computer == 1):
        print("You Lose !!")
    elif (you == -1 and computer == 0):
        print("You Won !!")
    elif (you == 0 and computer == -1):
        print("You Lose !!")
    elif (you == 0 and computer == 1):
        print("You Won !!")
    else :
        print ("Invalid input !")
