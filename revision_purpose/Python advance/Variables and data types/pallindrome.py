# Palindrome Checker
# Write a Python program that takes a string input from the user and checks if it is a palindrome (reads the same forwards and backwards, ignoring spaces, punctuation, and case). For example, "Racecar" and "A man a plan a canal Panama" are palindromes. Print "Palindrome" if it is, or "Not a palindrome" if it isn’t.

word = input ("Enter the string you wanna check the pallindrome of : ")

if (word[::-1] == word):
    print ("Yes it is pallindrome !")
else :
    print ("nope it is not .")