
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
        self.skradanie = Abbility("skradanie", random.randint(1, 100))
        self.atletyka = Abbility("atletyka", random.randint(1, 100))
        self.perswazja = Abbility("perswazja", random.randint(1, 100))

    def __str__(self):
        # Zwraca reprezentację postaci jako jeden ciąg tekstu (dla zapisu do pliku)
        return f"{self.imie} {self.skradanie} {self.atletyka} {self.perswazja}"

# Funkcja tworząca nową postać i zapisująca ją do pliku
def tworzeniepostaci(imiepostaci):

    # Ustal ścieżkę katalogu o poziom wyżej niż plik z tym kodem
    parent = Path(__file__).parent.parent

    # Dodaj do niej katalog "Postacie", w którym będą zapisywane dane postaci
    lokalizacjapostaci = parent / "Postacie"

    # Utwórz katalog "Postacie" w głównej lokalizacji, jeśli nie istnieje
    lokalizacjapostaci.mkdir(parents=True, exist_ok=True)

    # Stwórz nową postać z podanym imieniem
    gracz = Postac(imiepostaci)

    # Ustal pełną ścieżkę do pliku, w którym zapiszesz postać
    lokalizacjapliku = lokalizacjapostaci/f"{gracz.imie}.txt"


    try:
        # Otwórz plik do zapisu, ale tylko jeśli jeszcze nie istnieje ("x")
        with open(lokalizacjapliku, "x") as f:
            # Zapisz dane postaci jako tekst
            f.writelines(str(gracz))
    except FileExistsError:
        # Jeśli plik już istnieje, wyświetl komunikat
        print("postac o takim imieniu juz istnieje")

# Wywołanie funkcji do testu — tworzy postać o imieniu "test"
tworzeniepostaci("test")
