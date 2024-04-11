from sys import exit
from src.properties.settings import *
from src.properties.windowmanager import WindowManager
from src.properties.buttons import *


def main():
    pygame.init()

    screen = pygame.display.set_mode((screen_width, screen_height))
    main_win = WindowManager(screen)

    pygame.display.set_caption("TheCovenantOfChaos")

    clock = pygame.time.Clock()

    bg_image = pygame.image.load('levels/res/bg_one.png').convert_alpha()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # типо паузы(недоработанно)
                    main_win.esc()

        # TODO: установка фона + смена уровня
        screen.blit(bg_image, (0, 0))

        main_win.run()  # загрузка главного меню

        pygame.display.update()
        clock.tick(60)  # fps control

main()


