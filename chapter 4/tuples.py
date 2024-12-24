kamlesh = () #an empty tuple 
kamlesh = (1,) #tuple with only 1 element
rajesh = (1)
print(type(rajesh)) #will be considered as int 
print(type(kamlesh)) #will be considered as a tuple of 1 element 


op = (56, 78, 78, 89.67, 78, "Vedansh", False)
topi = (56, 78, 78, 89.67, 78)

print(op.count(78))
print(op.index(78))

print(len(op)) #no. of elements
print(max(topi)) #only applicable when int/float type elements
print(min(topi)) 
print(sum(topi))
print(sorted(topi))