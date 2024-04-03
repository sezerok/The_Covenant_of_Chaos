import pygame

class Tile(pygame.sprite.Sprite):
    # TODO: подгрузить текстуры
    # TODO: настроить текстурки

    def __init__(self, pos, size, type_of_tile):
        super().__init__()
        # self.image = pygame.Surface((size, size)) # основа-плитка
        # self.image.fill('grey') # заливка плитки платформы
        # self.main_ground_image = pygame.image.load('levels/res/ground_main.png').convert()
        # self.image = pygame.transform.scale(self.main_ground_image, (size, size))
        self.select_image(type_of_tile, size)
        self.rect = self.image.get_rect(topleft=pos) # определение расположения

    def select_image(self, type_of_tile, size):
        self.main_ground_image = pygame.image.load(f'levels/res/{type_of_tile}.png').convert_alpha()
        self.image = pygame.transform.scale(self.main_ground_image, (size, size))

    def update(self, x_shitf):
        self.rect.x += x_shitf