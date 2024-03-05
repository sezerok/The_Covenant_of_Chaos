import pygame
import button_class
import screen_resolution
import gamer


pygame.init()


def game_window_start():
    screen_resol = screen_resolution.choose_resolution()
    screen = pygame.display.set_mode(screen_resol, pygame.FULLSCREEN)
    running=True
    screen.fill((198, 50, 100))
    g = gamer.Gamer(200, 200, 200, 200,screen)
    while running:
        for event in pygame.event.get():
            screen.fill((198, 50, 100))
            g.move(event,screen.fill)
            g.draw()



            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running=False




        pygame.display.flip()