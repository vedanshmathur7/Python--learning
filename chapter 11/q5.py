class Vector :
    def __init__(self , x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        result = f"Vector ({self.x + other.x}, {self.y + other.y}, {self.z + other.z})"
        return result

    def __mul__(self, other ):
        result = f"{(self.x * other.x) + (self.y * other.y) + (self.z * other.z) }"
        return result

    # def __str__(self):
        

v1 = Vector(5,9,8)
v2 = Vector(6,8,9)
v3 = Vector(4,9,7)

print (v1+v2)
print (v1*v2)

print (v1+v3)
print (v1*v3)
