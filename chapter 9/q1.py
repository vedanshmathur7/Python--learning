f = open ("poem.txt")

check = f.read()
if ("Twinkle" in check):
    print("Twinkle is present in the text")

else :
    print("Twinkle is not present in the text")