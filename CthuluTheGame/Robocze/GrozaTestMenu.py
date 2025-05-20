import pygame
import sys

pygame.init()

# Rozmiar okna
szerokosc, wysokosc = 800, 600
ekran = pygame.display.set_mode((szerokosc, wysokosc))
pygame.display.set_caption("Menu Główne Gry")

tlo = pygame.image.load("../Grafika/menu.jpg")
tlo = pygame.transform.scale(tlo, (szerokosc, wysokosc))

# Kolory
bialy = (255, 255, 255)
czarny = (0, 0, 0)
niebieski = (0, 120, 255)

# Czcionka
czcionka = pygame.font.SysFont("arial", 50)

# Teksty
start_text = czcionka.render("START GAME", True, bialy)
exit_text = czcionka.render("EXIT", True, bialy)

# Pozycje przycisków
start_rect = pygame.Rect(200, 200, 400, 60)
exit_rect = pygame.Rect(200, 300, 400, 60)

def rysuj_menu():
    ekran.blit(tlo, (0, 0))  # Najpierw rysujemy tło
    pygame.draw.rect(ekran, niebieski, start_rect)
    pygame.draw.rect(ekran, niebieski, exit_rect)
    ekran.blit(start_text, (start_rect.x + 15, start_rect.y + 5))
    ekran.blit(exit_text, (exit_rect.x + 15, exit_rect.y + 5))
    pygame.display.flip()

def rysuj_LV():
    ekran.blit(tlo, (2, 2))  # Najpierw rysujemy tło
    pygame.draw.rect(ekran, niebieski, start_rect)
    pygame.draw.rect(ekran, niebieski, exit_rect)
    ekran.blit(start_text, (start_rect.x + 15, start_rect.y + 5))
    ekran.blit(exit_text, (exit_rect.x + 15, exit_rect.y + 5))
    pygame.display.flip()

# Pętla menu
while True:
    rysuj_menu()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if start_rect.collidepoint(event.pos):
                print("Gra startuje...")
                # Tutaj możesz załadować poziom gry
            elif exit_rect.collidepoint(event.pos):
                pygame.quit()
                sys.exit()