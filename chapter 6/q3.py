p1 = "make a lot money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

comment = input("Enter the comment : ")

if (p1 in comment or p2 in comment or p3 in comment or p4 in comment):
    print ("the comment is spam. ")

else:
    print("the comment is not spam. ")