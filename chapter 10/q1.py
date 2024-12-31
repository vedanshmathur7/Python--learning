class Programmer :
    company = "Microsoft"
    def __init__(self, name , salary, pincode, jobTitle):
        self.name = name 
        self.salary = salary 
        self.pincode = pincode  
        self.jobTitle = jobTitle 

Rajesh = Programmer("Rajesh", "25,00,000", 302019, "chor")
print (f"Rajesh works in {Rajesh.company}, as {Rajesh.jobTitle}. His salary is {Rajesh.salary}. His pincode is {Rajesh.pincode}  ")

        
Vedansh = Programmer("Vedansh", "1,00,00,000", 302019, "CEO")
print (f"Vedansh works in {Vedansh.company}, as {Vedansh.jobTitle}. His salary is {Vedansh.salary}. His pincode is {Vedansh.pincode}  ")

        
Joy = Programmer("Joy", "25,00,000", 302019, "Influencer")
print (f"Joy works in {Joy.company}, as an {Joy.jobTitle}. His salary is {Joy.salary}. His pincode is {Joy.pincode}  ")

        