# Simple Grade Calculator
# Write a Python program that takes a numerical score (0–100) as input from the user and prints the corresponding grade based on the following:
# 90–100: A
# 80–89: B
# 70–79: C
# 60–69: D
# Below 60: F If the input is not in the range 0–100, print "Invalid score".

marks = int (input ("Enter the marks : "))

if (marks <= 90 and marks >= 100):
    print ("grade - A")
elif (marks <= 80 and marks > 89):
    print ("grade - B")
elif (marks <= 70 and marks >= 79):
    print ("grade - C")
elif (marks <= 60 and marks >= 69):
    print ("grade - D")
else:
    print ("grade - F\nAukaat m rho!")