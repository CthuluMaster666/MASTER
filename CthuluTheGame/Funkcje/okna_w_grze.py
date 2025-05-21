from pygame_textinput import TextInputVisualizer  # Import klasy do wizualizacji pola tekstowego

# Importy własnych modułów gry
from CthuluTheGame.Robocze.okno_tekstowe import *  # Funkcje związane z wyświetlaniem okna tekstowego
from CthuluTheGame.baza import pobierz_postacie     # Funkcja do pobierania postaci z bazy danych

pygame.init()  # Inicjalizacja wszystkich modułów pygame

# Ustawienia rozmiaru okna gry
szerokosc, wysokosc = 800, 600
ekran = pygame.display.set_mode((szerokosc, wysokosc))  # Utworzenie głównego okna gry
pygame.display.set_caption("Menu Główne Gry")           # Ustawienie tytułu okna

# Definicje kolorów RGB
bialy = (255, 255, 255)
niebieski = (0, 120, 255)
czarny = (0, 0, 0)

# Inicjalizacja czcionki
czcionka = pygame.font.SysFont("arial", 50)

# Przygotowanie tekstów do przycisków
start_text = czcionka.render("START", True, bialy)
opcje_text = czcionka.render("OPCJE", True, bialy)
exit_text = czcionka.render("WYJŚCIE", True, bialy)
powrot_text = czcionka.render("COFNIJ", True, bialy)
stworz_postac_text = czcionka.render("Stwórz Postać", True, bialy)
wczytaj_postac_text = czcionka.render("Wczytaj Postać", True, bialy)

# Definicje prostokątów reprezentujących interaktywne przyciski
start_rect = pygame.Rect(200, 200, 400, 60)
options_rect = pygame.Rect(200, 300, 400, 60)
create_character_rect = pygame.Rect(10, 400, 380, 60)
load_character_rect = pygame.Rect(410, 400, 380, 60)
exit_rect = pygame.Rect(200, 400, 400, 60)
back_rect = pygame.Rect(200, 500, 400, 60)

# Inicjalizacja pola tekstowego
textinput = TextInputVisualizer()
clock = pygame.time.Clock()
pygame.key.set_repeat(200, 25)  # Ustawienie powtarzania klawiszy (200 ms opóźnienia, co 25 ms powtarzanie)

# Funkcja rysująca ekran głównego menu
def rysuj_menu(tlo_menu):
    ekran.blit(tlo_menu, (0, 0))  # Ustawienie tła
    pygame.draw.rect(ekran, niebieski, start_rect)  # Rysowanie przycisku START
    pygame.draw.rect(ekran, niebieski, options_rect) #Rysowanie przycisku OPCJE
    pygame.draw.rect(ekran, niebieski, exit_rect)   # Rysowanie przycisku EXIT
    ekran.blit(start_text, (start_rect.x + 15, start_rect.y + 5))  # Wyświetlenie tekstu START
    ekran.blit(opcje_text, (options_rect.x + 15, options_rect.y + 5))  #Wyświetlanie tekstu OPCJE
    ekran.blit(exit_text, (exit_rect.x + 15, exit_rect.y + 5))     # Wyświetlenie tekstu EXIT

# Funkcja rysująca ekran tworzenia postaci
def rysuj_ekran_tworzenia_postaci(tlo_poziomu):
    ekran.blit(tlo_poziomu, (0, 0))  # Ustawienie tła ekranu

    # Rysowanie przycisku "Stwórz postać"
    pygame.draw.rect(ekran, niebieski, create_character_rect)
    ekran.blit(stworz_postac_text, (create_character_rect.x + 15, create_character_rect.y + 5))

    # Rysowanie przycisku "Wczytaj postać"
    pygame.draw.rect(ekran, niebieski, load_character_rect)
    ekran.blit(wczytaj_postac_text, (load_character_rect.x + 15, load_character_rect.y + 5))

    # Rysowanie przycisku "Powrót"
    pygame.draw.rect(ekran, niebieski, back_rect)
    ekran.blit(powrot_text, (back_rect.x + 15, back_rect.y + 5))

    pygame.display.update()  # Aktualizacja ekranu

# Funkcja rysująca ekran wyboru postaci z bazy
def rysuj_ekran_wyboru_postaci(tlo_poziomu):
    ekran.blit(tlo_poziomu, (0, 0))  # Ustawienie tła

    postacie = pobierz_postacie()  # Pobranie listy postaci z bazy danych
    lista_rectow = []              # Lista przechowująca prostokąty (przyciski) i odpowiadające im postacie

    czcionka = pygame.font.SysFont("arial", 32)  # Czcionka do imion postaci
    odstep_y = 70  # Odstęp pionowy między przyciskami

    for i, postac in enumerate(postacie):
        imie = postac[0]  # Pobranie imienia postaci

        # Utworzenie prostokąta dla danego imienia
        rect = pygame.Rect(100, 100 + i * odstep_y, 300, 50)
        pygame.draw.rect(ekran, (50, 50, 50), rect)       # Tło przycisku
        pygame.draw.rect(ekran, (200, 200, 200), rect, 2) # Obramowanie przycisku

        tekst = czcionka.render(imie, True, czarny)       # Renderowanie tekstu z imieniem
        ekran.blit(tekst, (rect.x + 10, rect.y + 10))     # Wyświetlenie imienia na przycisku

        lista_rectow.append((rect, postac))  # Dodanie przycisku i danych postaci do listy

    # Rysowanie przycisku "Powrót"
    pygame.draw.rect(ekran, niebieski, back_rect)
    ekran.blit(powrot_text, (back_rect.x + 15, back_rect.y + 5))

    pygame.display.update()  # Aktualizacja ekranu

    return lista_rectow  # Zwrócenie listy przycisków z postaciami