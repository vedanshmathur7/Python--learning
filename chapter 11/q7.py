class Len :
    def __init__(self, l):
        self.l = l

    def __len__(self):
        return len (self.l)
    
op = Len([1, 4, 67, "Vedansh", 90, 100, 27637])
print (len(op))