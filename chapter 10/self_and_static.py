class Company :
    salary = 120000
    language = "Python"

    def getinfo(self):
        print (f"The salary is {self.salary} and language is {self.language} ")
        
    @staticmethod
    def opchappal():
        print ("Good Morning")

naam = Company()
naam.name = "Vedansh Mathur"
naam.opchappal()
naam.getinfo()