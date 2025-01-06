list1 = ["rajesh", "vedansh", "tejaswi"]
list2 = [ item for item in list1 if item == "tejaswi" ]

print (list2) #prints ['tejaswi']

l1 = [1, 5, 6, 4, 7]
l2 = [i*i for i in l1 ]

print (f"The squared items of {l1} are {l2}")