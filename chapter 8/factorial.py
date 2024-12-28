def fac (num):
    if (num==1 or num == 0):
        return 1
    else :
        fact = num * fac (num-1)
        return fact
    
num = int (input("Enter the no. to find the factorial of : "))

print (f"The factorial of {num} is {fac(num)}")