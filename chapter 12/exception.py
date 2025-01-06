try :
    a = int (input ("enter the no. mf! : "))
    print (a)

except ValueError as v:
    print ("bkl aukaat m")
    print (v)

except Exception as e:
    print ("kaam 25 h")
    print (e)