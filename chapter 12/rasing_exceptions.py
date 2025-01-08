a = int (input ("enter the no. a : "))
b = int (input ("enter the no. b : "))

if (b == 0):
    raise ZeroDivisionError("Hey ... zero na daalo plzzz !!")

else :
    c = a/b
    print (round (c,2)) #rounding till 2 decimal values .