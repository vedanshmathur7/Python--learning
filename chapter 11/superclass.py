class Employee:
    def __init__(self):
        print("Hello bhai")

class Programmer(Employee):
    def __init__(self):
        super().__init__()
        print("Khelo INDIA")

class Vedansh(Programmer):
    def __init__(self):
        super().__init__()
        print("Mera desh mahaan !")

    def haal_gabru_da(self):
        print("Haal gabru da poochhta sahi")

op = Vedansh()
op.haal_gabru_da()