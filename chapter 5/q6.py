# Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique

rajesh = {}
print (type (rajesh ))

name = input ("Enter your name : ")
lang = input ("Enter the lang : ")
rajesh.update({name : lang})

name = input ("Enter your name : ")
lang = input ("Enter the lang : ")
rajesh.update({name : lang})

name = input ("Enter your name : ")
lang = input ("Enter the lang : ")
rajesh.update({name : lang})

name = input ("Enter your name : ")
lang = input ("Enter the lang : ")
rajesh.update({name : lang})

print (rajesh)