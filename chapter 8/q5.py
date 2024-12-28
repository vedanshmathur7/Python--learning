def pattern(n):
    if (n==0):
        return 0
    
    else :
        print ("*" * n)
        pattern(n-1)


n = int (input("Enter the no. : "))
print (pattern(n))