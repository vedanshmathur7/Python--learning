with open ("log.txt") as f:
    content = f.read()

if ("python" in content):
    print ("the word python is present in the log file.")

else: 
    print ("the word python is not present in the log file.")