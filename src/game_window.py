import pygame
import button_class
import screen_resolution


pygame.init()


def game_window_start():
    screen_resol = screen_resolution.choose_resolution()
    screen = pygame.display.set_mode(screen_resol, pygame.FULLSCREEN)
    running=True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((198, 50, 100))
        pygame.display.flip()