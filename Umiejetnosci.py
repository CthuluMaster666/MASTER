import random

class Abbility:
    def __init__(self, nazwa, wartosc):
        self.nazwa = nazwa
        self.wartosc = wartosc
    def __str__(self):
        return f"{self.nazwa} {self.wartosc}"
    def skillcheck(self):
        self.rzut=random.randint(0,100)
        #print(self.rzut)
        #print(self.wartosc)
        if self.rzut <= self.wartosc:
            return print("test zdany")
        else:
            return print("test niezdany")