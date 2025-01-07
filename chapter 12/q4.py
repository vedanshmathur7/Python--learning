try: 
    a = int (input("Enter the no. a : "))
    b = int (input("Enter the no. b : "))
    print (round((a/b),2))

except ZeroDivisionError as e:
    print ("Infinite hai madarch*d")





