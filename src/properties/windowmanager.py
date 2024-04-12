from src.properties.buttons import *
from src.levels.level import Level
from src.properties.settings import *
import pygame


class WindowManager:
    def __init__(self, surface):
        pygame.init()
        self.initial_number = 0  # номер отображаемого окна
        self.display_surface = surface
        self.level = Level(level_map, self.display_surface)
        self.button_start_game = Button("Играть", 40, 400, 100, (132, 133, 179), 200, 200)
        self.button_avtory = Button("Авторы", 40, 400, 100, (132, 133, 179), 200, 350)
        self.button_quit = Button("Выход", 40, 400, 100, (132, 133, 179), 200, 500)

    def run(self):
        if self.initial_number == 0:
            self.main_menu()

        if self.initial_number == 1:
            self.level.run()

        if self.initial_number == 2:
            self.make_text((screen_width / 3, 200), "Наша команда:", 72, (13, 12, 11))
            self.make_text((screen_width / 5, 300), "Разработчики:", 62, (13, 12, 11))
            self.make_text((screen_width / 5, 350), "- Sezer_Ok       - ecrsty", 58, (13, 12, 11))
            self.make_text((screen_width / 5, 450), "Дизайнеры:", 62, (13, 12, 11))
            self.make_text((screen_width / 5, 500), "- Amarie           - Степанова Екатерина", 58, (13, 12, 11))

        pygame.display.flip()

    def make_text(self, pos, text, font_size, font_color):
        font = pygame.font.Font(None, font_size)
        text_surface = font.render(text, True, font_color)
        text_rect = text_surface.get_rect(midleft=pos)
        self.display_surface.blit(text_surface, text_rect)

    def main_menu(self):
        mouse_pos = pygame.mouse.get_pos()
        x, y = mouse_pos

        self.button_start_game.draw(self.display_surface)
        self.button_avtory.draw(self.display_surface)
        self.button_quit.draw(self.display_surface)

        self.button_start_game.blackout_and_click(x, y, (101, 102, 158), self.start_game)
        self.button_avtory.blackout_and_click(x, y, (101, 102, 158), self.razraby_ne_dauni)
        self.button_quit.blackout_and_click(x, y, (101, 102, 158), quit)

    def esc(self):
        if self.initial_number != 0:
            self.initial_number = 0

    def start_game(self):
        self.initial_number = 1

    def razraby_ne_dauni(self):
        self.initial_number = 2
