# Number Classifier
# Write a Python program that takes an integer input from the user and classifies it as follows:
# Print "Positive" if the number is greater than 0.
# Print "Negative" if the number is less than 0.
# Print "Zero" if the number is 0.
# Additionally, print "Even" if the number is even or "Odd" if the number is odd.
# For example, if the input is 4, the output should be "Positive" and "Even".

a = int (input ("Enter the no. : "))

if (a > 0):
    print ("The no. is positive.")
elif (a < 0):
    print ("The no. is negative.")
else :
    print ("The no. is zero.")

if (a %2 == 0):
    print ("The no. is even.")
elif (a %2 != 0):
    print ("The no. is odd.")