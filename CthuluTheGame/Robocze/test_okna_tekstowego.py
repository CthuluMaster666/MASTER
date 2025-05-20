import pygame_textinput
import pygame
pygame.init()



def proba_wyswietlenia(screen):
# Create TextInput-object
    textinput = pygame_textinput.TextInputVisualizer()


    clock = pygame.time.Clock()

    while True:

        events = pygame.event.get()

        textinput.update(events)

        screen.blit(textinput.surface, (10, 10))

        for event in events:
            if event.type == pygame.QUIT:
                exit()

        pygame.display.update()
        clock.tick(30)

