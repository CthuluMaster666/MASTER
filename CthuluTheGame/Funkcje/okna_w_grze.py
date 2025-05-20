from pygame_textinput import TextInputVisualizer
from CthuluTheGame.Robocze.okno_tekstowe import *

pygame.init()

# Rozmiar okna
szerokosc, wysokosc = 800, 600
ekran = pygame.display.set_mode((szerokosc, wysokosc))
pygame.display.set_caption("Menu Główne Gry")


# Kolory
bialy = (255, 255, 255)
niebieski = (0, 120, 255)

# Czcionka
czcionka = pygame.font.SysFont("arial", 50)

# Teksty
start_text = czcionka.render("START GAME", True, bialy)
exit_text = czcionka.render("EXIT", True, bialy)
powrot_text = czcionka.render("BACK", True, bialy)
stworz_postac_text = czcionka.render("Stwórz Postać", True, bialy)

# Pozycje przycisków
start_rect = pygame.Rect(200, 200, 400, 60)
create_character_rect = pygame.Rect(200, 400, 400, 60)
exit_rect = pygame.Rect(200, 300, 400, 60)
back_rect = pygame.Rect(200, 500, 400, 60)

#TextInput objekt
textinput=TextInputVisualizer()
clock=pygame.time.Clock()
pygame.key.set_repeat(200,25)

def rysuj_menu(tlo_menu):
    ekran.blit(tlo_menu, (0, 0))
    pygame.draw.rect(ekran, niebieski, start_rect)
    pygame.draw.rect(ekran, niebieski, exit_rect)
    ekran.blit(start_text, (start_rect.x + 15, start_rect.y + 5))
    ekran.blit(exit_text, (exit_rect.x + 15, exit_rect.y + 5))


def rysuj_ekran_postaci(tlo_poziomu):

    ekran.blit(tlo_poziomu, (0, 0))
    pygame.draw.rect(ekran, niebieski, back_rect)
    pygame.draw.rect(ekran, niebieski, create_character_rect)
    ekran.blit(stworz_postac_text,(create_character_rect.x +15, create_character_rect.y + 5))
    ekran.blit(powrot_text, (back_rect.x + 15, back_rect.y + 5))
    pygame.display.update()


