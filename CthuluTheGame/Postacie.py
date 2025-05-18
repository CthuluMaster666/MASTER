from types import new_class
from unittest import case
import random

def number_to_string(b):
    match b:
        case 0:
            return "zero"
        case 1 :
            return "one"
        case 2 :
            return "two"
        case _:
            return "default"




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



class Postac :
    def __init__(self, imie):
        self.imie = imie
        self.skradanie = Abbility("skradanie",random.randint(1,100))
        self.atletyka = Abbility("atletyka",random.randint(1,100))
        self.perswazja = Abbility("perswazja",random.randint(1,100))
    def __str__(self):
        return f"{self.imie} {self.skradanie} {self.atletyka} {self.perswazja}"


imiepostaci = input("podaj imie postaci ")
gracz = Postac(imiepostaci)
#postac2 = Postac(imie="Marzenka")
#postac3 = Postac(imie="Karol")

print(gracz)
#print(postac2)
#print(postac3)

#print(gracz.skradanie.wartosc)


try:
    with open(gracz.imie, "x") as f:
        f.writelines(gracz.__str__())
except FileExistsError:
    print("postac o takim imieniu juz istnieje")

gracz.skradanie.skillcheck()
gracz.perswazja.skillcheck()