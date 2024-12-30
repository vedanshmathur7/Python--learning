a= '''
Vedansh Mathur loves Tejaswi Khandelwal !
so this is my story 
that has started now !!
and will never end i guess ;)
'''

f = open ("myfiles.txt" , "a") #a is for appending / adding
for i in range (100):
    f.write (a)



f.close ()