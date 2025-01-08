def op():
    try : 
      a = int (input ("Enter the no. : "))

    except Exception as e:
      print (e)

    finally : 
      print ("Its done now !") #it is used to print the statement as final even without calling .
        # if something else was used ... we had to call the same 
op()