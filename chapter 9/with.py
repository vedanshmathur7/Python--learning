f = open ("myfiles.txt")

print(f.read())
f.close()

#The same thing can be done by using with statement 
with open ("myfiles.txt") as f:
    print (f.read())

# You dont have to explicitly close the file