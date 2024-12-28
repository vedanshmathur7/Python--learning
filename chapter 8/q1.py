def great (a,b,c):
    if (a>b and a>c):
        return a
    if (b>a and b>c):
        return b
    if (c>b and c>a):
        return c
    
a = int (input("Enter the no. a : "))
b = int (input("Enter the no. b : "))
c = int (input("Enter the no. c : "))

print(f"The greatest no. is {great(a,b,c)}. ")