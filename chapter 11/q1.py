class TwoDVector:
    def __init__(self , i, j):
        self.i = i
        self.j = j
        # print (f"The Two D vector is {self.i}i + {self.j}j")

class ThreeDVector (TwoDVector) :
    def __init__(self, i , j , k ):
        super().__init__(i,j)
        self.k = k
        print (f"The Three D vctor is {self.i}i + {self.j}j + {self.k}k")

vedansh = TwoDVector(89,89)
joy = ThreeDVector(89,89,89)

