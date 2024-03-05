import pygame
import sys
import button_class
import screen_resolution
import game_window
import avtory_window

pygame.init()

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
button_start_game = button_class.button("Начать игру", 40, 400, 100, WHITE, 300, 300)
button_avtory = button_class.button("Авторы",40,400,100, WHITE, 300, 500)
buttun_quit = button_class.button("Выход",40,400,100, WHITE, 300, 700)

def main_window_start():
    screen_resol = screen_resolution.choose_resolution()
    screen = pygame.display.set_mode(screen_resol, pygame.FULLSCREEN)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))

        mouse_pos = pygame.mouse.get_pos()
        x, y = mouse_pos

        button_start_game.draw(screen)
        button_avtory.draw(screen)
        buttun_quit.draw(screen)

        button_start_game.blackout_and_click(x,y,WHITE,start_game)
        button_avtory.blackout_and_click(x,y,WHITE,razraby_ne_dauni)
        buttun_quit.blackout_and_click(x,y,WHITE,quit)

        pygame.display.flip()
    pygame.quit()
    sys.exit()

def quit():
    pygame.quit()
    sys.exit()

def start_game():

    game_window.game_window_start()
    pygame.quit()

def razraby_ne_dauni():
    avtory_window.avtors_window_start()
    pygame.quit()




