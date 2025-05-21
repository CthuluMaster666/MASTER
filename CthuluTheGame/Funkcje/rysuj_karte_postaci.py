import pygame

def rysuj_karte_postaci(ekran, postac, tlo):
    ekran.blit(tlo, (0, 0))
    font = pygame.font.Font(None, 36)

    teksty = [
        f"Imię: {postac.imie}",
        f"Siła: {postac.sila.wartosc}",
        f"Zręczność: {postac.zrecznosc.wartosc}",
        f"Inteligencja: {postac.inteligencja.wartosc}",
        f"Charyzma: {postac.charyzma.wartosc}"
    ]

    for i, tekst in enumerate(teksty):
        txt_surface = font.render(tekst, True, (255, 255, 255))
        ekran.blit(txt_surface, (100, 100 + i * 40))

    back_rect = pygame.Rect(20, 20, 120, 40)
    pygame.draw.rect(ekran, (0, 0, 255), back_rect)
    powrot_text = font.render("Powrót", True, (255, 255, 255))
    ekran.blit(powrot_text, (back_rect.x + 15, back_rect.y + 5))

    return back_rect