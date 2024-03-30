import pygame

class Tile(pygame.sprite.Sprite):
    # TODO: подгрузить текстуры
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size, size)) # основа-плитка
        self.image.fill('grey') # заливка плитки платформы
        self.rect = self.image.get_rect(topleft=pos) # определение расположения

    def update(self, x_shitf):
        self.rect.x += x_shitf