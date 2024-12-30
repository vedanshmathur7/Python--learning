def stripu(l, word):
    for i in range (len(l)):
        if (word in l[i]):
            l[i] = l[i].replace(word,"").strip()
    return [item for item in l if item != ""]
    
l = ["Harry", "Rohan", "Mohan", "an"]

print(stripu(l,"an"))

