class Employee :
    def __init__(self, n ):
        self.n = n
    def __add__(self, num):
        return self.n + num.n
    
a = Employee(100)
b = Employee(200) 
print (a+b)   
