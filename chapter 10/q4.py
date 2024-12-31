class Calculator:
    def __init__(self, n):
        self.n = n
        
    def square (self):
        print (f"The square of {self.n} is {self.n * self.n}")

    def cube (self):
        print (f"The cube of {self.n} is {self.n * self.n * self.n}")

    def sqroot (self):
        print (f"The square root of {self.n} is {self.n**1/2}")
    
    @staticmethod
    def hello ():
        print ("Ayyooo Whatsuppp Homieeee !!?")
        print ("Your calculations are as follows ...")

a = Calculator(16)
a.hello()
a.sqroot() 
a.square() 
a.cube()
        
