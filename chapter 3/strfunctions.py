op = "Vedansh mathur"

print(len(op)) #used to define length of the string
print(op.endswith("nsh")) #false
print(op.startswith("nsh")) #false
print(op.capitalize()) #Vedansh mathur
print(op.lower()) #vedansh mathur
print(op.title()) #  capitalise first letter of each word
print(op.strip()) #removes leading and trailing spaces
print(op.lstrip()) #removes leading spaces
print(op.rstrip()) #removes trailing spaces
print(op.replace("h", "j"))
print(op.find("h")) #Returns the index of the first occurrence of a substring, or -1 if not found.
print(op.rfind("h")) #Returns the index of the last occurrence of a substring, or -1 if not found.
print(op.find("k")) #throws -1
print(op.index("h")) #Similar to find() but raises a ValueError if the substring is not found.
print(op.count("h")) #counting the occurence of "h"
print(op.isupper()) #checks all the characters in the string are upper case or not
print(op.islower()) #checks all the characters in the string are lower case or not
print(op.istitle()) #false (checks if all the words are starting with the uppercase or not)
print(op.isspace()) #Checks if all characters are whitespace.
print(op.isalpha()) #all characters are alphabetical or not (even due to the spaces... the error will be shown) 
print(op.isdigit()) #checks int type
print(op.center(10)) #Centers the string within a specified width, padded with spaces (or specified characters).
print(op.rjust(1)) #Right-aligns the string within a specified width, padded with spaces
print(op.ljust(10)) #Left-aligns the string within a specified width, padded with spaces.


