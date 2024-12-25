d = {} #empty dict declared 
print(type(d))

champal = {
    "marks" : 89,
    "namak" : "sahi hai ",
    777 : "lucky no."
}

print (champal, type(champal))

print (champal["namak"])
print (champal.items ()) #prints all the items present 
print (champal.keys()) #all the keys 
print (champal.values()) #all the values of the keys

champal.update({"namak" : "namak haram", "vedansh" : "kaam 25"})
#updates and even adds new key with value

print(champal.get("namak")) #prints none if no key found
print (champal["namak"]) #throws a keyerror no key found
print (champal.popitem()) #prints the last inserted key-value pair as a tuple
print (champal.pop("marks"))

print("chappppppppppppp")
print (len(champal))
print("chappppppppppppp")

print(champal)

rajesh = champal.copy()

champal.clear()
print(champal)
print(rajesh)


