#using for loop
sum = 0
n = int (input("Enter the no. till the sum is to be found : "))

for i in range (1, (n+1)):
    sum += i
    
    
print(sum)


#using while loop
n = int (input("Enter the no. : "))

i = 1
sum = 0

while (i <= n):
    sum += i
    i += 1

print (sum)