word = "Donkey"

with open ("file.txt", "r") as f:
    content = f.read()

newcontent = content.replace(word, (len(word) * "*"))

with open ("file.txt", "w") as f:
    f.write (newcontent)