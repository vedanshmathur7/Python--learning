s1 = {98, 56, 76, 1, 23, "vedansh"}
s2 = {98, 76, 74, 87, 5367, "vedansh"}

print (s1.union(s2))
print (s1.intersection(s2))
print (s1-s2)
print (s2-s1)

print ({98, 1, 76}.issubset(s1))
print ({98, 1, 76}.issubset(s2))