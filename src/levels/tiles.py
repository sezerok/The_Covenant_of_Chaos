import pygame

class Tile(pygame.sprite.Sprite):
    # TODO: подгрузить текстуры
    # TODO: настроить текстурки

    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size, size)) # основа-плитка
        self.image.fill('grey') # заливка плитки платформы
        # self.main_ground_image = pygame.image.load(
        #     'D:/Python/The_Covenant_of_Chaos/src/levels/res/ground_main.png').convert()
        # self.image = pygame.transform.scale(self.main_ground_image, (size, size))
        self.rect = self.image.get_rect(topleft=pos) # определение расположения

    def update(self, x_shitf):
        self.rect.x += x_shitf