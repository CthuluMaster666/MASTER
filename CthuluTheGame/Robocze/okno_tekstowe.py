import pygame_textinput
import pygame



def okno_tekstowe(textinput,screen,clock,ekran_aktywny,back_rect):
    pygame.init()

    dalej= True
    while dalej==True:

        events = pygame.event.get()

    # Feed it with events every frame

    # Blit its surface onto the scree
        screen.blit(textinput.surface, (100, 100))
        for event in pygame.event.get():
            textinput.update(events)
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_rect.collidepoint(event.pos):
                    ekran_aktywny = "menu"
                    dalej=False
                    pygame.display.update()
                    print(ekran_aktywny)
        pygame.display.update()
        clock.tick(30)