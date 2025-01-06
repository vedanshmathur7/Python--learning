a  = 89 #global variable 

def num ():
    global a

    a = 67
    print (a)

print (a) #-> 89
num() #prints 67 until global is applied 
print (a) #-> 67 (if global is called inside the func)
          #-> 89 (if global is not called inside the func)