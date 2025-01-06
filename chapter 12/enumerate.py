list = [56, 56.7, 390, 349, "Vedansh" , "joy"]

index = 0
for item in list :
    print (f"The item at index {index} is {item}")
    index += 1

#the same can be achieved using enumerate func

for index , item in enumerate (list) :
    # print (f"The item at index {index} is {item}")
    print (index, item)