
# Importuje moduł random do losowania wartości umiejętności
import random
# Importuje klasy umiejętności z modułu
from CthuluTheGame.Klasy.Umiejetnosci import *
# Importuje klasę Path do obsługi ścieżek plików w stylu obiektowym
from pathlib import Path


# Definicja klasy reprezentującej postać w grze
class Postac:
    def __init__(self, imie):
        self.imie = imie    # Imię postaci

        # Losowo przypisywane umiejętności z wartością od 1 do 100
        self.sila = Abbility("siła", random.randint(15, 100))
        self.zrecznosc = Abbility("zręczność", random.randint(15, 100))
        self.inteligencja = Abbility("inteligencja", random.randint(15, 100))
        self.charyzma = Abbility("charyzma", random.randint(15, 100))

    @staticmethod
    def z_bazy(rekord):
        p = Postac(rekord[0])
        p.sila.wartosc = rekord[1]
        p.zrecznosc.wartosc = rekord[2]
        p.inteligencja.wartosc = rekord[3]
        p.charyzma.wartosc = rekord[4]
        return p
