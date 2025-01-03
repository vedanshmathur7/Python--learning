class Employee:
    company = "Microsoft"
    def show (self, name):
        self.name = name
        print (f"The name of company is {self.company} and the person who works here is {self.name}")


class Code (Employee)  : 
    language = "Python"
    def lang (self):
        print (f"The default language is {self.language}, of the person named {self.name} ")

class Salary (Code) :
    salary = 1250000
    def sal(self):
        print (f"The salary of {self.name} is {self.salary}")


joy = Salary()
joy.show("Chitranshu Mathur")
joy.lang()
joy.sal()