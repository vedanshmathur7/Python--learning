rajesh = [56, 89, "Vedansh", False, 65.63]

print(rajesh)
rajesh.append(78) #adds at the end
print(rajesh)
rajesh.pop(2) #element is removed according to order
print(rajesh)

rajesh.sort() #sets A.T. alphabetical order
print(rajesh)

rajesh.reverse()
print(rajesh)


rajesh.remove(rajesh[2]) ##element is removed according to data value
print(rajesh)

rajesh.insert(2, False) #adds False at the index 2
print(rajesh)

rajesh.insert(4, 69696) #adds 69696 at the index 4
print(rajesh)