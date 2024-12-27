marks1 = int (input("Enter your marks out of 100, in sub 1 : "))
marks2 = int (input("Enter your marks out of 100, in sub 2 : "))
marks3 = int (input("Enter your marks out of 100, in sub 3 : "))

total_percentage = 100*((marks1 + marks2 + marks3)/300)

if (total_percentage>=40 and marks1>= 33 and marks2>= 33 and marks3>= 33):
    print ("You are passed with",total_percentage)

else :
    print ("Bhaad m jaa !")