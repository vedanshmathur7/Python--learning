class Op :
    a = 3

o = Op()
print (o.a) #prints the class attribute until the instance attribute is assigned. 
o.a = 4 
print (o.a) # prints the instance attribute.
print (Op.a) #but the default attribute is class only
