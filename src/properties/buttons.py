import pygame
class button():

    def __init__(self, text, text_size, width, height, button_color, o_x, o_y):
        self.o_x = o_x
        self.o_y = o_y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.o_x, self.o_y, self.width, self.height)
        self.text = text
        self.text_size = text_size
        self.button_color = button_color

    def draw(self, surface):
        pygame.draw.rect(surface, self.button_color, self.rect)
        font = pygame.font.SysFont(None, 36)
        text_surface = font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def blackout_and_click(self, x, y, first_color, another_func):
        if (x > self.o_x) and (x < self.width + self.o_x) and (y > self.o_y) and (y < self.height + self.o_y):
            self.button_color = (128, 128, 128)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    another_func()
        else:
            self.button_color = first_color

    # для отладки
    def info(self):
        print(self.o_x, self.width + self.o_x, self.o_y, self.height + self.o_y)