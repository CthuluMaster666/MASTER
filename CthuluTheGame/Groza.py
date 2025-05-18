import pygame
import sys

pygame.init()

# Rozmiar okna
szerokosc, wysokosc = 800, 600
ekran = pygame.display.set_mode((szerokosc, wysokosc))
pygame.display.set_caption("Menu Główne Gry")

# Tło
tlo = pygame.image.load("CTHULU.jpg")
tlo = pygame.transform.scale(tlo, (szerokosc, wysokosc))
tlo_poziom1 = pygame.image.load("Level1.png")
tlo_poziom1 = pygame.transform.scale(tlo_poziom1, (szerokosc, wysokosc))

# Kolory
bialy = (255, 255, 255)
niebieski = (0, 120, 255)

# Czcionka
czcionka = pygame.font.SysFont("arial", 50)

# Teksty
start_text = czcionka.render("START GAME", True, bialy)
exit_text = czcionka.render("EXIT", True, bialy)
powrot_text = czcionka.render("BACK", True, bialy)

# Pozycje przycisków
start_rect = pygame.Rect(200, 200, 400, 60)
exit_rect = pygame.Rect(200, 300, 400, 60)
back_rect = pygame.Rect(200, 500, 400, 60)

# Stan gry
ekran_aktywny = "menu"  # "menu" lub "gra"

def rysuj_menu():
    ekran.blit(tlo, (0, 0))
    pygame.draw.rect(ekran, niebieski, start_rect)
    pygame.draw.rect(ekran, niebieski, exit_rect)
    ekran.blit(start_text, (start_rect.x + 15, start_rect.y + 5))
    ekran.blit(exit_text, (exit_rect.x + 15, exit_rect.y + 5))
    pygame.display.flip()

def rysuj_poziom(tekst, tlo_poziomu):
    ekran.blit(tlo_poziomu, (0, 0))
    tekst_poziomu = czcionka.render(tekst, True, bialy)
    ekran.blit(tekst_poziomu, (200, 200))
    pygame.draw.rect(ekran, niebieski, back_rect)
    ekran.blit(powrot_text, (back_rect.x + 15, back_rect.y + 5))
    pygame.display.flip()

# Główna pętla
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if ekran_aktywny == "menu":
                if start_rect.collidepoint(event.pos):
                    print("Przejście do gry...")
                    ekran_aktywny = "gra"
                elif exit_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
            elif ekran_aktywny == "gra":
                if back_rect.collidepoint(event.pos):
                    print("Powrót do menu...")
                    ekran_aktywny = "menu"

    if ekran_aktywny == "menu":
        rysuj_menu()
    elif ekran_aktywny == "gra":
        rysuj_poziom("Umarłeś chuju niemyty", tlo_poziom1)
