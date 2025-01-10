from functools import reduce

greater = lambda x,y: x if x>y else y

l = [12, 344, 7574, 74, 8347, 948, 875]

op = reduce (greater , l) #no need to write list outside
print (op)