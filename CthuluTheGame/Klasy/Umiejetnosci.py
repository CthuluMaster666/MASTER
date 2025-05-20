import random

# Klasa reprezentująca jedną umiejętność postaci

class Abbility:
    def __init__(self, nazwa, wartosc):
        self.nazwa = nazwa  # Nazwa umiejętności (np. "skradanie")
        self.wartosc = wartosc  # Wartość umiejętności

    def __str__(self):
        # Zwraca czytelną reprezentację umiejętności jako tekst
        return f"{self.nazwa} {self.wartosc}"

    def skillcheck(self):
        # Wykonuje test umiejętności — losuje wartość od 0 do 100
        self.rzut=random.randint(0,100)

        # pomocnicze printy przy sprawdzaniu czy dziala
        #print(self.rzut)
        #print(self.wartosc)

        # Porównuje wynik rzutu do wartości umiejętności
        if self.rzut <= self.wartosc:
            return print("test zdany") #sukces
        else:
            return print("test niezdany") #porażka