from random import randint

class Train :
    def __init__ (self, trainNo):
        self.trainNo = trainNo

    def getfare (self):
        print (f"The fare of the trip is ₹{randint(222, 100000)}")

    def book (self, fro, to):
        self.fro = fro
        self.to = to
        print (f"The train booking is from {self.fro} to {self.to}.")

    def status (self):
        print (f"The running status of the train no.: {self.trainNo} is 5 min delay by the actual time.")


passenger = Train (122456)
passenger.book("Jaipur", "Jhalawar")
passenger.getfare()
passenger.status()


