from types import new_class
from unittest import case
import random
from Umiejetnosci import *

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
lokalizacjapostaci="Postacie/"

try:
    with open(lokalizacjapostaci+gracz.imie, "x") as f:
        f.writelines(gracz.__str__())
except FileExistsError:
    print("postac o takim imieniu juz istnieje")

gracz.skradanie.skillcheck()
gracz.perswazja.skillcheck()