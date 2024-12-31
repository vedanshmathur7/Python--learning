class Company:
    salary = 13000
    language = "Java"

op = Company()
op.name = "Vedansh Mathur"
op.language = "python" #preference will be given to instance attributes over class attributes
op.salary = 1200000000

print (op.name, op.salary, op.language)