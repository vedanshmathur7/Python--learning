f = open ("myfiles.txt")

# data = f.read()
# print (data)

# lines = f.readlines()
# print (lines , type(lines)) #will be considered as lists 

line1 = f.readline()
print (line1)
line2 = f.readline()
print (line2)
line3 = f.readline()
print (line3)
line4 = f.readline()
print (line4)
f.close()