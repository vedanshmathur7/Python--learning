def fibon(num):
    lis = [0, 1]

    for i in range (num-2):
        lis.append(lis[-1] + lis[-2])

    return lis

num = int (input("Enter the no. of terms : "))
fibo = fibon (num)

print (f"The fibonacci series till {num} is {fibo}")
