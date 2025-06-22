# Write a Python program to swap the values of two variables without using a temporary variable. 
# For example, if a = 5 and b = 10, after swapping, a should be 10 and b should be 5.

a = 10
b = 5
a = a + b
b = a - b
a = a - b
print (a)
print (b)