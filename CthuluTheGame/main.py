# Import niezbędnych modułów systemowych i graficznych
import sys                      # Dostęp do funkcji systemowych, np. sys.exit()
import os                       # Operacje na ścieżkach plików i katalogach
import pygame                   # Główna biblioteka do tworzenia gier
import pygame_textinput         # Biblioteka do tworzenia pól tekstowych
from pathlib import Path        # Obsługa ścieżek plików w sposób niezależny od systemu
import sqlite3                  # Moduł do obsługi bazy danych

# Import funkcji i klas z własnych modułów gry
from CthuluTheGame.Funkcje.okna_w_grze import *  # Funkcje do rysowania okien/menu
from CthuluTheGame.Klasy.Postac import *          # Klasy i funkcje związane z postaciami
from CthuluTheGame.Funkcje.rysuj_pole_tekstowe import *  # Funkcje do rysowania pola tekstowego
from CthuluTheGame.Funkcje.tworzenie_postaci_baza import * # Funkcja zapisująca postać do bazy danych
from CthuluTheGame.Funkcje.rysuj_karte_postaci import *    # Funkcja rysująca kartę postaci
from CthuluTheGame.Funkcje.wczytaj_postac_z_bazy import *   # Funkcja wczytująca postać z bazy danych

# Konfiguracja pola tekstowego do wpisywania imienia
textinput = pygame_textinput.TextInputVisualizer()
textinput.font_color = (255, 255, 255)      # Kolor tekstu na biały
textinput.cursor_color = (255, 255, 255)    # Kolor kursora na biały
textinput.font_object = pygame.font.Font(None, 32)  # Ustawienie czcionki i rozmiaru

# Inicjalizacja biblioteki pygame
pygame.init()    # Uruchomienie wszystkich modułów pygame

# Parametry okna gry
szerokosc, wysokosc = 800, 600                             # Ustawienie rozmiaru okna
ekran = pygame.display.set_mode((szerokosc, wysokosc))    # Utworzenie głównego okna gry
pygame.display.set_caption("Cthulhu The Game")            # Ustawienie tytułu okna

# Zmienne globalne i pomocnicze
ekran_aktywny = "menu"             # Aktualnie wyświetlany ekran (menu, tworzenie postaci, itp.)
clock = pygame.time.Clock()        # Zegar do kontrolowania FPS (klatek na sekundę)
textinput = pygame_textinput.TextInputVisualizer()  # Inicjalizacja pola tekstowego ponownie (ew. nadpisanie)

# Wczytanie i przygotowanie grafik tła
lokalizacjagrafik = Path("Grafika")    # Ścieżka do folderu z grafiką

tlo_menu = pygame.transform.scale(     # Wczytanie i skalowanie tła menu do rozmiaru okna
    pygame.image.load(lokalizacjagrafik / "menu.jpg"), (szerokosc, wysokosc)
)
tlo_poziom_tworzenia_postaci = pygame.transform.scale(  # Wczytanie i skalowanie tła ekranu tworzenia postaci
    pygame.image.load(lokalizacjagrafik / "Level1.png"), (szerokosc, wysokosc)
)

# Główna pętla gry – wykonuje się cały czas, dopóki gra jest uruchomiona
while True:
    ekran.fill((0, 0, 0))        # Wyczyść ekran, wypełniając go czarnym kolorem

    events = pygame.event.get()  # Pobierz wszystkie zdarzenia, np. klawiatura, mysz, zamknięcie okna

    # Obsługa zdarzeń
    for event in events:
        if event.type == pygame.QUIT:  # Jeśli użytkownik kliknie "X" w oknie gry
            pygame.quit()               # Zakończ moduły pygame
            sys.exit()                 # Zamknij program
        elif event.type == pygame.MOUSEBUTTONDOWN:  # Obsługa kliknięć myszą
            print(f"Kliknięcie: {event.pos}")       # Wypisanie pozycji kliknięcia do konsoli

            # Logika obsługi kliknięć dla ekranu menu
            if ekran_aktywny == "menu":
                if start_rect.collidepoint(event.pos):  # Kliknięcie na przycisk "Start"
                    ekran_aktywny = "tworzenie_postaci" # Przejście do ekranu tworzenia postaci
                    textinput.value = ""                # Wyczyszczenie pola tekstowego
                elif exit_rect.collidepoint(event.pos): # Kliknięcie na przycisk "Wyjście"
                    pygame.quit()                       # Zamknięcie pygame
                    sys.exit()                         # Zakończenie programu

            # Logika obsługi kliknięć na ekranie tworzenia postaci
            elif ekran_aktywny == "tworzenie_postaci":
                if back_rect.collidepoint(event.pos):    # Kliknięcie na przycisk "Powrót"
                    ekran_aktywny = "menu"               # Powrót do menu
                    textinput.value = ""                 # Wyczyszczenie pola tekstowego
                elif create_character_rect.collidepoint(event.pos):  # Kliknięcie "Stwórz postać"
                    imie = textinput.value.strip()       # Pobranie imienia z pola tekstowego (bez spacji na początku/końcu)
                    if imie:                             # Sprawdzenie, czy imię nie jest puste
                        tworzeniepostaci(imie)          # Zapisanie postaci do bazy danych
                        aktywna_postac = wczytaj_postac_z_bazy(imie)  # Wczytanie postaci z bazy
                        textinput.value = ""             # Wyczyszczenie pola tekstowego
                        print(aktywna_postac)            # Wypisanie danych postaci do konsoli
                    else:
                        print("Podaj imię postaci!")     # Komunikat, jeśli pole jest puste
                elif load_character_rect.collidepoint(event.pos): # Kliknięcie "Wczytaj postać"
                    ekran_aktywny = "wybor_postaci"     # Przejście do ekranu wyboru postaci

            # Logika obsługi kliknięć na ekranie wyboru postaci
            elif ekran_aktywny == "wybor_postaci":
                if back_rect.collidepoint(event.pos):  # Kliknięcie "Powrót"
                    ekran_aktywny = "tworzenie_postaci"  # Powrót do ekranu tworzenia postaci
                else:
                    # Sprawdzenie, czy kliknięto na którąś z postaci w liście
                    for rect, imie in lista_rectow_postaci:
                        if rect.collidepoint(event.pos):
                            aktywna_postac = wczytaj_postac_z_bazy(imie[0])  # Wczytanie wybranej postaci
                            ekran_aktywny = "karta_postaci"                   # Przejście do ekranu karty postaci
                            print(aktywna_postac.zrecznosc.skillcheck())

            # Logika obsługi kliknięć na ekranie karty postaci
            elif ekran_aktywny == "karta_postaci":
                if back_rect_karty.collidepoint(event.pos):  # Kliknięcie "Powrót" na karcie postaci
                    ekran_aktywny = "wybor_postaci"           # Powrót do ekranu wyboru postaci

                    #TODO Domyślnie można później dodać przejście do gry

    # Rysowanie odpowiedniego ekranu gry w zależności od aktualnego stanu
    if ekran_aktywny == "menu":
        rysuj_menu(tlo_menu)    # Rysowanie tła i elementów menu
    elif ekran_aktywny == "tworzenie_postaci":
        rysuj_ekran_tworzenia_postaci(tlo_poziom_tworzenia_postaci)  # Rysowanie tła i elementów tworzenia postaci
        rysuj_pole_tekstowe(ekran, textinput, events, x=100, y=100) # Rysowanie pola tekstowego na ekranie
    elif ekran_aktywny == "wybor_postaci":
        lista_rectow_postaci = rysuj_ekran_wyboru_postaci(tlo_poziom_tworzenia_postaci)    # Rysowanie ekranu wyboru postaci i pobranie listy prostokątów
    elif ekran_aktywny == "karta_postaci" and aktywna_postac:
        back_rect_karty = rysuj_karte_postaci(ekran, aktywna_postac, tlo_poziom_tworzenia_postaci)  # Rysowanie karty postaci i przycisku powrotu

    pygame.display.update()    # Aktualizacja całego ekranu po narysowaniu wszystkich elementów
    clock.tick(30)             # Ustawienie limitu do 30 klatek na sekundę (FPS)
