class Employee :
    salary = 15000
    increment = 20
    
    @property
    def  salaryafterincrement (self):
        return (self.salary + self.salary*(self.increment/100))
    
    @salaryafterincrement.setter    
    def salaryafterincrement (self, salaryafterincrement):
        self.increment = ((salaryafterincrement/self.salary) - 1)*100
    
joy = Employee()
print (joy.salaryafterincrement)
joy.salaryafterincrement = 20000
print (joy.salaryafterincrement)
print (joy.increment)
