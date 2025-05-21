import pygame
import pygame_textinput

pygame.init()
def rysuj_pole_tekstowe(ekran, textinput, events, x=100, y=100, szer=300, wys=40,
                        kolor_tla=(255, 255, 255), kolor_ramki=(200, 200, 200), grubosc_ramki=2):
    """
    Rysuje pole tekstowe na ekranie z tłem, ramką i aktualizowanym tekstem.
     Parametry:
        ekran: powierzchnia Pygame (np. screen)
        textinput: obiekt TextInputVisualizer z pygame_textinput
        events: lista zdarzeń pygame.event.get()
        x, y: pozycja pola tekstowego
        szer, wys: rozmiary pola
        kolor_tla: kolor tła prostokąta
        kolor_ramki: kolor obramowania
        grubosc_ramki: grubość linii obramowania
    """
    # Tło
    pygame.draw.rect(ekran, kolor_tla, (x, y, szer, wys))

    # Obramowanie
    pygame.draw.rect(ekran, kolor_ramki, (x, y, szer, wys), grubosc_ramki)

    # Aktualizacja i rysowanie tekstu
    textinput.update(events)
    ekran.blit(textinput.surface, (x + 5, y + 5))  # +5 to padding od brzegu