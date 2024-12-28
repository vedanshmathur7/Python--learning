def ramram (name, salu = "namaste"):
    nam = (f"{name} {salu}")
    return nam

name = input("Enter your name : ")
salu = input("The salutation u want to greeted with : ")

op = ramram(name, salu)
print (op)