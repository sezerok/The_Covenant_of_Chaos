import pygame
from sys import exit
from levels.settings import *
from levels.level import Level
from src.levels.main_window import Main_Window
from src.levels.buttons import *

# TODO: минимизировать глобальные переменные (требование не засорять глоб. обл. видимости)

def main():
    pygame.init()

    screen = pygame.display.set_mode((screen_width, screen_height))

    pygame.display.set_caption("TheCovenantOfChaos")

    clock = pygame.time.Clock()

    main_win = Main_Window(screen)


    # TODO: меню входа
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: #типо паузы(недоработанно)
                    main_win.esc()

        # TODO: установка фона + смена уровня
        screen.fill('black')

        main_win.run() #загрузка главного меню



        pygame.display.update()
        clock.tick(60) # fps control

main()


