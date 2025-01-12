a= '''
hello guuys ;)
'''

f = open ("myfiles.txt" , "a") #a is for appending / adding
for i in range (100):
    f.write (a)



f.close ()
