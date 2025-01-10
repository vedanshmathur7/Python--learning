from functools import reduce

#Map example
l = [1, 4, 6, 2, 64]

square = lambda x: x*x
print (list(map(square, l)))


#Filter example
def even (n):
    if (n%2 == 0):
        return True
    return False

onlyeven = filter (even, l)
print (list (onlyeven))


sum = lambda x,y : x+y
multi = lambda x,y : x*y

print (reduce(sum, l))
print (reduce(multi, l))

