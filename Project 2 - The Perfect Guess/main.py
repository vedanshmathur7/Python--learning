import random
n  = random.randint(1,100)
a = -1
guesses = 1

while (a != n):
    a = int (input("Enter the no. : "))
    if (a>n):
        print ("Lower no. please ")
        guesses += 1
    elif (a<n):
        print ("Higher no. please ")
        guesses += 1

print (f"Yeahh!! You've guessed the no.{n} correctly, in {guesses} no. of guesses !")