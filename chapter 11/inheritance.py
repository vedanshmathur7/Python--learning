class Employee:
    company = "Microsoft"
    def show (self): 
        print (f"The name of person is {self.name} and the salary is {self.salary}")

    def salary (self, name , salary):
        self.name = name
        self.salary = salary


class Programmer (Employee):
    company = "Apple"


vedansh = Programmer()
print (vedansh.company)

vedansh.salary("Chitranshu Mathur", "36LPA" )
vedansh.show()

chitranshu = Employee()
print (chitranshu.company)