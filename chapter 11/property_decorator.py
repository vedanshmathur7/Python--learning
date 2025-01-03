class Employee:
    
    @property
    def name (self):
        return f"{self.fname} {self.lname}"
    
    @name.setter 
    def name (self, value):
        self.fname = value.split (" ")[0]
        self.lname = value.split (" ")[1]

vedansh = Employee()
vedansh.name = "Vedansh Mathur"
print (vedansh.fname)
print (vedansh.lname)

