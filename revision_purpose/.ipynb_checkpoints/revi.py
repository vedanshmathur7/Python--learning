n = int(input("Enter the no.: "))
if n > 1:
    for i in range(2, n):
        if n % i == 0:
            print("The no. is not prime.")
            break
    else:
        print("The no. is prime.")
else:
    print("The no. is not prime.
