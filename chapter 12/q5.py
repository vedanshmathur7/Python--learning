n = int (input("Enter the no. : "))

table = [n*i for i in range (1, 11)]
with open ("tables.txt" , "a") as f : #appending 
    f.write(f"The table for {n} is : {str(table)} \n")