# Vowel Counter and Classifier
# Write a Python program that takes a string input from the user and:
# Counts the number of vowels (a, e, i, o, u, case-insensitive) in the string.
# If the string has more than 3 vowels, prints "Vowel-heavy string" and the vowel count.
# If the string has 1–3 vowels, prints "Moderate vowels" and the vowel count.
# If the string has no vowels, prints "No vowels found".
# Additionally, if the string is longer than 10 characters, print "Long string".

count = 0

word = input ("Enter the string : ")

for i in word.lower():
    if i in "aeiou":
        count += 1

if (count >= 3):
    print (f"Vowel-heavy string with {count} no. of vowels. ")
elif (count == 0):
    print ("No vowels found")
elif (count >= 1 and count <= 3):
    print (f"Moderate vowels with {count} no. of vowels.")

if (len(word) > 10):
    print ("Long string")
