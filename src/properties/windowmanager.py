from src.properties.buttons import *
from  src.levels.level import Level
from src.properties.settings import *
import pygame

class WindowManager:
    def __init__(self, surface):
        pygame.init()
        self.initial_number = 0  # номер отображаемого окна
        self.display_surface = surface
        self.level = Level(level_map, self.display_surface)
        self.button_start_game = button("Играть", 40, 400, 100, (255, 0, 0), 200, 200)
        self.button_avtory = button("Авторы", 40, 400, 100, (255, 0, 0), 200, 350)
        self.buttun_quit = button("Выход", 40, 400, 100, (255, 0, 0), 200, 500)

    def run(self):
        mouse_pos = pygame.mouse.get_pos()
        x, y = mouse_pos
        if self.initial_number == 0:
            self.button_start_game.draw(self.display_surface)
            self.button_avtory.draw(self.display_surface)
            self.buttun_quit.draw(self.display_surface)

            self.button_start_game.blackout_and_click(x, y, (255, 0, 0), self.start_game)
            self.button_avtory.blackout_and_click(x, y, (255, 0, 0), self.razraby_ne_dauni)
            self.buttun_quit.blackout_and_click(x, y, (255, 0, 0), quit)

        if self.initial_number == 1:
            self.level.run()

        if self.initial_number == 2:
            pass

        pygame.display.flip()

    def razraby_ne_dauni(self):
        self.initial_number = 2

    def esc(self):
        if self.initial_number != 0:
            self.initial_number = 0

    def start_game(self):
        self.initial_number = 1