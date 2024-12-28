def inch_to_cm(inch):
    to_cm = inch * 2.54
    return to_cm

a = int (input("Enter inches to be converted in centimeters : "))

print (f"The value of {a} inches in centimeters is {inch_to_cm(a)} cm.")
    