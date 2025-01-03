class Employee:
    company = "Microsoft"
    
    @classmethod #without this ... it will print apple ; instance attribute
    def show(cls):
        print(f"The name of company is {cls.company}")
               
vedansh = Employee()
vedansh.company = "Apple"
vedansh.show()