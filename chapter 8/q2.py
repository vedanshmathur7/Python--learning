
def cel_to_fer (cel):
     return ((9*cel)/5) + 32

a= int (input ("Enter the celsius : "))
b = cel_to_fer(a)

print (f"The conversion of {a}°C in Fehrenheit is {round(b,2)}°F ")