def sum(n):
    if (n==1):
        return 1
    else :
        op = n + sum(n-1)
        return op

a = int (input("Enter the no. : "))
print (f"The sum of the terms {a} is {sum(a)}.")

