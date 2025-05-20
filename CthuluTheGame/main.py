# Import niezbędnych modułów systemowych i graficznych
import sys                      # Dostęp do funkcji systemowych, np. sys.exit()
import os                       # Operacje na ścieżkach plików i katalogach
import pygame                   # Główna biblioteka do tworzenia gier
import pygame_textinput         # Biblioteka do tworzenia pól tekstowych
from pathlib import Path        # Obsługa ścieżek plików w sposób niezależny od systemu

# Import funkcji i klas z własnych modułów gry
from CthuluTheGame.Funkcje.okna_w_grze import *  # Funkcje do rysowania okien/menu
from CthuluTheGame.Klasy.Postacie import *       # Klasy i funkcje związane z postaciami

# --- Inicjalizacja ---
pygame.init()                   # Inicjalizacja wszystkich modułów pygame

# --- Parametry okna ---
szerokosc, wysokosc = 800, 600                             # Rozmiar okna gry
ekran = pygame.display.set_mode((szerokosc, wysokosc))    # Tworzenie głównego okna gry
pygame.display.set_caption("Cthulhu The Game")            # Ustawienie tytułu okna gry

# --- Zmienne globalne ---
ekran_aktywny = "menu"             # Zmienna przechowująca informację o aktualnym ekranie gry
clock = pygame.time.Clock()        # Zegar do kontrolowania liczby klatek na sekundę
textinput = pygame_textinput.TextInputVisualizer()  # Inicjalizacja pola tekstowego do wpisania imienia

# --- Wczytaj tła ---
lokalizacjagrafik = Path("Grafika")    # Ścieżka do folderu z grafiką
tlo_menu = pygame.transform.scale(     # Wczytanie i skalowanie tła menu
    pygame.image.load(lokalizacjagrafik / "menu.jpg"), (szerokosc, wysokosc)
)
tlo_poziom_tworzenia_postaci = pygame.transform.scale(  # Wczytanie i skalowanie tła ekranu tworzenia postaci
    pygame.image.load(lokalizacjagrafik / "Level1.png"), (szerokosc, wysokosc)
)

# --- Główna pętla gry ---
while True:
    ekran.fill((0, 0, 0))        # Wypełnienie ekranu kolorem czarnym, aby go wyczyścić

    events = pygame.event.get() # Pobranie wszystkich zdarzeń z kolejki Pygame

    # Obsługa zdarzeń (np. kliknięcia, zamknięcie okna)
    for event in events:
        if event.type == pygame.QUIT:  # Jeśli użytkownik kliknie "X", zamknij grę
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:  # Obsługa kliknięcia myszą
            print(f"Kliknięcie: {event.pos}")       # Wypisanie pozycji kliknięcia do konsoli

            # Logika dla ekranu menu
            if ekran_aktywny == "menu":
                if start_rect.collidepoint(event.pos):  # Jeśli kliknięto przycisk "Start"
                    ekran_aktywny = "tworzenie_postaci" # Przejdź do ekranu tworzenia postaci
                    textinput.value = ""                # Wyczyszczenie pola tekstowego
                elif exit_rect.collidepoint(event.pos): # Jeśli kliknięto przycisk "Wyjście"
                    pygame.quit()
                    sys.exit()

            # Logika dla ekranu tworzenia postaci
            elif ekran_aktywny == "tworzenie_postaci":
                if back_rect.collidepoint(event.pos):    # Jeśli kliknięto "Powrót"
                    ekran_aktywny = "menu"               # Przejdź do menu
                    textinput.value = ""                 # Wyczyszczenie pola tekstowego
                elif create_character_rect.collidepoint(event.pos):  # Jeśli kliknięto "Stwórz postać"
                    imie = textinput.value.strip()       # Pobierz imię z pola tekstowego
                    if imie:                             # Sprawdź, czy imię nie jest puste
                        tworzeniepostaci(imie)           # Utwórz postać z podanym imieniem
                        textinput.value = ""             # Wyczyszczenie pola po stworzeniu postaci
                    else:
                        print("Podaj imię postaci!")     # Informacja zwrotna w konsoli

    # --- Rysowanie odpowiedniego ekranu ---
    if ekran_aktywny == "menu":
        rysuj_menu(tlo_menu)    # Narysuj tło i elementy menu

    elif ekran_aktywny == "tworzenie_postaci":
        rysuj_ekran_postaci(tlo_poziom_tworzenia_postaci)  # Narysuj tło i elementy tworzenia postaci
        textinput.update(events)            # Aktualizuj zawartość pola tekstowego
        ekran.blit(textinput.surface, (100, 100))  # Narysuj pole tekstowe na ekranie

    pygame.display.update()    # Aktualizacja całego ekranu
    clock.tick(30)             # Ograniczenie pętli do 30 klatek na sekundę