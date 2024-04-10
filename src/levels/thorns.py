import pygame
#TODO загрузить текстуры
class Thorn(pygame.sprite.Sprite):
    def __init__(self,size,pos):
        super().__init__()
        self.image = pygame.Surface((size, size))  # основа-плитка
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect(topleft=pos)  # определение расположения
    def damage(self):
        return 10

    def update(self, x_shitf):
        self.rect.x += x_shitf