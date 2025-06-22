# Write a Python program that takes two numbers and an operator (+, -, *, /)
# as input from the user.
# Based on the operator, perform the corresponding arithmetic operation
# and print the result. 
# Include error handling for invalid operators and division by zero.

a = int (input ("Enter the no. : "))
b = int (input ("Enter the no. : "))
operator = input ("Enter the operator : ")

if (operator == '+'):
    print (f"The sum of {a} and {b} is {a+b}")
elif ((operator == '-')):
    print (f"The difference of {a} and {b} is {a-b}")
elif ((operator == '/')):
    print (f"The division of {a} and {b} is {a/b}")
elif ((operator == '*')):
    print (f"The multiplication of {a} and {b} is {a*b}")
elif (operator == '0'):
    raise ZeroDivisionError
else :
    raise SyntaxError