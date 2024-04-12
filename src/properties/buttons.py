import pygame


class Button():
    def __init__(self, text, text_size, width, height, button_color, o_x, o_y):
        self.posX = o_x
        self.posY = o_y
        self.width = width
        self.height = height
        self.text = text
        self.text_size = text_size
        self.button_color = button_color
        self.rect = pygame.Rect(self.posX, self.posY, self.width, self.height)

    # отображение кнопки на экране
    def draw(self, surface):
        pygame.draw.rect(surface, self.button_color, self.rect)
        font = pygame.font.SysFont(None, 36)
        text_surface = font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    # обработка наведения мыши и нажатия
    def blackout_and_click(self, x, y, first_color, another_func):
        if (x > self.posX) and (x < self.width + self.posX) and (y > self.posY) and (y < self.height + self.posY):
            self.button_color = (128, 128, 128)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    another_func()
        else:
            self.button_color = first_color

    # для отладки
    def info(self):
        print(self.posX, self.width + self.posX, self.posY, self.height + self.posY)
