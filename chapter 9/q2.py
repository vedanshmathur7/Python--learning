import random

def game ():
    print ("You mf are playing a game !!")
    with open ("hiscore.txt") as f:
        hiscore = f.read()
        if (hiscore != ""):
            hiscore = int(hiscore)
        else :
            hiscore = 0

    score = random.randint(1,62)
    print (f"Your score is {score}")
    if (score > hiscore):
        with open("hiscore.txt", "w") as f:
            f.write (str(score))

    return score


game ()
