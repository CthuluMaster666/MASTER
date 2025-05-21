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
#tworzeniepostaci("test")